# cases_bugsMetaData.php

**Chemin :** `metadata/cases_bugsMetaData.php`
**Type :** config (métadonnées de table de jointure)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `cases_bugs` qui matérialise la relation many-to-many entre les cas support (`Cases`) et les bogues (`Bugs`). Permet de lier un bogue à un ou plusieurs cas support.

## Type

config

## Dépendances clés

- Variable globale `$dictionary` (framework SugarCRM).
- Protégé par la constante `sugarEntry`.

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['cases_bugs']` | variable globale PHP | Définition de la table de jointure |

### Structure de la table `cases_bugs`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `case_id` | varchar(36) | FK vers `cases.id` |
| `bug_id` | varchar(36) | FK vers `bugs.id` |
| `date_modified` | datetime | Horodatage de modification |
| `deleted` | bool(1) | Soft delete (défaut : 0) |

### Index

| Nom | Type | Champs |
|---|---|---|
| `cases_bugspk` | primary | `id` |
| `idx_cas_bug_cas` | index | `case_id` |
| `idx_cas_bug_bug` | index | `bug_id` |
| `idx_case_bug` | alternate_key | `case_id`, `bug_id` |

### Relation

- **Type :** many-to-many
- **LHS :** module `Cases`, table `cases`, clé `id`
- **RHS :** module `Bugs`, table `bugs`, clé `id`

## Interactions

- **Appelé par :** framework SugarCRM, modules Cases et Bugs
- **Appelle :** rien

## Notes

- RAS.
