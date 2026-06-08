# vardefs.php

**Chemin :** `modules/Bugs/vardefs.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Definit le schema du bean Bug : champs, relations, index et options de la table `bugs`. Fichier de reference structurelle pour l'ORM SuiteCRM.

## Type
config / schema

## Dependances cles
- `VardefManager::createVardef()` — injection des groupes de champs standards : `default`, `assignable`, `security_groups`, `issue`
- Table DB : `bugs`
- Modules lies : `Releases`, `Users`, `Tasks`, `Notes`, `Meetings`, `Calls`, `Emails`, `Documents`, `Contacts`, `Accounts`, `Cases`, `Projects`

## Exports / Symboles principaux
- `$dictionary['Bug']` — definition complete du bean
- Champs specifiques : `found_in_release`, `fixed_in_release`, `release_name`, `fixed_in_release_name`, `source`, `product_category`
- Relations definies : `bug_tasks`, `bug_meetings`, `bug_calls`, `bug_emails`, `bug_notes`, `bugs_release`, `bugs_fixed_in_release`, `bugs_assigned_user`, etc.
- Index DB : `bug_number`, `idx_bug_name`, `idx_bugs_assigned_user`

## Interactions
- **Appelle :** `VardefManager::createVardef('Bugs', 'Bug', [...])`
- **Appele par :** framework SuiteCRM au chargement du module (autoload vardefs)

## Notes
- `audited = true` : les modifications sont tracees dans la table d'audit.
- `unified_search = true` : ce module apparait dans la recherche globale.
- `duplicate_merge = true` : la fusion de doublons est activee.
- `optimistic_locking = true` : protection contre les modifications concurrentes.
- Le groupe `security_groups` integre la gestion des groupes de securite SecurityGroups.
