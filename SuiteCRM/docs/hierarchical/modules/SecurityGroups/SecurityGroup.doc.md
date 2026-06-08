# SecurityGroup.php

**Chemin :** `modules/SecurityGroups/SecurityGroup.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Classe centrale du systeme SecuritySuite. Gere la logique d'acces par groupe de securite : controle d'acces, heritage de groupes lors de la creation/modification d'enregistrements, gestion des groupes par defaut, et requetes SQL de filtrage par groupe.

## Type
model / service

## Dependances cles
- `SecurityGroup_sugar` (heritage) — bean de base SecurityGroup
- `DBManagerFactory` — acces direct a la DB
- `BeanFactory` — instanciation de beans (Releases, Relationships, Users)
- `$sugar_config` — parametres SecuritySuite (`securitysuite_inherit_creator`, `securitysuite_inherit_parent`, `securitysuite_inherit_assigned`, `securitysuite_strict_rights`, `securitysuite_popup_select`)
- Tables DB : `securitygroups`, `securitygroups_users`, `securitygroups_records`, `securitygroups_acl_roles`, `securitygroups_default`

## Exports / Symboles principaux
- `class SecurityGroup extends SecurityGroup_sugar`
- **Methodes statiques cles :**
  - `getGroupWhere($table_name, $module, $user_id)` — clause SQL WHERE pour filtrer par groupe
  - `getGroupJoin($table_name, $module, $user_id)` — clause SQL JOIN pour filtrage par groupe
  - `getGroupUsersWhere($user_id)` / `getGroupUsersJoin($user_id)` — filtrage des utilisateurs du meme groupe
  - `groupHasAccess($module, $id, $action)` — verifie si l'utilisateur courant a acces via groupe
  - `inherit($focus, $isUpdate)` — orchestre l'heritage de groupes a la creation
  - `assign_default_groups`, `inherit_creator`, `inherit_assigned`, `inherit_parent`, `inherit_parentQuery` — strategies d'heritage
  - `inheritOne($user_id, $record_id, $module)` — heritage si l'utilisateur est dans un seul groupe
  - `getMembershipCount($user_id)` — nombre de groupes (mis en cache en session)
  - `retrieveDefaultGroups`, `saveDefaultGroup`, `removeDefaultGroup`
  - `getSecurityModules()` — liste des modules avec relation SecurityGroups
  - `getLinkName($this_module, $rel_module)` — nom du lien de relation
  - `addGroupToRecord`, `removeGroupFromRecord`, `getUserSecurityGroups`, `getAllSecurityGroups`
  - `getPrimaryGroupID`, `getParentGroups`, `getRecordGroups`, `getParentBean`

## Interactions
- **Appelle :** `DBManagerFactory::getInstance()`, `BeanFactory::newBean/getBean`, `RelationshipHandler`
- **Appele par :** `AssignGroups`, `MassAssign.php`, `SaveConfig.php`, `SaveSecurityGroupUserRelationship.php`, hooks logiques SuiteCRM

## Notes
- `getGroupWhere` et `getGroupJoin` ont un traitement specifique pour le module `SecurityGroups` lui-meme.
- `inherit()` est l'entrypoint principal : il appelle `assign_default_groups`, `inherit_assigned`, `inherit_parent`, puis `inherit_creator` (dans cet ordre).
- `getMembershipCount` utilise `$_SESSION['securitygroup_count']` comme cache — a reinitialiser si les groupes changent.
- `groupHasAccess` supporte le mode `securitysuite_strict_rights` avec verification des roles ACL.
- `securitysuite_popup_select` : si actif et que l'utilisateur est dans plusieurs groupes, `inherit()` ne fait PAS l'heritage creator automatique.
