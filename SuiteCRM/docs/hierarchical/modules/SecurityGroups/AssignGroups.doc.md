# AssignGroups.php

**Chemin :** `modules/SecurityGroups/AssignGroups.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Hook logique qui intercepte les evenements SuiteCRM pour : afficher le formulaire de selection de groupe lors de la creation d'un enregistrement (mode popup), afficher la popup de groupe pour les utilisateurs, et injecter le formulaire d'assignation en masse dans les vues liste.

## Type
helper / logic hook

## Dependances cles
- `SecurityGroup` — `getSecurityModules()`, `getLinkName()`, `inheritOne()`
- `$sugar_config` — flags : `securitysuite_popup_select`, `securitysuite_user_popup`
- `BeanFactory::newBean('SecurityGroups')`
- `ACLAction::getUserAccessLevel`

## Exports / Symboles principaux
- `class AssignGroups`
- `popup_select(&$bean, $event, $arguments)` — hook after_save : assigne les groupes selectionnes via popup
- `popup_onload($event, $arguments)` — hook after_save/onload : declenche la popup JS de selection de groupe
- `mass_assign($event, $arguments)` — hook list_view_display : injecte le formulaire HTML/JS d'assignation en masse

## Interactions
- **Appelle :** `SecurityGroup::getSecurityModules()`, `SecurityGroup::getLinkName()`, `BeanFactory::newBean`
- **Appele par :** framework LogicHook SuiteCRM (evenements after_save, list_view_display)

## Notes
- `mass_assign` exclut les modules `Emails` et `ACLRoles`.
- `popup_onload` utilise `$_SESSION['securitygroups_popup']` pour les popups en attente.
- Code JS inline genere directement (heredoc).
