# view.list.php

**Chemin :** `modules/Home/views/view.list.php`
**Type :** PHP - View
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Vue "liste" du module Home, qui correspond en réalité au rendu du tableau de bord principal. Étend `ViewList` pour inclure `modules/Home/index.php` et gérer les erreurs de dépassement de taille POST.

## Type
view

## Dépendances clés
- `ViewList` (classe parente, framework SuiteCRM)
- `modules/Home/index.php` (include dans `display()`)
- `$GLOBALS['app_strings']` — messages d'erreur upload

## Exports / Symboles principaux
- `HomeViewList` (classe) — étend `ViewList`
  - `display()` — inclut `index.php` après vérification des erreurs POST
  - `processMaxPostErrors()` — détecte et affiche les erreurs de dépassement `post_max_size`/`upload_max_filesize`

## Interactions
- **Appelé par :** dispatcher de vues SuiteCRM (`?module=Home&action=index`)
- **Appelle :** `modules/Home/index.php`, `ini_get('post_max_size')`, `ini_get('upload_max_filesize')`

## Notes
- Le nom de constructeur `ActivitiesViewList()` (ligne 46) semble être un vestige de copier-coller — il appelle le constructeur parent mais la classe s'appelle `HomeViewList`.
