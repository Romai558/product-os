# Skill — /pm-data-analysis

**Décision** : stop / iterate / scale / rollback, mémoire produit mise à jour en conséquence.
**Entrées** : `01-success-metrics.md` ; accès BI (Metabase/Mixpanel/Amplitude/SQL) ; résultats A/B bruts si applicable ; feedback qualitatif post-ship
**Sortie** : `outputs/specs/[feature]/08-data-analysis.md`
**Bloque si** : durée minimale/échantillon insuffisant → pas de décision forcée parmi les 4, report explicite de la mesure
**Met à jour** : `decision-log.md`, `product-facts.md`, `evidence-register.md`, `product-strategy.md` — les 4 systématiquement vérifiés, même pour dire "rien à mettre à jour"

**Mesure ROI post-ship.** Analyse les données d'une feature livrée : SQL pour extraire les métriques, analyse A/B si test en cours, adoption/activation/rétention par segment, feedback qualitatif, impact économique, recommandation stop/iterate/scale/rollback.

Sources : inspiré de phuryn/pm-skills (ab-test-analysis + sql-queries).

## Déclencheur

- `/pm-data-analysis [feature ou question]`
- Post-ship pour mesurer l'impact d'une feature
- Quand un A/B test doit être arbitré
- Quand une question business nécessite une requête SQL

## Pré-requis

- Accès à l'outil BI (Metabase, Mixpanel, Amplitude, SQL direct…)
- `outputs/specs/[feature]/01-success-metrics.md` — **l'objectif de mesure posé ici, pas dans le PRD** (le PRD ne fait que le charger, il ne le redéfinit pas) — ou à préciser si l'initiative n'est pas passée par le pipeline complet
- Pour A/B test : résultats bruts (conversions, impressions, durée test)
- Optionnel : `outputs/interviews/insights-*.md` postérieurs au ship — feedback qualitatif

## Place dans le pipeline

```
07-release.md (feature shippée)
  → /pm-data-analysis [J+7 / J+30]
  → outputs/specs/[feature]/08-data-analysis.md
  → décision STOP / ITERATE / SCALE / ROLLBACK
  → mise à jour mémoire — les 4 fichiers systématiquement vérifiés :
    decision-log.md · product-facts.md · evidence-register.md · product-strategy.md
```

Peut aussi être déclenché hors pipeline (question ad hoc, dashboard, audit).

## Étapes

### 1. Cadrer la question

- Quelle décision doit être prise avec cette analyse ?
- Quelles métriques sont concernées (depuis le PRD ou à définir maintenant) ?
- Quelle période d'analyse ? Quelle granularité ?
- Est-ce un A/B test ou une mesure d'impact post-ship ?

### 2. SQL — extraire les données

Générer la requête adaptée à la question. Format :
- Écrire la requête en SQL standard, annoter les parties dialecte-spécifiques si besoin
- Préciser le dialect cible (PostgreSQL / MySQL / BigQuery / Redshift…)
- Prioriser la lisibilité : CTEs nommées, commentaires sur les joins non-évidents
- Identifier les limites : données manquantes, biais de sélection, fenêtre trop courte

### 3. Analyse A/B test (si applicable)

