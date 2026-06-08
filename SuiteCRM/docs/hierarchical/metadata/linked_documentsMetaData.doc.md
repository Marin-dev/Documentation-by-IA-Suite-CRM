# linked_documentsMetaData.php

**Chemin :** `metadata/linked_documentsMetaData.php`
**Type :** config (métadonnées de table de jointure polymorphe)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table `linked_documents` qui matérialise la relation polymorphe entre différents types de beans (Contracts, Leads, ContractTypes) et les documents. Supporte plusieurs relations via une colonne discriminante `parent_type`.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['linked_documents']` | variable globale PHP | Définition de la table de jointure polymorphe |

### Structure de la table `linked_documents`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `parent_id` | varchar(36) | UUID du bean parent (polymorphe) |
| `parent_type` | varchar(25) | Type du bean parent (discriminant) |
| `document_id` | varchar(36) | FK vers `documents.id` |
| `document_revision_id` | varchar(36) | FK vers une révision spécifique |
| `date_modified` | datetime | Horodatage |
| `deleted` | bool(1) | Soft delete (défaut : 0) |

### Index

| Nom | Type | Champs |
|---|---|---|
| `linked_documentspk` | primary | `id` |
| `idx_parent_document` | alternate_key | `parent_type`, `parent_id`, `document_id` |

### Relations définies (via `relationship_role_column = parent_type`)

| Relation | LHS Module | Valeur `parent_type` |
|---|---|---|
| `contracts_documents` | `Contracts` | `Contracts` |
| `leads_documents` | `Leads` | `Leads` |
| `contracttype_documents` | `ContractTypes` | `ContracTemplates` (faute de frappe) |

## Interactions

- **Appelé par :** modules Contracts, Leads, ContractTypes, module Documents
- **Appelle :** rien

## Notes

- Pattern polymorphe : une seule table sert plusieurs relations en filtrant sur `parent_type`.
- Faute de frappe ligne 76 : `relationship_role_column_value` = `'ContracTemplates'` (lettre `t` manquante dans `Contracts`) — peut provoquer des problèmes de relation.
- Champ `document_revision_id` : lie le bean à une révision spécifique du document, pas seulement au document courant.
