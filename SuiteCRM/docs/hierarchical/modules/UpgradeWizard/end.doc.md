# end.php

**Chemin :** `modules/UpgradeWizard/end.php`
**Type :** PHP - Script d'action (finalisation de mise à jour)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Étape finale du wizard de mise à jour. Effectue les tâches de nettoyage après l'installation réussie : suppression des fichiers temporaires d'upgrade, mise à jour des répertoires.

## Type
helper

## Dépendances clés
- `logThis()` — journalisation
- `$unzip_dir`, `$path`, `$sugar_config` (globaux)

## Exports / Symboles principaux
Aucune classe. Script procédural.

## Interactions
- **Appelé par :** wizard UpgradeWizard (dernière étape)
- **Appelle :** `logThis()`

## Notes
- Log initial : "[At end.php]".
