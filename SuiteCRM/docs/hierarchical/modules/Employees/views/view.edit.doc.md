# view.edit.php

**Chemin :** `modules/Employees/views/view.edit.php`
**Type :** PHP - Vue (édition)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Vue d'édition du module Employees. Étend `ViewEdit` avec des règles d'accès spécifiques : seuls les admins peuvent éditer n'importe quel employé. Active `useForSubpanel = true` pour l'utilisation dans les sous-panneaux.

## Type
view

## Dépendances clés
- `ViewEdit` — classe parente
- `is_admin($GLOBALS['current_user'])` — vérification admin
- `$GLOBALS['current_user']`

## Exports / Symboles principaux
- `EmployeesViewEdit` (classe, étend `ViewEdit`)
  - `$useForSubpanel` = `true`
  - `display()` — vérifie les droits admin avant d'afficher le formulaire

## Interactions
- **Appelé par :** action EditView du module Employees
- **Appelle :** `ViewEdit::display()`, `is_admin()`

## Notes
- Complète la chaîne de sécurité : `controller.php` → `Save.php` → `view.edit.php` vérifient tous les droits.
