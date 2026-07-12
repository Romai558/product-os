# Skill — /pm-ux-personas

**Décision** : quel segment/persona doit guider les décisions de design pour cette initiative.
**Entrées** : `outputs/interviews/insights-*.md` (3+ entretiens, même segment) ; `product-facts.md`
**Sortie** : `outputs/discovery/personas-[segment]-YYYY-MM-DD.md`
**Bloque si** : rien — se déclenche seulement si la sélection d'artefact discovery le recommande
**Met à jour** : `product-facts.md` (proposé)

**Artefact discovery conditionnel — pas une étape obligatoire.** Déclenché seulement si la logique de sélection d'artefact (`tools/product-os/index.md` § Sélection d'artefact discovery) identifie que l'incertitude à réduire est "qui" (segments hétérogènes pas encore caractérisés). Transforme des insights d'interviews utilisateurs en personas structurées, ancrées sur des données réelles. Alimente directement la section Personas de `product-facts.md`.

> Personas basées sur des suppositions = proto-personas. Le signaler explicitement si les données sont insuffisantes.
> Si l'incertitude porte plutôt sur la motivation/l'objectif que sur "qui", préférer JTBD (à construire). Si elle porte sur un parcours multi-étapes, préférer `/pm-journey-mapping`.

## Déclencheur

- `/pm-ux-personas [chemin insights ou texte brut]`
- Dans la boucle discovery, après `/pm-interview-insights`, sur un ensemble de 3+ entretiens du même segment — **seulement si l'artefact persona a été sélectionné**

## Pré-requis

- Fichiers `outputs/interviews/insights-*.md` (min 2-3 entretiens, même segment)
- `tools/product-os/context/product-facts.md` — personas existantes à enrichir ou invalider

## Place dans le pipeline

```
/pm-interview-insights (x3+, dans la boucle discovery)
  → [sélection d'artefact recommande "persona"]
  → /pm-ux-personas
  → outputs/discovery/personas-[segment]-YYYY-MM-DD.md
  → MAJ product-facts.md (section Personas)
  → retour à la boucle discovery (autre artefact, re-priorisation, ou /pm-commitment-gate)
```

## Étapes

### 1. Charger les insights

Lire les fichiers `insights-*.md` concernés. Identifier le segment ciblé.

### 2. Repérer les clusters

Regrouper les participants par comportements, douleurs et objectifs similaires. Viser 2-4 clusters max — au-delà, les personas se diluent.

### 3. Construire chaque persona

Pour chaque cluster, une persona. Chaque élément doit répondre : *"est-ce que ça changerait une décision de design ?"* Sinon, supprimer.

Inclure :
- **Nom + tag line** : utile, pas créatif (ex: "Le chef de chantier sous pression marge", pas "Thomas, 42 ans, aime le café")
- **Rôle / contexte d'usage** : où et quand il utilise le produit
- **Objectif principal** : ce qu'il cherche à accomplir
- **Douleurs principales** : frictions concrètes (verbatims à l'appui)
- **Comportements observés** : ce qu'il fait vraiment (pas ce qu'il dit faire)
- **Citation représentative** : verbatim exact d'un entretien
- **Niveau de maturité tech** : impacte les choix UX

### 4. Test de validité

Pour chaque persona : est-elle grounded sur au least un verbatim ? Si non → proto-persona, le signaler.

### 5. Écrire les personas

`tools/product-os/outputs/discovery/personas-[segment]-YYYY-MM-DD.md`

### 6. Proposer MAJ product-facts.md

Identifier les personas à créer, enrichir ou invalider dans `product-facts.md`. Proposer les modifications, ne pas modifier directement.

## Format de sortie

```markdown
# Personas — [Segment] — [Date]

**Source** : [liste des fichiers insights utilisés]
**Statut** : research-based / proto-persona (à valider)

---

## [Persona 1 — Tag line]

**Rôle** : ...
**Contexte d'usage** : où / quand / avec quoi

**Objectif principal** : ...

**Douleurs**
- [Douleur 1] > "[verbatim]"
- [Douleur 2] > "[verbatim]"

**Comportements observés**
- ...

**Citation représentative**
> "[verbatim exact]"

**Maturité tech** : faible / moyenne / élevée

---

## Propositions MAJ product-facts.md

- [ ] Persona [X] : créer / enrichir / invalider
```

## Règles dures

- **Non obligatoire** — ne se lance que si la sélection d'artefact discovery le recommande. Ne pas enchaîner par défaut après `/pm-interview-insights`.
- **Verbatim obligatoire** sur chaque douleur — pas d'insight sans citation.
- **Max 4 personas** — au-delà c'est du bruit.
- **Proto-persona = signalé explicitement** si données insuffisantes.
- **Tout détail doit changer une décision de design** — sinon supprimer.
