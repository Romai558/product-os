# Skill — /pm-prototype

**Décision** : la solution est-elle visuellement prête (composants, états, flow) pour le développement, et les hypothèses Value/Usability du PRD tiennent-elles toujours une fois vues concrètement construites.
**Entrées** : `04-scope.md` (validé PM) ; `design-system.md` ; `ui-checklist.md`
**Sortie** : `outputs/specs/[feature]/05-prototype.md` + écrans construits dans `pencils/[cible]-ds.pen`
**Bloque si** : quality gate `ui-checklist.md` en Fail non résolu ; une hypothèse VAL/USA du PRD passe à `contradicted` pendant la construction (bloque le passage à `/pm-tickets`, pas cette skill elle-même)
**Met à jour** : `evidence-register.md` (si contradiction détectée) ; `design-system.md` (Mode B, proposé)

**Étape 2.5 du workflow delivery.** Transforme un scope validé en specs visuelles ancrées sur le Design System. Fonctionne avec un DS existant (Mode A) ou sans DS du tout (Mode B — le DS émerge au fil des specs).

Pas de craft UI dans Figma : c'est la réflexion UX et le raisonnement sur les composants qui priment. L'IA génère les specs — le PM reste garant de la logique UX.

> Inspiré du workflow 5 agents Double Diamond Voyage (Mia/Theo/Jules/Eva/Max). Version allégée : 1 agent + PM en boucle courte + quality gate.

## Déclencheur

- `/pm-prototype [chemin scope validé]`
- Après relecture et arbitrage PM du scope (`04-scope.md`), avant `/pm-tickets`

## Pré-requis

- `outputs/specs/[feature]/04-scope.md` — validé par le PM
- `tools/product-os/context/design-system.md` — peut être vide (Mode B) ou rempli (Mode A). Le fichier Pencil correspondant (si Mode A) est `tools/product-os/pencils/[cible]-ds.pen`, cible = nom lu en tête de `product-facts.md`
- `tools/product-os/standards/ui-checklist.md` — quality gate (étape 8)
- Outils MCP Pencil : `get_editor_state`, `get_variables`, `batch_get`, `batch_design`, `get_screenshot`
- Optionnel : `outputs/discovery/journey-map-*.md` — pour ancrer les écrans sur le parcours réel

## Place dans le pipeline

```
04-scope.md (validé PM)
  → /pm-prototype
  → écrans construits dans pencils/[cible]-ds.pen (ou DS Mode B équivalent)
  → outputs/specs/[feature]/05-prototype.md (spec + lien vers les frames Pencil)
  → [PM relit — quality gate ui-checklist sur les écrans réels]
  → /pm-tickets (specs visuelles intégrées)
```

## Étapes

### 0. Vérifier l'état de Pencil

Avant toute chose, `get_editor_state` pour confirmer quel fichier `.pen` est actif dans l'app. Ne jamais supposer l'état de Pencil — le MCP ne lit que le document actuellement ouvert au premier plan dans l'app, jamais un chemin de fichier passé en paramètre.

- Si le fichier actif n'est pas le DS attendu (`design-system.md` → champ "Fichier") : demander au PM de l'ouvrir dans l'app Pencil (et de fermer tout autre document ouvert, notamment "Welcome to Pencil" qui peut rester actif même en arrière-plan) avant de continuer.
- Une fois confirmé, `batch_get` avec `patterns: [{reusable: true}]` pour lister les composants réellement disponibles — ne pas se fier uniquement au tableau texte de `design-system.md`, qui peut avoir dérivé.

### 1. Lire le contexte

Lire `04-scope.md` + `design-system.md`. Déterminer le mode :

**Mode A — DS existant** : `design-system.md` contient des composants et tokens renseignés.
→ Passer à l'étape 2. L'agent s'y conforme strictement.

**Mode B — Pas de DS** : `design-system.md` est vide ou partiel.
→ Passer à l'étape 1b.

### 1b. Mode B uniquement — Bootstrapper le DS

Avant de dessiner les écrans, proposer au PM une liste de composants de base adaptés au produit et aux user stories du scope. Format :

```
Composants de base proposés pour cette feature :

Boutons : Primary, Secondary, Ghost, Destructive
Inputs : Text, Select, Search
Containers : Card, Dialog, BottomSheet
Feedback : Toast (success/error), EmptyState, Skeleton, Loader
Navigation : Header, TabBar, BackButton
[Composants métier identifiés depuis le scope]

Tokens couleur minimaux : primary, background, foreground, muted, destructive, success
Spacing : base 4px (space-1 à space-8)
Radius : sm, md, lg, full

→ Valide cette liste ou ajuste avant de continuer.
```

