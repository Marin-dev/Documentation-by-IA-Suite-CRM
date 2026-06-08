# project_relationMetaData.php

**Chemin :** `metadata/project_relationMetaData.php`
**Type :** config (métadonnées de table de jointure polymorphe projet)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table `project_relation` qui matérialise de multiples relations entre les projets (`Project`) et d'autres entités (Accounts, Contacts, Opportunities, Quotes) via une colonne discriminante `relation_type`. Table polymorphe clé pour la gestion des projets.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['project_relation']` | variable globale PHP | Définition de la table de jointure polymorphe |

### Structure de la table `project_relation`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | id | Clé primaire UUID (requis) |
| `project_id` | id | FK vers `project.id` (requis) |
| `relation_id` | id | UUID de l'entité liée (polymorphe, requis) |
| `relation_type` | enum | Type de relation : discriminant polymorphe (requis) |
| `deleted` | bool | Soft delete (défaut : 0, requis) |
| `date_modified` | datetime | Horodatage (requis) |

### Relations définies via `relation_type`

| Relation | Module LHS | Module RHS | Valeur `relation_type` |
|---|---|---|---|
| `projects_accounts` | `Accounts` | `Project` | `Accounts` |
| `projects_contacts` | `Project` | `Contacts` | `Contacts` |
| `projects_opportunities` | `Project` | `Opportunities` | `Opportunities` |
| `projects_quotes` | `Project` | `Quotes` | `Quotes` |

## Interactions

- **Appelé par :** module Project, modules Accounts, Contacts, Opportunities, Quotes
- **Appelle :** rien

## Notes

- Table polymorphe : une seule table couvre 4 types de relations (Accounts, Contacts, Opportunities, Quotes).
- `relation_type` reference `project_relation_type_options` : valeurs possibles définies dans les dropdown options de SuiteCRM.
- Asymétrie dans la définition de `projects_accounts` : le LHS et RHS sont inversés par rapport aux autres relations (Account → Project au lieu de Project → Account).
