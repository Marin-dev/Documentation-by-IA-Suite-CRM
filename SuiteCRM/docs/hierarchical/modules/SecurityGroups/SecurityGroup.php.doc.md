# 📄 SecurityGroup.php

**Chemin :** `modules/SecurityGroups/SecurityGroup.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Classe principale du système SecuritySuite. Gère l'héritage de groupes de sécurité sur les enregistrements SuiteCRM : lors de la création d'un enregistrement, les groupes du créateur, du responsable assigné et/ou du parent sont automatiquement propagés. Fournit également les clauses WHERE/JOIN pour filtrer les listes par groupe.

## Rôle technique

Classe `SecurityGroup` héritant de `SecurityGroup_sugar`. Expose exclusivement des méthodes statiques (sauf `addGroupToRecord`, `getMembers`). Construit dynamiquement des requêtes SQL `INSERT INTO securitygroups_records` pour l'héritage, et des sous-requêtes EXISTS/JOIN pour le filtrage. Compatible MySQL et MSSQL.

---

## Dépendances clés

- `modules/SecurityGroups/SecurityGroup_sugar.php` — classe parente (ORM de base)
- `DBManagerFactory::getInstance()` — accès DB
- `BeanFactory::newBean('Relationships')` — détection des modules liés
- `modules/Relationships/RelationshipHandler.php` — résolution du link name
- `$sugar_config['securitysuite_*']` — configuration des modes d'héritage
- Tables DB : `securitygroups`, `securitygroups_users`, `securitygroups_records`, `securitygroups_default`

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `getGroupWhere()` | méthode statique | Clause WHERE pour filtrer les enregistrements par groupe |
| `getGroupJoin()` | méthode statique | Clause JOIN pour filtrer avec flag `securitygroup_join` |
| `getGroupUsersWhere()` / `getGroupUsersJoin()` | méthodes statiques | Filtrage des utilisateurs dans le même groupe |
| `groupHasAccess()` | méthode statique | Vérifie si l'utilisateur courant a accès à un enregistrement via son groupe |
| `inherit()` | méthode statique | Orchestre l'héritage complet (défaut + assigné + parent + créateur) |
| `assign_default_groups()` | méthode statique | Assigne les groupes par défaut à la création |
| `inherit_creator()` | méthode statique | Hérite les groupes du créateur |
| `inherit_assigned()` | méthode statique | Hérite les groupes du responsable assigné |
| `inherit_parent()` | méthode statique | Hérite les groupes du module parent (sous-panneau) |
| `inheritOne()` | méthode statique | Héritage automatique si l'utilisateur n'appartient qu'à un groupe |
| `getMembershipCount()` | méthode statique | Compte les groupes héritables de l'utilisateur (cache session) |
| `getSecurityModules()` | méthode statique | Liste des modules activés pour SecurityGroups (via relationships) |
| `addGroupToRecord()` | méthode | Ajoute un groupe à un enregistrement |
| `removeGroupFromRecord()` | méthode statique | Retire un groupe d'un enregistrement |
| `getUserSecurityGroups()` | méthode statique | Liste des groupes d'un utilisateur |
| `getAllSecurityGroups()` | méthode statique | Liste de tous les groupes |
| `getPrimaryGroupID()` | méthode statique | ID du groupe principal de l'utilisateur courant |

## Consommateurs identifiés

- `modules/Cases/Case.php` — `groupHasAccess()` dans `listviewACLHelper()`
- `modules/SecurityGroups/AssignGroups.php` — `getSecurityModules()`, `getLinkName()`
- `modules/ACLActions/ACLAction.php` — indirectement via session ACL
- Framework SugarCRM (hooks after_save) — `inherit()` appelé par logic hooks

---

## Relations clés

- **Appelé par :** hooks `after_save` de SugarCRM, `AssignGroups`, `Case.php`, `ACLController`
- **Appelle :** `DBManagerFactory`, `BeanFactory`, `RelationshipHandler`
- **Position dans le flux global :** cœur du système de sécurité par groupe, s'intercale entre la sauvegarde des beans et leur accessibilité en liste

---

## Notes

- `$sugar_config['securitysuite_strict_rights']` : si `true`, `groupHasAccess()` vérifie aussi les rôles ACL du groupe (jointure `securitygroups_acl_roles`).
- `$sugar_config['securitysuite_additive']` : si `true`, le niveau d'accès le plus permissif des rôles de groupes est appliqué.
- `$sugar_config['securitysuite_user_role_precedence']` : les rôles utilisateur priment sur les rôles de groupe.
- `getMembershipCount()` utilise `$_SESSION['securitygroup_count']` — invalidation manuelle requise si les groupes changent dans la même session.
- Module blacklist : `SchedulersJobs`, `Schedulers`, `Trackers` exclus de SecurityGroups.
