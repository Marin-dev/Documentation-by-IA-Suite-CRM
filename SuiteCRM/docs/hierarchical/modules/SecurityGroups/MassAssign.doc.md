# MassAssign.php

**Chemin :** `modules/SecurityGroups/MassAssign.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Script d'action qui assigne ou retire un groupe de securite a plusieurs enregistrements en masse depuis la vue liste (mass update).

## Type
controller (action script)

## Dependances cles
- `modules/SecurityGroups/SecurityGroup.php`
- `include/formbase.php`
- `BeanFactory::newBean('SecurityGroups')`
- `$_REQUEST['return_module']`, `$_REQUEST['massassign_group']`, `$_REQUEST['uid']`

## Exports / Symboles principaux
- Script PHP sans classe. Lit `$_POST['mass']` (liste d'IDs), puis appelle `$rel->add()` ou `$rel->delete()` sur la relation SecurityGroups de chaque enregistrement.

## Interactions
- **Appelle :** `SecurityGroup::getLinkName()`, `$sugarbean->load_relationship()`, `$rel->add()`, `$rel->delete()`
- **Appele par :** formulaire `MassAssign_SecurityGroups` (genere par `AssignGroups::mass_assign`)

## Notes
- Supporte 3 modes : `selected` (checkboxes), `page` (toute la page), `entire` (toute la liste via export_where).
- Verification MD5 de `export_where` pour securiser le mode `entire` (ligne ~51-54).
- Redirige vers `return_action`/`return_module` apres traitement.
