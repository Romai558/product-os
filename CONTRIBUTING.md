# Contribuer à Product OS

## Avant de proposer un changement d'architecture

Ce système applique sa propre règle de gouvernance à lui-même (cf. `tools/product-os/index.md` § Gouvernance des évolutions) : toute évolution doit partir d'une **Observation** d'usage réel (quelle skill a été utilisée sur quelle initiative, ce qui a coincé), pas d'un raffinement théorique. Une proposition qui ne peut pas citer un usage concret doit d'abord être reformulée en Observation/Problème.

## Format des skills

Chaque `.claude/skills/pm-*.md` ouvre sur 5 champs standardisés, avant toute description :

```
**Décision** : la décision produit unique que cette skill tranche ou prépare
**Entrées** : fichiers/contexte nécessaires
**Sortie** : chemin du fichier produit
**Bloque si** : conditions qui empêchent l'exécution ou la progression de statut
**Met à jour** : fichiers mémoire que cette skill écrit ou propose de modifier
```

Test de garde-fou avant d'ajouter ou modifier une skill : si elle ne peut pas se résumer en une phrase "Cette skill décide...", son découpage doit être challengé.

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
