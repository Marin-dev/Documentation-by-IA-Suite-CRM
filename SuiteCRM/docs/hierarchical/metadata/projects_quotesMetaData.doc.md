# projects_quotesMetaData.php

**Chemin :** `metadata/projects_quotesMetaData.php`
**Type :** config (métadonnées de table de jointure)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `projects_quotes` qui matérialise la relation many-to-many entre les projets (`Project`) et les devis (`Quotes`).

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['projects_quotes']` | variable globale PHP | Définition de la table de jointure |

### Structure de la table `projects_quotes`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `quote_id` | varchar(36) | FK vers `quotes.id` |
| `project_id` | varchar(36) | FK vers `project.id` |
| `date_modified` | datetime | Horodatage |
| `deleted` | bool(1) | Soft delete (défaut : 0) |

### Relation

- **Type :** many-to-many
- **LHS :** module `Project`, table `project`, clé `id`
- **RHS :** module `Quotes`, table `quotes`, clé `id`

## Notes

- RAS.
