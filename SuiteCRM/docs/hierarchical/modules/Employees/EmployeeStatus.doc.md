# EmployeeStatus.php

**Chemin :** `modules/Employees/EmployeeStatus.php`
**Type :** PHP - Helper (fonction de métadonnées)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Fichier helper du framework de métadonnées pour le champ `employee_status`. Fournit la fonction `getEmployeeStatusOptions()` qui génère le HTML du champ de statut employé, avec des règles d'affichage différentes selon la vue (EditView/MassUpdate pour admin, DetailView pour tous).

## Type
helper

## Dépendances clés
- `$current_user` — vérification des droits admin
- `$app_list_strings` — options de la dropdown
- `$sugar_config` — configuration (default_user_name)
- `modules/Users/vardefs.php` — champ `employee_status` défini ici

## Exports / Symboles principaux
- `getEmployeeStatusOptions($focus, $name, $value, $view)` (fonction) — génère le HTML select/span du statut employé selon la vue et les droits

## Interactions
- **Appelé par :** framework de métadonnées lors du rendu des vues Employees/Users
- **Appelle :** `is_admin()`

## Notes
- En mode EditView/MassUpdate : select disponible uniquement pour les admins.
- L'utilisateur par défaut (`default_user_name`) peut avoir un comportement spécifique (ligne 59).
