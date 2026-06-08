# project_productsMetaData.php

**Chemin :** `metadata/project_productsMetaData.php`
**Type :** config (métadonnées de table de jointure)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `projects_products` qui matérialise la relation many-to-many entre les projets (`Project`) et les produits (`Products`). Permet de lier des produits à un projet.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['projects_products']` | variable globale PHP | Définition de la table de jointure |

### Structure de la table `projects_products`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `product_id` | varchar(36) | FK vers `products.id` |
| `project_id` | varchar(36) | FK vers `project.id` |
| `date_modified` | datetime | Horodatage |
| `deleted` | bool(1) | Soft delete (défaut : 0) |

### Relation

- **Type :** many-to-many
- **LHS :** module `Project`, table `project`, clé `id`
- **RHS :** module `Products`, table `products`, clé `id`

## Notes

- Commentaire source ligne 44 : "adding project-to-products relationship".
