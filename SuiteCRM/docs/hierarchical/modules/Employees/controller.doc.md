# controller.php

**Chemin :** `modules/Employees/controller.php`
**Type :** PHP - Controller
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Contrôleur du module Employees. Gère les actions d'édition et de détail avec des vérifications de sécurité : seuls les admins ou l'employé lui-même peuvent accéder à l'édition de son profil.

## Type
controller

## Dépendances clés
- `SugarController` — classe parente
- `is_admin($current_user)` — vérification admin
- `$GLOBALS['current_user']->id` — identité de l'utilisateur connecté

## Exports / Symboles principaux
- `EmployeesController` (classe, étend `SugarController`)
  - `action_editview()` — redirige vers 'edit' si admin ou propriétaire, `sugar_die` sinon

## Interactions
- **Appelé par :** framework SugarCRM (dispatcher d'actions module Employees)
- **Appelle :** `is_admin()`, `sugar_die()`

## Notes
- Sécurité : `sugar_die("Unauthorized access to employees.")` si l'utilisateur tente d'éditer un autre employé.
- Reproduit la même vérification que `Save.php`.
