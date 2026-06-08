# vardefs.php

**Chemin :** `modules/SecurityGroups/vardefs.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Definit le schema du bean SecurityGroup : champs, relations, index.

## Type
config / schema

## Dependances cles
- Table DB : `securitygroups`
- Relations : `securitygroups_users` (link users), `securitygroups_acl_roles` (link aclroles)
- `VardefManager::createVardef()` — groupes standards

## Exports / Symboles principaux
- `$dictionary['SecurityGroup']`
- Champ specifique : `noninheritable` (bool) — groupe non-heritable
- Champs de relation utilisateur : `securitygroup_noninheritable`, `securitygroup_primary_group`
- Liens : `users`, `aclroles`

## Notes
- `audited = true`.
- Le champ `securitygroup_noninher_fields` est un champ `relate` de type `relationship_info` servant a exposer les flags de la table de jointure.
