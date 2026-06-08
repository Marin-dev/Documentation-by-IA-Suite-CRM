# UploadFileCheck.php

**Chemin :** `modules/UpgradeWizard/UploadFileCheck.php`
**Type :** PHP - Helper (vérification d'upload)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Script AJAX de vérification de la taille d'un fichier avant son upload dans le wizard de mise à jour. Compare la taille du fichier avec les limites PHP (`upload_max_filesize`, `post_max_size`) et retourne la taille si elle dépasse les limites.

## Type
helper

## Dépendances clés
- `include/JSON.php` — décodage JSON
- `include/upload_file.php` — `return_bytes()`
- `$_REQUEST['file_name']` — nom du fichier à vérifier

## Exports / Symboles principaux
Aucune classe ni fonction exportée. Script procédural.

## Interactions
- **Appelé par :** wizard UpgradeWizard (AJAX, sélection du fichier de mise à jour)
- **Appelle :** `return_bytes()`, `filesize()`

## Notes
- Protection contre les chemins `phar://` (ligne 60) — sécurité.
- Retourne la taille du fichier si trop grand, sinon rien.
