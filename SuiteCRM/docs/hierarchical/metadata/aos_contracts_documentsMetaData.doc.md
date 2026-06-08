# aos_contracts_documentsMetaData.php

**Chemin :** `metadata/aos_contracts_documentsMetaData.php`
**Type :** config (métadonnées de table de jointure)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `aos_contracts_documents` qui matérialise la relation many-to-many entre les contrats (`AOS_Contracts`) et les documents (`Documents`). Permet d'attacher des documents à un contrat commercial.

## Type

config

## Dépendances clés

- Variable globale `$dictionary` (framework SugarCRM).

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['aos_contracts_documents']` | variable globale PHP | Définition de la table de jointure |

### Structure de la table `aos_contracts_documents`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `date_modified` | datetime | Horodatage de modification |
| `deleted` | bool(1) | Soft delete (défaut : 0, requis) |
| `aos_contracts_id` | varchar(36) | FK vers `aos_contracts.id` |
| `documents_id` | varchar(36) | FK vers `documents.id` |
| `document_revision_id` | varchar(36) | FK vers une révision spécifique du document |

### Index

| Nom | Type | Champs |
|---|---|---|
| `aos_contracts_documentsspk` | primary | `id` |
| `aos_contracts_documents_alt` | alternate_key | `aos_contracts_id`, `documents_id` |

### Relation

- **Type :** many-to-many
- **LHS :** module `AOS_Contracts`, table `aos_contracts`, clé `id`
- **RHS :** module `Documents`, table `documents`, clé `id`

## Interactions

- **Appelé par :** framework SugarCRM (dictionnaire de schéma), module AOS_Contracts
- **Appelle :** rien

## Notes

- Champ supplémentaire `document_revision_id` : permet de lier le contrat à une révision précise du document (pas seulement au document courant). Point d'attention : ce champ n'est pas inclus dans les index, ni dans la clé `alternate_key`.
