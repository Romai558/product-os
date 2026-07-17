# Contribuer à Product OS

## Avant de proposer un changement d'architecture

Toute évolution suit la gouvernance définie dans [`tools/product-os/index.md`](tools/product-os/index.md) § Gouvernance des évolutions (Observation → Problème → Hypothèse → Évolution) — pas répétée ici pour éviter deux versions de la même règle. Une proposition qui ne peut pas citer un usage concret n'est pas prête à être discutée en architecture.

## Format des skills

Chaque `.claude/skills/pm-*.md` suit le header à 5 champs et le test de garde-fou définis dans [`tools/product-os/index.md`](tools/product-os/index.md) § Header standardisé des skills — c'est la définition canonique, ne pas la redupliquer ici.

## Linter

```bash
python3 tools/product-os/lint-pm-skills.py
```

Vérifie : présence des 5 champs de header, références à des fichiers/skills inexistants, collisions de numérotation des outputs, cohérence bidirectionnelle skills ↔ `index.md`. Volontairement simple (regex sur les headers structurés) — pas de parseur Markdown/dépendances complet.

### Annoter une exception volontaire

Si une skill référence intentionnellement une autre skill absente (historique — fusionnée ou supprimée — ou prospective — pas encore construite), annoter la ligne concernée :

```markdown
Cette fonctionnalité a été fusionnée dans `/pm-autre-skill`. <!-- lint-ok: raison courte -->
```

- La justification est obligatoire — une annotation vide (`<!-- lint-ok: -->`) est signalée comme erreur.
- Seule l'occurrence sur cette ligne est couverte — toute autre mention non annotée de la même skill ailleurs continue d'être signalée. Ce n'est pas une allowlist globale.

Une sortie du linter sans erreur doit vouloir dire "tout est cohérent" — ne pas contourner un warning autrement qu'en l'annotant explicitement avec une raison.
