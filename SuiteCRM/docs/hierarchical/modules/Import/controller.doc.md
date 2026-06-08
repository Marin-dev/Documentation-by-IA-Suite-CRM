# controller.php

**Chemin :** `modules/Import/controller.php`
**Type :** PHP - Controller
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Contrôleur du module Import. Charge le bean du module importé (vérifie `importable`), restreint l'import Users aux admins, et dispatche les actions (step1 à step4, confirm, undo, dupcheck, etc.).

## Type
controller

## Dépendances clés
- `modules/Import/Forms.php`
- `include/MVC/Controller/SugarController.php`
- `modules/Import/sources/ImportFile.php`
- `modules/Import/views/ImportListView.php`
- `SugarController` (classe parente)
- `loadBean()` — chargement du bean importable

## Exports / Symboles principaux
- `ImportController` (classe) — étend `SugarController`
  - `loadBean()` — vérifie `import_module`, charge et valide le bean

## Interactions
- **Appelé par :** dispatcher SuiteCRM (`?module=Import&action=*`)
- **Appelle :** `loadBean()`, vues Import (step1-4, confirm, dupcheck…)

## Notes
- Si `import_module` absent → vue `error`.
- Import du module Users réservé aux administrateurs.
