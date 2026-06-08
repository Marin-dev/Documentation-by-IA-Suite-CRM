# config.php

**Chemin :** `modules/SecurityGroups/config.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Vue de configuration admin de SecuritySuite. Affiche un formulaire XTemplate permettant aux administrateurs de configurer les parametres d'heritage de groupes, les popups de selection, et les groupes par defaut par module.

## Type
view (admin)

## Dependances cles
- `XTemplate` — template `config.html`
- `SecurityGroup::retrieveDefaultGroups`, `SecurityGroup::getSecurityModules`
- `Administration`, `BeanFactory::newBean('SecurityGroups')`
- `$sugar_config` — lecture des valeurs actuelles

## Interactions
- **Appelle :** `SecurityGroup::retrieveDefaultGroups()`, `SecurityGroup::getSecurityModules()`, `BeanFactory::newBean`
- **Appele par :** framework SuiteCRM (action=config, module=SecurityGroups, admin only)
- **Soumet vers :** `SaveConfig.php`

## Notes
- Reservee aux administrateurs (`is_admin` verifie ligne 18).
