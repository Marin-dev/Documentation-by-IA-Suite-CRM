# SaveConfig.php

**Chemin :** `modules/SecurityGroups/SaveConfig.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Script d'action qui sauvegarde la configuration SecuritySuite (parametres d'heritage, de filtrage, de popup, etc.) et gere les groupes par defaut. Appele depuis la page de configuration admin.

## Type
controller (action script)

## Dependances cles
- `Configurator` — sauvegarde dans `$sugar_config`
- `SecurityGroup::saveDefaultGroup`, `SecurityGroup::removeDefaultGroup`
- `Administration`

## Exports / Symboles principaux
- Parametres de configuration sauvegardees :
  - `securitysuite_additive`, `securitysuite_strict_rights`, `securitysuite_filter_user_list`
  - `securitysuite_user_role_precedence`, `securitysuite_user_popup`, `securitysuite_popup_select`
  - `securitysuite_inherit_creator`, `securitysuite_inherit_parent`, `securitysuite_inherit_assigned`
  - `securitysuite_inbound_email`
  - `addAjaxBannedModules` : SecurityGroups est ajoute

## Interactions
- **Appelle :** `SecurityGroup::saveDefaultGroup/removeDefaultGroup`, `Configurator->handleOverride()`
- **Appele par :** formulaire config.html/config.php

## Notes
- Ajoute automatiquement `SecurityGroups` dans `addAjaxBannedModules`.
