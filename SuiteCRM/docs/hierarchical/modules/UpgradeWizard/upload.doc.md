# upload.php

**Chemin :** `modules/UpgradeWizard/upload.php`
**Type :** PHP - Script d'action (upload du package de mise à jour)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Gère l'upload du package de mise à jour (.zip). Enregistre la progression de l'étape `'upload'` à `'in_progress'`.

## Type
helper

## Dépendances clés
- `logThis()` — journalisation
- `set_upgrade_progress()` — suivi de progression

## Exports / Symboles principaux
Aucune classe. Script procédural.

## Interactions
- **Appelé par :** wizard UpgradeWizard (étape upload)
- **Appelle :** `logThis()`, `set_upgrade_progress('upload', 'in_progress')`

## Notes
- Log initial : "At upload.php".