Attendre validation PM. Puis s'y tenir pour TOUS les écrans — pas de divergence.
En fin de session (étape 9), peupler `design-system.md` avec ce qui a été utilisé.

### 2. Inventaire des écrans

Pour chaque user story must-have : combien d'écrans ? Quel enchaînement ?
Nommer chaque écran du point de vue utilisateur ("Saisie des heures", pas "TimesheetForm").

Lister tous les écrans avant de descendre dans le détail.

### 3. Pour chaque écran — raisonnement UX

Avant de lister les composants :
- Quel est l'objectif de l'utilisateur sur cet écran ?
- Quelle est l'information la plus importante à mettre en avant ?
- Quelle action principale doit être évidente ?
- Quelles frictions à éliminer ?

### 4. Pour chaque écran — mapping composants

Décrire l'écran en termes de composants. Nommage exact depuis `design-system.md` (Mode A) ou depuis la liste validée en 1b (Mode B). En Mode A, les noms doivent correspondre aux vrais composants du `.pen` (vérifiés à l'étape 0 via `batch_get`), pas seulement au tableau texte — c'est ce mapping qui sera directement traduit en `ref` Pencil à l'étape 7.

Format : `Zone | Composant (variante) | Contenu | Token`

Signaler immédiatement si un composant nécessaire est absent → décision PM (créer / adapter / contourner).

### 5. États à couvrir

Pour chaque écran must-have :
- **Défaut** : données présentes, flow nominal
- **Vide** : premier usage, aucune donnée (`EmptyState`)
- **Chargement** : latence réseau (`Skeleton` ou `Loader`)
- **Erreur** : message explicite + action de récupération (`Toast/Destructive` ou `Alert`)

### 6. Flow de navigation

Décrire l'enchaînement entre écrans : quelle action déclenche quelle transition, depuis où on arrive, où on peut aller. Pas de dead end.

### 7. Construire les écrans dans Pencil

Le mapping composants (étape 4) et les états (étape 5) ne restent pas du texte : ils sont construits dans le `.pen` actif.

