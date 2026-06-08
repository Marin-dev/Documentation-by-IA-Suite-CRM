# aok_knowledgebase_categoriesMetaData.php

**Chemin :** `metadata/aok_knowledgebase_categoriesMetaData.php`
**Type :** config (métadonnées de table de jointure)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `aok_knowledgebase_categories` qui matérialise la relation many-to-many entre les articles de la base de connaissances (`AOK_KnowledgeBase`) et leurs catégories (`AOK_Knowledge_Base_Categories`). Permet de catégoriser les articles de la base de connaissances.

## Type

config

## Dépendances clés

- Variable globale `$dictionary` (framework SugarCRM).

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['aok_knowledgebase_categories']` | variable globale PHP | Définition de la table de jointure |

### Structure de la table `aok_knowledgebase_categories`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `date_modified` | datetime | Horodatage de modification |
| `deleted` | bool(1) | Soft delete (défaut : 0, requis) |
| `aok_knowledgebase_id` | varchar(36) | FK vers `aok_knowledgebase.id` |
| `aok_knowledge_base_categories_id` | varchar(36) | FK vers `aok_knowledge_base_categories.id` |

### Index

| Nom | Type | Champs |
|---|---|---|
| `aok_knowledgebase_categoriesspk` | primary | `id` |
| `aok_knowledgebase_categories_alt` | alternate_key | `aok_knowledgebase_id`, `aok_knowledge_base_categories_id` |

### Relation

- **Type :** many-to-many
- **LHS :** module `AOK_KnowledgeBase`, table `aok_knowledgebase`, clé `id`
- **RHS :** module `AOK_Knowledge_Base_Categories`, table `aok_knowledge_base_categories`, clé `id`

## Interactions

- **Appelé par :** framework SugarCRM (dictionnaire de schéma), module AOK KnowledgeBase
- **Appelle :** rien

## Notes

- Pas de garde `sugarEntry` dans ce fichier (contrairement à la plupart des autres fichiers du dossier).
- La table porte le même nom que la relation (`aok_knowledgebase_categories`) — pas de suffixe `_c` car relation définie dans le core et non via Studio.
