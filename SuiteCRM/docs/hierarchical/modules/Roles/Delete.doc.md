# Delete.php

**Chemin :** `modules/Roles/Delete.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Script d'action qui supprime (soft delete) un role. Appelle `mark_deleted()` sur le bean Role.

## Type
controller (action script)

## Dependances cles
- `BeanFactory::newBean('Roles')`

## Interactions
- **Appelle :** `$focus->mark_deleted($_REQUEST['record'])`
- **Appele par :** bouton Supprimer de la vue detail Roles

## Notes
- Soft delete uniquement (flag `deleted=1`).
