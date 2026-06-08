# Save.php

**Chemin :** `modules/Employees/Save.php`
**Type :** PHP - Script d'action (sauvegarde)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Gère la sauvegarde d'un enregistrement employé. Inclut une vérification de sécurité critique : un utilisateur non-admin ne peut pas sauvegarder un enregistrement qui n'est pas le sien, empêchant la substitution d'ID admin.

## Type
helper

## Dépendances clés
- `modules/MySettings/TabController.php`
- `include/SugarFields/SugarFieldHandler.php`
- `$_POST['record']`, `$_REQUEST['display_tabs_def']`
- `$GLOBALS['current_user']`, `is_admin()`, `isAdminForModule()`

## Exports / Symboles principaux
Aucune classe ni fonction exportée. Script procédural.

## Interactions
- **Appelé par :** formulaires EditView du module Employees
- **Appelle :** `TabController`, `SugarFieldHandler`, `sugar_die()`

## Notes
- Sécurité critique (ligne 57-60) : vérifie que `$_POST['record'] == $current_user->id` pour les non-admins.
- Protection contre l'injection d'ID admin via proxy tool (commentaire en ligne 53-55).