Pour chaque test :
- **Variantes** : contrôle vs traitement, taille des groupes
- **Métrique primaire** : conversion, durée, taux d'activation…
- **Significance statistique** : p-value, confidence interval, durée minimale atteinte ?
- **Métriques secondaires** : impact sur les guardrail metrics (ne pas dégrader ce qu'on ne cherchait pas à améliorer)
- **Segmentation** : l'effet est-il homogène ou concentré sur un segment ?

Ne pas conclure si la durée minimum n'est pas atteinte ou si la taille d'échantillon est insuffisante — dans ce cas, ne pas forcer une des 4 décisions (étape 5) : recommander de **prolonger la mesure**, ce n'est pas une 5e catégorie de décision, c'est un report explicite.

### 3.5 Adoption, activation, rétention — par segment

- **Adoption** : quelle part de la population cible (définie dans `01-success-metrics.md`) a utilisé la feature au moins une fois
- **Activation** : quelle part a atteint le comportement cible défini dans l'outcome (pas juste "cliqué une fois")
- **Rétention** : cette part revient-elle utiliser la feature dans le temps, ou c'est un usage one-shot
- **Par segment** : ventiler ces 3 chiffres par segment pertinent (pas juste une moyenne globale qui masque les écarts)

### 3.6 Feedback qualitatif

- Verbatims post-ship disponibles (support, interviews, reviews) — même logique verbatim-obligatoire que `/pm-interview-insights`
- Contredisent-ils ou confirment-ils le signal quantitatif ? Une adoption forte avec un feedback qualitatif négatif est un signal à ne pas ignorer.

### 3.7 Impact économique

- Effet mesuré ou estimé sur revenu/coût/marge, même en ordre de grandeur
- Comparer à l'impact économique attendu posé au commitment gate (`00-commitment-gate.md` § Strategic fit) — écart notable = à expliquer, pas à passer sous silence

### 4. Interprétation

- Les résultats sont-ils alignés avec l'outcome posé dans `01-success-metrics.md` ?
- Y a-t-il des effets inattendus (positifs ou négatifs) ?
- Les résultats sont-ils causals ou corrélationnels ?
- Quels segments sur- ou sous-performent (cf. étape 3.5) ?

### 5. Recommandation — STOP / ITERATE / SCALE / ROLLBACK

- **SCALE** : résultats positifs, statistiquement solides → déployer à 100 % / à plus de segments
- **ITERATE** : résultats mixtes ou en dessous des attentes → identifier ce qui cloche, proposer la prochaine hypothèse
- **STOP** : résultats non concluants et le jeu n'en vaut plus la chandelle → la feature reste en l'état, on arrête d'y investir sans pour autant la retirer
- **ROLLBACK** : résultats négatifs sur les métriques primaires ou guardrails → recommander le retrait

La recommandation doit être claire et actionnable. Pas de "à surveiller" sans action concrète associée.

### 6. Mise à jour mémoire — les 4 fichiers, systématiquement

Le point de fermeture de la boucle d'apprentissage. Chaque fichier est vérifié explicitement, même pour conclure qu'il n'y a rien à mettre à jour — jamais sauté en silence.

- **`decision-log.md`** : nouvelle entrée — date, contexte (résultats de l'analyse), options considérées (les 4 catégories), choix, justification, signaux qui feraient revenir sur cette décision. Toujours écrite.
- **`product-facts.md`** : si SCALE ou ITERATE confirmé, proposer la mise à jour de la section Features existantes (statut de la feature). Proposer, ne pas appliquer directement sans validation PM (même règle que `/pm-interview-insights`). Sinon, l'écrire explicitement : "non applicable".
- **`evidence-register.md`** : clôturer les entrées `EV-n` liées à l'initiative — `sufficient` si les résultats confirment l'hypothèse, `contradicted` si les résultats l'infirment. C'est le registre qui ferme le cycle ouvert dès `/pm-prioritize`.
- **`product-strategy.md`** : si l'initiative était rattachée à un OKR ou à une sous-métrique NSM (cf. `01-success-metrics.md` § Metric de succès), proposer une mise à jour de statut (on track / at risk / off track) ou signaler la sous-métrique à revoir. Sinon, l'écrire explicitement : "non applicable, aucun OKR/NSM rattaché".

### 7. Écrire l'analyse

`tools/product-os/outputs/specs/[feature]/08-data-analysis.md`

## Format de sortie

```markdown
# Data Analysis — [Feature / Question]

**Date analyse** : YYYY-MM-DD
**Période mesurée** : [J+7 / J+30 / autre]
**Métriques cibles** : [depuis 01-success-metrics.md, ou définies ici si hors pipeline]
**Type** : A/B test / mesure post-ship / question ad hoc

---

## Requêtes SQL

### [Métrique 1 — ex: taux d'activation]

```sql
-- Dialecte : [PostgreSQL / MySQL / BigQuery]
WITH active_users AS (
  SELECT
    user_id,
    COUNT(*) AS sessions
  FROM events
  WHERE event_type = 'feature_used'
    AND created_at BETWEEN '2026-06-01' AND '2026-07-01'
  GROUP BY user_id
)
SELECT
  COUNT(DISTINCT user_id) AS activated_users,
  COUNT(DISTINCT user_id) * 100.0 / (SELECT COUNT(*) FROM users WHERE ...) AS activation_rate
FROM active_users;
```

**Limites** : [biais, données manquantes, fenêtre courte]

---

## Résultats

| Métrique | Baseline / Contrôle | Résultat / Traitement | Variation |
|---|---|---|---|
| [Métrique primaire] | [X%] | [Y%] | [+Z%] |
| [Guardrail metric] | [X] | [Y] | [impact] |

### A/B test (si applicable)

- **Groupes** : Contrôle [N=x] / Traitement [N=y]
- **Durée** : [X jours / semaines]
- **p-value** : [0.03] — significatif / non significatif
- **Confidence interval** : [IC 95% : +2% à +8%]
- **Durée minimale atteinte** : oui / non ([X jours restants] — si non, ne pas trancher STOP/ITERATE/SCALE/ROLLBACK, recommander de prolonger)

---

## Adoption, activation, rétention — par segment

| Segment | Adoption | Activation | Rétention |
|---|---|---|---|
| [Segment 1] | [%] | [%] | [%] |
| [Segment 2] | [%] | [%] | [%] |

## Feedback qualitatif

- [Verbatim ou synthèse] — source : [support / interview / review]
- **Cohérent ou en tension avec le signal quantitatif ?** [préciser]

## Impact économique

- **Mesuré/estimé** : [effet revenu/coût/marge, ordre de grandeur]
- **Vs attendu au commitment gate** : [conforme / écart — expliquer si écart]

---

## Interprétation

- [Observation 1 : aligné / en divergence avec l'outcome de 01-success-metrics.md]
- [Observation 2 : effet inattendu]
- [Segment sur-performant / sous-performant]

---

## Recommandation

**STOP / ITERATE / SCALE / ROLLBACK**

Pourquoi : [justification en 2-3 lignes]

Actions concrètes :
- [ ] [Action 1 — ex: déployer à 100% d'ici J+3 (SCALE)]
- [ ] [Action 2 — ex: suivre la rétention à J+30]
- [ ] [Action 3 — ex: investiguer segment X]

## Mise à jour mémoire

- [ ] `decision-log.md` — entrée créée
- [ ] `product-facts.md` — MAJ proposée (si SCALE/ITERATE) / "non applicable"
- [ ] `evidence-register.md` — entrées EV-n liées clôturées (sufficient / contradicted)
- [ ] `product-strategy.md` — MAJ OKR/NSM proposée / "non applicable, aucun OKR/NSM rattaché"
```

## Règles dures

- **Ne pas conclure sur un A/B test non significatif** — mentionner la durée restante estimée, reporter la décision plutôt que la forcer.
- **Décision limitée à 4 catégories : STOP / ITERATE / SCALE / ROLLBACK** — pas de "extend" comme 5e catégorie, c'est un report explicite de la décision, pas une décision.
- **Adoption/activation/rétention par segment obligatoires** — une moyenne globale seule masque les écarts, ne suffit pas.
- **Feedback qualitatif toujours mentionné**, même pour dire "aucun disponible" — ne pas sauter la section en silence.
- **Impact économique comparé à l'estimation du commitment gate** — un écart notable doit être expliqué, pas juste constaté.
- **Guardrail metrics obligatoires** — vérifier qu'on n'a pas amélioré la métrique primaire en dégradant ailleurs.
- **Recommandation = action, pas observation** — "à surveiller" n'est pas une recommandation.
- **Distinguer causalité et corrélation** — toujours nommer les limites méthodologiques.
- **Requêtes lisibles** — CTEs nommées, pas de spaghetti SQL. Un autre PM doit pouvoir relire.
- **Mise à jour mémoire = les 4 fichiers systématiquement vérifiés** — `decision-log.md` reçoit toujours une entrée ; les 3 autres sont soit mis à jour (proposé, jamais appliqué directement sans validation PM), soit explicitement marqués "non applicable". Jamais sauté en silence — c'est le point qui ferme la boucle d'apprentissage ouverte dès `/pm-prioritize`.
