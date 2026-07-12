#!/usr/bin/env python3
"""
Lint de cohérence structurelle des skills Product OS.

Vérifie, à partir des fichiers .claude/skills/pm-*.md et de tools/product-os/index.md :
1. présence des 5 champs de header standardisé (Décision/Entrées/Sortie/Bloque si/Met à jour)
2. références à des fichiers inexistants sur disque
3. références à des skills /pm-* inexistantes ou supprimées
4. collisions ou trous dans la numérotation des fichiers de sortie déclarés
5. cohérence bidirectionnelle : toute skill sur disque est référencée dans index.md, et inversement

Volontairement simple : parsing par regex sur les headers standardisés, pas de
parseur Markdown/dépendances complet. Si un contrôle butte sur du texte libre non
structuré, il est signalé comme limite plutôt que résolu par une heuristique fragile.

Annotations d'exception (mécanisme local et explicite, pas d'allowlist cachée dans
le script) : une référence à une skill volontairement absente (historique, fusionnée,
ou prospective, pas encore construite) doit porter, sur la MÊME ligne, un commentaire :

    <!-- lint-ok: raison courte -->

La justification est obligatoire (une annotation vide est signalée comme erreur).
Seule l'occurrence sur cette ligne est couverte — toute autre occurrence de la même
skill ailleurs, non annotée, continue d'être signalée.
"""
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]  # tools/product-os/lint-pm-skills.py -> racine du repo
SKILLS_DIR = REPO_ROOT / ".claude" / "skills"
INDEX_FILE = REPO_ROOT / "tools" / "product-os" / "index.md"

REQUIRED_HEADER_FIELDS = ["Décision", "Entrées", "Sortie", "Bloque si", "Met à jour"]

errors = []
warnings = []
limitations = []
annotations = []

LINT_OK_RE = re.compile(r"<!--\s*lint-ok\s*:?\s*(.*?)\s*-->")


def annotation_status(line: str):
    """None = pas d'annotation ; 'empty' = annotation sans justification ; 'valid' = OK."""
    m = LINT_OK_RE.search(line)
    if not m:
        return None
    return "valid" if m.group(1).strip() else "empty"


