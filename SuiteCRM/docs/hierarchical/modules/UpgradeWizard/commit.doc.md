# commit.php

**Chemin :** `modules/UpgradeWizard/commit.php`
**Type :** PHP - Script d'action (commit de mise à jour)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Script principal d'application de la mise à jour (étape "commit"). Met en pause le TrackerManager pendant la mise à jour, puis exécute les scripts de mise à jour définis dans `uw_utils.php`.

## Type
helper

## Dépendances clés
- `include/SugarLogger/SugarLogger.php` — journalisation
- `TrackerManager::getInstance()` — pause du suivi pendant la mise à jour

## Exports / Symboles principaux
Aucune classe ni fonction exportée. Script procédural.

## Interactions
- **Appelé par :** wizard UpgradeWizard (étape commit)
- **Appelle :** `TrackerManager::pause()`, `TrackerManager::unsetMonitors()`

## Notes
- Met en pause le tracker pendant la mise à jour pour éviter des enregistrements parasites.
