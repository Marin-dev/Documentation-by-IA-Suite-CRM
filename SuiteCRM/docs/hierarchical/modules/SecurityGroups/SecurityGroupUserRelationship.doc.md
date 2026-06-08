# SecurityGroupUserRelationship.php

**Chemin :** `modules/SecurityGroups/SecurityGroupUserRelationship.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Bean representant la relation entre un groupe de securite et un utilisateur. Stocke les flags `noninheritable` (non-heritable) et `primary_group` (groupe principal de l'utilisateur).

## Type
model (relation)

## Dependances cles
- `SugarBean` (heritage via `data/SugarBean.php`)
- `DBManagerFactory` — acces DB
- Table DB : `securitygroups_users`

## Exports / Symboles principaux
- `class SecurityGroupUserRelationship extends SugarBean`
- Champs : `securitygroup_id`, `user_id`, `noninheritable`, `primary_group`
- Methodes : `fill_in_additional_detail_fields()`, `create_list_query()`
- `disable_row_level_security = true`

## Interactions
- **Appele par :** `SecurityGroupUserRelationshipEdit.php`, `SaveSecurityGroupUserRelationship.php`

## Notes
- `disable_row_level_security = true` : la securite par ligne est desactivee pour cette table de relation.
- Pas de VardefManager ; schema defini directement dans `$field_defs`.
