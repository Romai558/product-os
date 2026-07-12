# UI Checklist — Quality Gate `/pm-prototype`

> Adapté du ui-checklist Voyage (PR #1). Checklist générique — compléter les sections
> spécifiques produit dans `design-system.md`.
> Score par section : ✓ Pass / △ Partial (1-2 items) / ✗ Fail (3+ items ou item critique)

---

## Hiérarchie visuelle

- [ ] 1 action principale par écran (CTA évident)
- [ ] Ordre de lecture logique (haut → bas, gauche → droite)
- [ ] Niveaux de titres cohérents (h1 > h2 > h3)
- [ ] Contenu groupé logiquement
- [ ] Whitespace intentionnel (pas de remplissage)
- [ ] Éléments primaires = contraste le plus fort

---

## Spacing & Alignement

- [ ] Tout le spacing utilise les tokens (`space-1` à `space-12`)
- [ ] Pas de valeurs magiques (padding: 13px → token)
- [ ] Padding interne des cards : `space-6` (24px)
- [ ] Padding écran : `space-4` à `space-6` selon plateforme
- [ ] Éléments alignés sur la grille
- [ ] Icônes centrées avec leur texte

---

## Typographie

- [ ] Distinction heading / body claire
- [ ] Taille corps : `text-base` (16px) minimum
- [ ] Métadonnées / labels : `text-xs` ou `text-sm`
- [ ] Longueur de ligne : 45-75 caractères
- [ ] Contraste texte : 4.5:1 minimum (WCAG AA)
- [ ] Toutes les tailles depuis la type scale — pas de valeur ad hoc

---

## Composants

- [ ] Uniquement des composants du `design-system.md`
- [ ] Pas de composants dupliqués ou réinventés
- [ ] Variante précisée pour chaque composant
- [ ] Composants manquants listés explicitement → décision PM

---

## États couverts (par écran principal)

- [ ] **Défaut** : données présentes, flow nominal
- [ ] **Vide** : premier usage, aucune donnée (EmptyState)
- [ ] **Chargement** : Skeleton ou Spinner
- [ ] **Erreur** : message explicite + action de récupération

---

## Éléments interactifs

- [ ] Touch targets : min 44×44pt (iOS) / 48×48dp (Android)
- [ ] Espacement suffisant entre les targets
- [ ] Action primaire > action secondaire (taille et contraste)
- [ ] Feedback visible sur tap/click
- [ ] État disabled clairement différent de l'état actif
- [ ] Loading sur les actions asynchrones

---

## Navigation

- [ ] Localisation actuelle évidente pour l'utilisateur
- [ ] Retour arrière disponible sur chaque écran non-root
- [ ] Pattern de navigation cohérent avec `design-system.md`
- [ ] Pas de cul-de-sac (dead end)
- [ ] Flow de navigation documenté (qui mène où)

---

## Contenu

- [ ] Pas de lorem ipsum — données réalistes ou réelles
- [ ] Longueurs de texte réalistes (pas juste 2 mots)
- [ ] Cas de texte long géré (troncature, wrap)
- [ ] Dates et nombres cohérents

---

## Accessibilité (niveau de base)

- [ ] Contraste couleurs : WCAG AA (4.5:1 texte, 3:1 UI)
- [ ] Couleur jamais seule pour indiquer un état
- [ ] Icônes avec label ou clairement décoratives
- [ ] Ordre de focus logique documenté

---

## Scoring final

| Section | Score |
|---|---|
| Hiérarchie visuelle | ✓ / △ / ✗ |
| Spacing & Alignement | ✓ / △ / ✗ |
| Typographie | ✓ / △ / ✗ |
| Composants | ✓ / △ / ✗ |
| États | ✓ / △ / ✗ |
| Éléments interactifs | ✓ / △ / ✗ |
| Navigation | ✓ / △ / ✗ |
| Contenu | ✓ / △ / ✗ |
| Accessibilité | ✓ / △ / ✗ |

**Résultat global :**
- ✅ Excellent : toutes les sections Pass
- 🟡 Acceptable : pas de Fail, max 2 Partials
- 🔴 À retravailler : 1 Fail ou plus
