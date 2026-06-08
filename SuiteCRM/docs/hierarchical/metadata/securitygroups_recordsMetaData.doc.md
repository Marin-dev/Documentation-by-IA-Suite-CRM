# securitygroups_recordsMetaData.php

**Chemin :** `metadata/securitygroups_recordsMetaData.php`
**Type :** config (métadonnées de table de jointure polymorphe sécurité)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table `securitygroups_records` qui matérialise la relation many-to-many polymorphe entre les groupes de sécurité (`SecurityGroups`) et tous les types d'enregistrements du CRM. Table centrale du module SecurityGroups : une seule table couvre tous les modules.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['securitygroups_records']` | variable globale PHP | Définition de la table polymorphe |

### Structure de la table `securitygroups_records`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | char(36) | Clé primaire UUID (requis) |
| `securitygroup_id` | char(36) | FK vers `securitygroups.id` |
| `record_id` | char(36) | UUID de l'enregistrement protégé (polymorphe) |
| `module` | varchar(100) | Module de l'enregistrement (discriminant) |
| `date_modified` | datetime | Horodatage |
| `modified_user_id` | char(36) | Utilisateur modificateur |
| `created_by` | char(36) | Utilisateur créateur |
| `deleted` | bool(1) | Soft delete (requis, défaut : 0) |

### Relations définies (discriminant = `module`)

Accounts, Bugs, Calls, Campaigns, Cases, Contacts, Documents, Emails, EmailTemplates, Leads, Meetings, Notes, Opportunities, Project, ProjectTask, ProspectLists, Prospects, Tasks.

## Interactions

- **Appelé par :** module SecurityGroups (SuiteCRM Security Suite), tous les modules listés ci-dessus
- **Appelle :** rien

## Notes

- Table polymorphe la plus large du repo : 18 modules couverts via un seul discriminant `module`.
- Index optimisés pour les filtres fréquents : `(module, deleted, record_id, securitygroup_id)` et `(deleted, record_id, module, securitygroup_id)`.
- Champs `modified_user_id` et `created_by` : traçabilité des modifications d'appartenance aux groupes.
