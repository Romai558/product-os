# Skill — /pm-release

**Décision** : est-on prêt à shipper en sécurité, et comment rendre le lancement légible aux parties prenantes.
**Entrées** : `06-tickets.md` (ou `sprint-plan-YYYY-MM-DD.md` si utilisé) ; `launch-readiness-checklist.md` ; `product-facts.md` ; `product-strategy.md` ; optionnel `03-prd.md`
**Sortie** : `outputs/specs/[feature]/07-release.md`
**Bloque si** : `launch-readiness-checklist.md` scorée 🔴 — ne poursuit pas vers les release notes tant que le scoring n'est pas au moins 🟡
**Met à jour** : `decision-log.md` (si le go/no-go n'est pas trivial)

**Étape post-delivery.** Couvre le **launch readiness gate juste avant le ship** (checklist dédiée, cf. `launch-readiness-checklist.md`) ET la préparation du lancement une fois shippé : release notes utilisateurs, stakeholder map, plan de communication Sales/CS.

Sources : inspiré de phuryn/pm-skills (release-notes + stakeholder-map).

## Déclencheur

- `/pm-release [chemin ou nom feature]`
- **Avant le ship** pour passer la Launch Readiness Checklist (go/no-go)
- **Après ship en production, avant communication externe** pour les release notes et le plan de comm

## Pré-requis

- `outputs/specs/[feature]/06-tickets.md` ou liste des tickets prêts/shippés
- `tools/product-os/standards/launch-readiness-checklist.md` — quality gate (étape 0)
- `tools/product-os/context/product-facts.md` — personas + features existantes
- `tools/product-os/context/product-strategy.md` — OKRs
- Optionnel : `03-prd.md` (problème initial + valeur visée, pour cohérence du messaging)

## Place dans le pipeline

```
06-tickets.md (ou sprint-plan-YYYY-MM-DD.md si utilisé)
  → /pm-release — passe launch-readiness-checklist.md (avant le ship, go/no-go)
  → ship en production
  → /pm-release — Release Notes + Stakeholder Map (après ship)
  → outputs/specs/[feature]/07-release.md
  → [PM relit + valide messaging]
  → Communication Sales / CS / clients
  → /pm-data-analysis (post-ship)
```

## Étapes

### 0. Launch Readiness — passer la checklist

À traiter **avant** de shipper, pas après. Passer `tools/product-os/standards/launch-readiness-checklist.md` (instrumentation / rollout / critères de rollback / go-no-go) et reporter le scoring (✅/🟡/🔴) dans le format de sortie. Ne pas réécrire les critères ici — la checklist est la source de vérité, ce fichier ne fait que rapporter le résultat de son passage pour cette initiative précise.

Si le scoring est 🔴 : s'arrêter, ne pas passer aux release notes.

### 1. Release notes — voix utilisateur

Rédiger la release note **du point de vue utilisateur**, pas du point de vue technique.

- Ce que l'utilisateur peut faire maintenant qu'il ne pouvait pas faire avant
- En langage simple, sans jargon technique
- Format : titre accrocheur + 2-3 bullets bénéfice + call to action si applicable
- Ton : confiant, concret, pas promotionnel

Ne pas lister les tickets fermés. Ne pas parler d'APIs, de migrations, de refacto.

### 2. Stakeholder map — qui est concerné

Identifier les parties prenantes par la grille **Impact × Intérêt** :

- **Informer** (impact fort, intérêt faible) : tenir au courant, format court
- **Gérer activement** (impact fort, intérêt fort) : aligner avant communication externe, avoir une réponse aux objections
- **Monitorer** (impact faible, intérêt faible) : liste, pas d'action pro-active
- **Impliquer** (impact faible, intérêt fort) : boucler en temps réel si questions

Catégories typiques : Sales, CS/Support, Marketing, Ops, Direction, Clients (segments concernés), Équipe Tech.

### 3. Plan de communication

Pour chaque stakeholder à gérer activement ou informer :
- **Canal** : Slack / email / réunion / Notion / Linear
- **Timing** : avant/pendant/après ship
- **Message clé** : une phrase adaptée à leur contexte
- **Action attendue** : qu'est-ce qu'ils doivent faire avec cette info ?

Pour Sales et CS : préparer les éléments de réponse aux questions clients fréquentes (FAQ interne).

### 4. Écrire le doc release

`tools/product-os/outputs/specs/[feature]/07-release.md`

## Format de sortie

```markdown
# Release — [Nom feature]

**Ship date** : YYYY-MM-DD
**Source** : 06-tickets.md
**Périmètre** : [fonctionnalités incluses — niveau utilisateur]

---

## Launch Readiness

**Scoring `launch-readiness-checklist.md`** : ✅ Prêt / 🟡 Prêt sous réserve / 🔴 Pas prêt
**Réserves si 🟡** : [ce qui reste partiel, et pourquoi le go est accepté quand même]
**Go/no-go** : [décision] — [référence decision-log.md si non trivial]

---

## Release Notes — version utilisateur

### [Titre accrocheur de la feature]

[1-2 phrases contexte : quel problème ça résout]

Ce que vous pouvez faire maintenant :
- **[Bénéfice 1]** : [description concrète]
- **[Bénéfice 2]** : [description concrète]
- **[Bénéfice 3 si applicable]**

[CTA si applicable : "Disponible dans [section de l'outil]"]

---

## Stakeholder Map

| Stakeholder | Impact | Intérêt | Stratégie |
|---|---|---|---|
| Sales | Fort | Fort | Gérer activement — brief avant lancement |
| CS/Support | Fort | Fort | Gérer activement — FAQ + brief |
| Direction | Moyen | Faible | Informer — summary 3 lignes |
| Tech | Faible | Fort | Impliquer — retour feedback |

---

## Plan de communication

### Sales — gérer activement

- **Canal** : Réunion sync OU Slack #sales
- **Timing** : J-1 avant communication externe
- **Message clé** : "[Ce que ça leur permet de pitcher aux prospects]"
- **Actions attendues** : tester la feature, préparer le discours
- **FAQ anticipée** :
  - Q : [Question client fréquente] → R : [Réponse]
  - Q : [Question] → R : [Réponse]

### CS / Support — gérer activement

- **Canal** : Notion + Slack #support
- **Timing** : J-0 au ship
- **Message clé** : "[Ce que les clients vont voir et demander]"
- **Actions attendues** : MAJ knowledge base, préparer les réponses
- **FAQ anticipée** :
  - Q : [Question client fréquente] → R : [Réponse]
  - Q : [Question] → R : [Réponse]

### [Autre stakeholder]

- **Canal** : ...
- **Timing** : ...
- **Message clé** : ...
- **Actions attendues** : ...

---

## Checklist lancement

- [ ] Launch Readiness scoring ≥ 🟡 — go/no-go tracé
- [ ] Release notes validées PM
- [ ] Brief Sales envoyé (J-1)
- [ ] Brief CS/Support envoyé + Notion MAJ
- [ ] Communication clients (newsletter / in-app / email) — si applicable
- [ ] Feature flag activé en prod (si rollout progressif)
- [ ] Monitoring post-ship confirmé actif (métriques clés — cf. /pm-data-analysis)
```

## Règles dures

- **Launch Readiness Checklist avant le ship, pas après** — gate, pas checklist rétroactive.
- **Scoring 🔴 = blocage** — ne pas poursuivre vers les release notes.
- **La checklist est la source de vérité des critères** — `/pm-release` rapporte le résultat de son passage, ne réécrit pas les critères inline.
- **Critères de rollback agréés avant le ship** — jamais improvisés après un incident.
- **Release notes en voix utilisateur** — jamais de jargon technique ou de liste de tickets.
- **Stakeholder map avant plan de comm** — ne pas rédiger des messages sans avoir identifié qui les reçoit.
- **Sales et CS en premier** — ce sont eux qui vont recevoir les questions. Toujours prioriser.
- **FAQ anticipée obligatoire pour Sales et CS** — sans ça, le brief ne sert à rien.
- **Timing de comm explicite** — "avant ship" / "J-0" / "J+1" — pas de vague "après le lancement".
