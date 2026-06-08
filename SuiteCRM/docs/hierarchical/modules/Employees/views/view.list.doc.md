# view.list.php

**Chemin :** `modules/Employees/views/view.list.php`
**Type :** PHP - Vue (liste)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Vue liste du module Employees. Désactive la suppression et l'email en masse dans la liste. Désactive la sélection multiple pour les non-admins des Users. Surcharge la préparation du formulaire de recherche pour ajouter des clauses WHERE supplémentaires.

## Type
view

## Dépendances clés
- `ViewList` — classe parente
- `ListViewSmarty` — affichage de liste
- `$GLOBALS['current_user']->isAdminForModule('Users')` — contrôle des droits

## Exports / Symboles principaux
- `EmployeesViewList` (classe, étend `ViewList`)
  - `preDisplay()` — configure `$this->lv` (désactive delete, email, multiSelect pour non-admins)
  - `prepareSearchForm()` (surcharge) — ajoute des clauses WHERE au formulaire de recherche

## Interactions
- **Appelé par :** action ListView du module Employees
- **Appelle :** `ListViewSmarty`, `ViewList`

## Notes
- La suppression d'employés depuis la liste est désactivée (`$this->lv->delete = false`).
