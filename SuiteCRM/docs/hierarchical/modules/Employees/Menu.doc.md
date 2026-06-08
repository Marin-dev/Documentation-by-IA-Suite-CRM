# Menu.php

**Chemin :** `modules/Employees/Menu.php`
**Type :** PHP - Configuration (menu)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Définit le menu du module Employees. Affiche "Nouveau Employé" uniquement aux administrateurs, et "Liste des Employés" à tous.

## Type
config

## Dépendances clés
- `$mod_strings` — LNK_NEW_EMPLOYEE, LNK_EMPLOYEE_LIST
- `$current_user` — vérification des droits admin
- `is_admin()`

## Exports / Symboles principaux
- `$module_menu` (tableau) — entrées conditionnelles selon les droits admin

## Interactions
- **Appelé par :** framework SugarCRM (chargement du menu)
- **Appelle :** `is_admin()`

## Notes
- Création d'un employé réservée aux admins. Liste accessible à tous.