def find_pm_skill_files():
    return sorted(SKILLS_DIR.glob("pm-*.md"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def header_block(text: str) -> str:
    """Le header standardisé vit entre le titre H1 et le premier '## '."""
    parts = text.split("\n## ", 1)
    return parts[0]


def check_headers(skill_files):
    for f in skill_files:
        text = read(f)
        head = header_block(text)
        missing = [field for field in REQUIRED_HEADER_FIELDS
                   if not re.search(rf"\*\*{re.escape(field)}\*\*\s*:", head)]
        if missing:
            errors.append(f"{f.name}: header incomplet, champ(s) manquant(s) avant le premier '## ': {', '.join(missing)}")


def extract_field(text: str, field: str) -> str:
    m = re.search(rf"\*\*{re.escape(field)}\*\*\s*:\s*(.+)", text)
    return m.group(1) if m else ""


def extract_md_refs(line: str):
    """Chemins .md entre backticks, avec ou sans préfixe de dossier."""
    return re.findall(r"`([\w./\[\]-]+\.md)`", line)


TEMPLATE_MARKERS = ("YYYY-MM-DD", "[feature]", "[cible]", "[sujet]", "[segment]",
                    "[scenario]", "[persona]", "[participant]")


def is_templated_path(rel_path: str) -> bool:
    return any(marker in rel_path for marker in TEMPLATE_MARKERS)


def check_referenced_files_exist(skill_files):
    """Vérifie l'existence des chemins tools/product-os/... et tools/candidate-os/... cités entre backticks.

    Ignore les chemins gabarits (YYYY-MM-DD, [feature], etc.) — ce sont des motifs de
    nommage futur, pas des fichiers censés exister aujourd'hui.
    """
    pattern = re.compile(r"`(tools/(?:product-os|candidate-os)/[\w./\[\]-]+\.md)`")
    for f in skill_files:
        text = read(f)
        for rel_path in set(pattern.findall(text)):
            if is_templated_path(rel_path):
                continue
            full = REPO_ROOT / rel_path
            if not full.exists():
                errors.append(f"{f.name}: référence un fichier inexistant sur disque: {rel_path}")


def known_skill_slugs(skill_files):
    return {f.stem for f in skill_files}


PM_REF_PATTERN = re.compile(r"(?<![\w])/pm-[a-z][a-z-]*")


def unknown_refs_on_line(line: str, known_slugs) -> set:
    slugs = {m.lstrip("/") for m in PM_REF_PATTERN.findall(line)}
    return slugs - known_slugs


def check_pm_references(skill_files, known_slugs):
    """Toute mention /pm-xxx (non précédée d'un caractère alphanumérique, pour exclure
    les mentions type 'phuryn/pm-skills' qui ne sont pas des slash-commands) doit
    correspondre à une skill existante, sauf si la ligne porte une annotation
    <!-- lint-ok: raison --> valide."""
    for f in skill_files:
        for lineno, line in enumerate(read(f).splitlines(), start=1):
            unknown = unknown_refs_on_line(line, known_slugs)
            if not unknown:
                continue
            status = annotation_status(line)
            if status == "valid":
                for slug in sorted(unknown):
                    annotations.append(f"{f.name}:{lineno}: /{slug} — exception acceptée (lint-ok)")
            elif status == "empty":
                errors.append(f"{f.name}:{lineno}: annotation lint-ok présente mais sans justification")
            else:
                for slug in sorted(unknown):
                    errors.append(f"{f.name}:{lineno}: référence une skill inexistante ou supprimée: /{slug}")


def check_index_bidirectional(known_slugs):
    if not INDEX_FILE.exists():
        errors.append("tools/product-os/index.md introuvable.")
        return
    lines = read(INDEX_FILE).splitlines()
    all_index_refs = set()
    for lineno, line in enumerate(lines, start=1):
        line_refs = {m.lstrip("/") for m in PM_REF_PATTERN.findall(line)}
        all_index_refs |= line_refs
        unknown = line_refs - known_slugs
        if not unknown:
            continue
        status = annotation_status(line)
        if status == "valid":
            for slug in sorted(unknown):
                annotations.append(f"index.md:{lineno}: /{slug} — exception acceptée (lint-ok)")
        elif status == "empty":
            errors.append(f"index.md:{lineno}: annotation lint-ok présente mais sans justification")
        else:
            for slug in sorted(unknown):
                errors.append(f"index.md:{lineno}: référence une skill introuvable sur disque: /{slug}")

    missing_from_index = sorted(known_slugs - all_index_refs)
    if missing_from_index:
        errors.append(f"index.md ne référence pas ces skills pourtant présentes sur disque: {missing_from_index}")


def check_output_numbering(skill_files):
    """Extrait le fichier de Sortie déclaré par chaque skill et vérifie collisions/trous."""
    numbered = {}  # numéro -> [(skill, basename)]
    unnumbered = []
    for f in skill_files:
        text = read(f)
        sortie = extract_field(text, "Sortie")
        refs = extract_md_refs(sortie)
        if not refs:
            limitations.append(f"{f.name}: champ Sortie sans nom de fichier .md identifiable ('{sortie[:60]}...') — ignoré")
            continue
        basename = refs[0].split("/")[-1]
        m = re.match(r"^(\d{2})-", basename)
        if m:
            numbered.setdefault(m.group(1), []).append((f.name, basename))
        else:
            unnumbered.append((f.name, basename))

    for num, entries in sorted(numbered.items()):
        basenames = {b for _, b in entries}
        if len(basenames) > 1:
            errors.append(f"Collision de numérotation '{num}-': {entries}")

    nums = sorted(int(n) for n in numbered)
    if nums:
        expected = set(range(nums[0], nums[-1] + 1))
        gaps = sorted(expected - set(nums))
        if gaps:
            warnings.append(
                f"Trou(s) dans la séquence de numérotation des Sorties déclarées: {gaps} "
                f"(vérifier si intentionnel — ex: une skill de branche annexe)"
            )

    limitations.append(
        "La numérotation est vérifiée sur le champ Sortie déclaré par chaque skill, "
        "pas sur les fichiers réellement présents dans outputs/specs/[feature]/ "
        "(aucune initiative n'a encore traversé le pipeline pour le vérifier en conditions réelles)."
    )


def main():
    skill_files = find_pm_skill_files()
    if not skill_files:
        print(f"Aucune skill pm-*.md trouvée dans {SKILLS_DIR} — vérifier le chemin.")
        sys.exit(2)

    known_slugs = known_skill_slugs(skill_files)
    check_headers(skill_files)
    check_referenced_files_exist(skill_files)
    check_pm_references(skill_files, known_slugs)
    check_index_bidirectional(known_slugs)
    check_output_numbering(skill_files)

    print(f"Skills analysées : {len(skill_files)}")

    if errors:
        print(f"\n❌ {len(errors)} erreur(s) :")
        for e in errors:
            print(f"  - {e}")
    if warnings:
        print(f"\n⚠️  {len(warnings)} avertissement(s) :")
        for w in warnings:
            print(f"  - {w}")
    if limitations:
        print(f"\nℹ️  {len(limitations)} limite(s) connue(s) du linter :")
        for l in limitations:
            print(f"  - {l}")
    if annotations:
        print(f"\n📌 {len(annotations)} exception(s) annotée(s) (lint-ok, acceptées) :")
        for a in annotations:
            print(f"  - {a}")
    if not errors and not warnings:
        print("\n✅ Aucun problème détecté.")

    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
