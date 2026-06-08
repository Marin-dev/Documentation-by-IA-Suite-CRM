# SecurityGroup_sugar.php

**Chemin :** `modules/SecurityGroups/SecurityGroup_sugar.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Classe de base generee (pattern Sugar) pour le bean SecurityGroup. Definit les proprietes et la structure ORM de base d'un groupe de securite.

## Type
model (base)

## Dependances cles
- `Basic` (heritage) — classe SugarBean simplifiee
- Table DB : `securitygroups`

## Exports / Symboles principaux
- `class SecurityGroup_sugar extends Basic`
- Proprietes : `id`, `name`, `description`, `noninheritable`, `assigned_user_id`, etc.
- `bean_implements('ACL')` — retourne true

## Interactions
- **Heritage par :** `SecurityGroup`

## Notes
- Classe intermediaire generee, ne pas modifier directement.
