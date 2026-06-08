# remove_actions.php

**Chemin :** `modules/ACL/remove_actions.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Script de desinstallation qui supprime les actions ACL (soft delete) de la table `acl_actions` pour tous les modules.

## Type
script de desinstallation

## Dependances cles
- `ACLAction::removeActions($category, $type)`
- `$beanList`, `BeanFactory`

## Interactions
- **Appele par :** processus de desinstallation SuiteCRM

## Notes
- Inverse de `install_actions.php`.
