# aos_quotes_projectMetaData.php

**Chemin :** `metadata/aos_quotes_projectMetaData.php`
**Type :** config (métadonnées de table de jointure)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `aos_quotes_project_c` qui matérialise la relation many-to-many entre les devis (`AOS_Quotes`) et les projets (`Project`). Permet de lier un devis à un projet.

## Type

config

## Dépendances clés

- Variable globale `$dictionary` (framework SugarCRM).

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['aos_quotes_project']` | variable globale PHP | Définition de la table de jointure |

### Structure de la table `aos_quotes_project_c`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `date_modified` | datetime | Horodatage de modification |
| `deleted` | bool(1) | Soft delete (défaut : 0, requis) |
| `aos_quotes1112_quotes_ida` | varchar(36) | FK vers `aos_quotes.id` |
| `aos_quotes7207project_idb` | varchar(36) | FK vers `project.id` |

### Index

| Nom | Type | Champs |
|---|---|---|
| `aos_quotes_projectspk` | primary | `id` |
| `aos_quotes_project_alt` | alternate_key | `aos_quotes1112_quotes_ida`, `aos_quotes7207project_idb` |

### Relation

- **Type :** many-to-many
- **LHS :** module `AOS_Quotes`, table `aos_quotes`, clé `id`
- **RHS :** module `Project`, table `project`, clé `id`

## Interactions

- **Appelé par :** framework SugarCRM (dictionnaire de schéma)
- **Appelle :** rien

## Notes

- Noms de colonnes avec hachage (`1112`, `7207`) : même pattern de génération automatique pour éviter les dépassements de longueur.
