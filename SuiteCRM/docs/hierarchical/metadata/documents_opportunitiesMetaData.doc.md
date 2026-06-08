# documents_opportunitiesMetaData.php

**Chemin :** `metadata/documents_opportunitiesMetaData.php`
**Type :** config (metadonnees de table de jointure)
**Derniere mise a jour doc :** 2026-05-31

---

## Role

Definit la structure de la table de jointure `documents_opportunities` qui materialise la relation many-to-many entre les documents (`Documents`) et les opportunites commerciales (`Opportunities`). Permet d'attacher des documents (contrats, propositions) a des opportunites.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary["documents_opportunities"]` | variable globale PHP | Definition de la table de jointure et de la relation |

### Structure de la table `documents_opportunities`

| Colonne | Type SQL | Role |
|---|---|---|
| `id` | varchar(36) | Cle primaire UUID |
| `date_modified` | datetime | Horodatage de modification |
| `deleted` | bool(1) | Soft delete (defaut : 0, requis) |
| `document_id` | varchar(36) | FK vers `documents.id` |
| `opportunity_id` | varchar(36) | FK vers `opportunities.id` |

### Index

| Nom | Type | Champs |
|---|---|---|
| `documents_opportunitiesspk` | primary | `id` |
| `idx_docu_opps_oppo_id` | alternate_key | `opportunity_id`, `document_id` |
| `idx_docu_oppo_docu_id` | alternate_key | `document_id`, `opportunity_id` |

### Relation

- **Type :** many-to-many
- **LHS :** module `Documents`, table `documents`, cle `id`
- **RHS :** module `Opportunities`, table `opportunities`, cle `id`
- **Table de jointure :** `documents_opportunities`

## Interactions

- **Appele par :** framework SugarCRM (dictionnaire de schema, module Documents, module Opportunities)
- **Appelle :** rien

## Notes

- Les noms d'index utilises ici suivent une convention abregee (`docu_opps`, `docu_oppo`) differente des autres fichiers `documents_*`.