Pour chaque écran de l'inventaire (étape 2), dans l'ordre :
1. `FindEmptySpace` (dans le même `batch_design`) — chaîner via l'ID de l'écran précédent (`nodeId`) pour garder les écrans d'une même feature alignés et lisibles de gauche à droite.
2. Créer un frame top-level nommé comme l'écran (nom utilisateur, ex: "Saisie des heures"), `clip:true`, `placeholder:true` le temps de la construction.
3. Assembler le contenu via `ref` vers les composants du DS, en suivant exactement le tableau Composition de l'étape 4 — jamais de nouveaux composants ad hoc sans passer par la règle "composant manquant" de l'étape 4.
4. Un frame séparé par état pertinent (Défaut obligatoire ; Vide/Chargement/Erreur si présents dans la spec de l'étape 5) — Pencil n'a pas de toggle d'état interactif.
5. `get_screenshot` sur le frame terminé pour preuve visuelle, puis repasser `placeholder:false`.

Composant manquant découvert en cours de construction (et pas anticipé à l'étape 4) → même règle : décision PM explicite, jamais résolu en silence (improviser une couleur ou un composant non listé dans `design-system.md`).

### 8. Quality gate — ui-checklist

Passer la `ui-checklist.md` sur les écrans réellement construits dans Pencil (via les screenshots de l'étape 7), pas sur leur description texte. Scorer chaque section (✓ / △ / ✗).
Corriger les Fail avant d'écrire le fichier final.

### 8.5 Vérifier les hypothèses Value/Usability du PRD

Voir concrètement la solution construite (écrans réels, pas la description texte du scope) peut invalider une hypothèse qui semblait tenir sur le papier — c'est le moment où ce risque est le plus visible, avant que la Tech ne commence à coder dessus.

Relire les hypothèses `VAL-n`/`USA-n` listées dans `03-prd.md` § Hypothèses critiques restantes. Pour chacune : la construction des écrans la confirme-t-elle, ou la met-elle en doute ?

- **Confirmée ou inchangée** : rien à faire, continuer.
- **Doute sérieux, pas encore une certitude** : proposer une mise à jour `evidence-register.md` vers `weak-but-testable` ou `critical-gap` (Romain valide), noter le doute explicitement dans le format de sortie — n'empêche pas d'écrire le prototype.
- **Clairement invalidée par ce qu'on voit construit** : proposer le statut `contradicted` sur l'entrée `evidence-register.md` liée. **Ce statut bloquera `/pm-tickets`** tant que le retour au PRD/commitment gate n'a pas eu lieu — le signaler explicitement dans le prototype plutôt que de laisser `/pm-tickets` le découvrir plus tard.

### 9. Écrire le prototype

`tools/product-os/outputs/specs/[feature]/05-prototype.md`

Le prototype reste la source durable, mais chaque écran documenté doit pointer vers le frame Pencil correspondant (voir `**Fichier Pencil**` dans le format de sortie) — pas de spec sans écran construit.

**Mode B uniquement** : après écriture du prototype, proposer de mettre à jour `design-system.md` avec les composants et tokens utilisés. Demander confirmation PM avant d'écrire.

## Format de sortie

```markdown
# Prototype — [Nom feature]

**Scope source** : 04-scope.md
**Date** : YYYY-MM-DD
**Mode DS** : A (DS existant) / B (DS bootstrappé)
**Fichier Pencil** : `tools/product-os/pencils/[cible]-ds.pen` — écrans : [liste des noms de frames créés]
**Statut** : draft — en attente validation PM

## Quality Gate

| Section | Score |
|---|---|
| Hiérarchie visuelle | ✓ / △ / ✗ |
| Spacing & Alignement | ✓ / △ / ✗ |
| Typographie | ✓ / △ / ✗ |
| Composants | ✓ / △ / ✗ |
| États | ✓ / △ / ✗ |
| Navigation | ✓ / △ / ✗ |
| Contenu | ✓ / △ / ✗ |

**Résultat** : ✅ Excellent / 🟡 Acceptable / 🔴 À retravailler

## Hypothèses Value/Usability — vérification post-construction

- [Hypothèse VAL/USA-n] : confirmée / doute (statut proposé) / **contradicted (bloque /pm-tickets)**
- *(ou "aucune hypothèse VAL/USA remise en cause par la construction")*

## Inventaire des écrans

1. [Écran 1 — nom utilisateur]
2. [Écran 2 — nom utilisateur]

## Composants manquants → décision PM

- [ ] [Composant] : créer / adapter [composant existant] / contourner via [alternative]

---

## [Écran 1 — Nom utilisateur]

**Objectif utilisateur** : [ce qu'il cherche à accomplir]
**Action principale** : [le CTA ou geste central]

### Composition

| Zone | Composant (variante) | Contenu | Token |
|---|---|---|---|
| Header | `Header` | "[Titre]" + back | `foreground` / `space-4` |
| Corps | `Card` | [données] | `background` / `space-6` |
| Footer | `Button/Primary` | "[Label CTA]" | `primary` |

### États

- **Défaut** : [description]
- **Vide** : [`EmptyState` — illustration + CTA "[label]"]
- **Chargement** : [`Skeleton` sur la zone corps]
- **Erreur** : [`Toast/Destructive` "[message]" + retry]

### Navigation

- [Action] → [Écran suivant]
- [Retour] → [Écran précédent]

---

## Flow de navigation

[Écran 1] → (CTA) → [Écran 2] → (validation) → [Confirmation]
[Écran 2] → (erreur) → [état erreur] → (retry) → [Écran 2]
```

## Règles dures

- **Mode A** : nommage exact depuis `design-system.md`, jamais d'improvisation.
- **Mode B** : proposer le set de composants AVANT les écrans, attendre validation, s'y tenir.
- **Cohérence inter-écrans** : `Button/Primary` sur l'écran 1 = `Button/Primary` sur l'écran 3 — pas de divergence de nommage.
- **Composant manquant = décision PM explicite** — jamais résoudre en silence.
- **Tous les états couverts** sur chaque écran must-have.
- **Quality gate obligatoire** — pas de Fail non résolu avant l'écriture finale.
- **Un écran = un objectif utilisateur** — si un écran fait deux choses, le découper.
- **Flow de navigation obligatoire** — la Tech ne devine pas les transitions.
- **Chaque écran markdown a un frame Pencil construit correspondant** — pas de spec sans écran construit.
- **Ne jamais halluciner l'état du document Pencil** — toujours `get_editor_state` avant d'agir dessus (étape 0).
- **Hypothèse VAL/USA invalidée par la construction = `contradicted` proposé sur `evidence-register.md`, signalé explicitement dans le prototype** — ne pas laisser `/pm-tickets` découvrir la contradiction sans avoir été prévenu.
