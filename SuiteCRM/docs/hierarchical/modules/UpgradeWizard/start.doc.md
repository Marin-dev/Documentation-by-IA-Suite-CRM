# start.php

**Chemin :** `modules/UpgradeWizard/start.php`
**Type :** PHP - Script d'action (début de mise à jour)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Première étape du wizard de mise à jour côté serveur. Initialise le statut de progression de la mise à jour à `'in_progress'` pour l'étape `'start'`.

## Type
helper

## Dépendances clés
- `logThis()` — journalisation
- `set_upgrade_progress()` — suivi de progression

## Exports / Symboles principaux
Aucune classe. Script procédural.

## Interactions
- **Appelé par :** wizard UpgradeWizard (étape start)
- **Appelle :** `logThis()`, `set_upgrade_progress('start', 'in_progress')`

## Notes
- Log initial : "Upgrade started. At start.php".
