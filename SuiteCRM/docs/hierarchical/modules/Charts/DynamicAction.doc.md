# DynamicAction.php

**Chemin :** `modules/Charts/DynamicAction.php`
**Type :** PHP - Helper (action AJAX)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Gère la sauvegarde d'images de graphiques (PNG/JPG) envoyées en base64 depuis le front-end. Valide l'extension de fichier, décode le contenu base64, le sauvegarde dans le cache, puis vérifie l'intégrité de l'image.

## Type
helper

## Dépendances clés
- `sugar_mkdir()` / `sugar_cached()` — utilitaires de gestion du cache
- `verify_uploaded_image()` — vérification de l'intégrité de l'image
- `$_GET['DynamicAction']`, `$_POST['filename']`, `$_POST['imageStr']`

## Exports / Symboles principaux
Aucune classe ni fonction exportée. Script procédural.

## Interactions
- **Appelé par :** requêtes AJAX front-end (RGraph "Get PNG" via context menu des graphiques)
- **Appelle :** `sugar_mkdir()`, `sugar_cached()`, `file_put_contents()`, `verify_uploaded_image()`

## Notes
- Seuls les formats `jpg`, `png`, `jpeg` sont acceptés (ligne 48).
- L'image est vérifiée via `verify_uploaded_image()` après écriture — si invalide, le fichier est supprimé.
- Uniquement déclenché si `$_GET['DynamicAction'] == 'saveImage'`.
