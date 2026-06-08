# cancel.php

**Chemin :** `modules/UpgradeWizard/cancel.php`
**Type :** PHP - Script d'action (annulation mise à jour)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Script d'annulation du wizard de mise à jour. Nettoie les fichiers temporaires et la session d'upgrade, affiche un message de confirmation, et ramène l'administrateur à l'écran initial.

## Type
helper

## Dépendances clés
- `logThis()` — journalisation (uw_utils.php)
- `unlinkUWTempFiles()` — suppression des fichiers temporaires
- `resetUwSession()` — réinitialisation de la session d'upgrade
- `$_SESSION['install_file']` — fichier d'install temporaire

## Exports / Symboles principaux
Aucune classe ni fonction exportée. Script procédural + HTML.

## Interactions
- **Appelé par :** action "Annuler" du wizard UpgradeWizard
- **Appelle :** `unlinkUWTempFiles()`, `resetUwSession()`, `logThis()`

## Notes
- Supprime `$_SESSION['install_file']` si existant avant nettoyage.
