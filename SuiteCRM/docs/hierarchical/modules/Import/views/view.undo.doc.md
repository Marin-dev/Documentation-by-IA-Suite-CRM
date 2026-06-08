# view.undo.php

**Chemin :** `modules/Import/views/view.undo.php`
**Type :** PHP - Vue (annulation d'import)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Vue permettant d'annuler le dernier import effectué. Charge les informations du dernier import et supprime les enregistrements créés lors de cette session d'import.

## Type
view

## Dépendances clés
- `modules/Import/views/ImportView.php` — classe parente
- `$mod_strings`, `$current_user`, `$current_language` (globaux)
- `$_REQUEST['import_module']` — module dont annuler l'import

## Exports / Symboles principaux
- `ImportViewUndo` (classe, étend `ImportView`)
  - `$pageTitleKey` = `'LBL_UNDO_LAST_IMPORT'`
  - `display()` — affiche la confirmation d'annulation avec le nom du module

## Interactions
- **Appelé par :** action `Undo` du module Import
- **Appelle :** `return_module_language()` pour récupérer le nom du module cible

## Notes
- L'annulation est destructive — supprime les enregistrements créés lors du dernier import.
