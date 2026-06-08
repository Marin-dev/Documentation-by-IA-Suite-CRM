# contacts_casesMetaData.php

**Chemin :** `metadata/contacts_casesMetaData.php`
**Type :** config (métadonnées de table de jointure)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `contacts_cases` qui matérialise la relation many-to-many entre les contacts (`Contacts`) et les cas support (`Cases`). Inclut le rôle du contact dans le cas.

## Type

config

## Dépendances clés

- Variable globale `$dictionary` (framework SugarCRM).
- Protégé par la constante `sugarEntry`.

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['contacts_cases']` | variable globale PHP | Définition de la table de jointure |

### Structure de la table `contacts_cases`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `contact_id` | varchar(36) | FK vers `contacts.id` |
| `case_id` | varchar(36) | FK vers `cases.id` |
| `contact_role` | varchar(50) | Rôle du contact dans le cas |
| `date_modified` | datetime | Horodatage de modification |
| `deleted` | bool(1) | Soft delete (défaut : 0) |

### Index

| Nom | Type | Champs |
|---|---|---|
| `contacts_casespk` | primary | `id` |
| `idx_con_case_con` | index | `contact_id` |
| `idx_con_case_case` | index | `case_id` |
| `idx_contacts_cases` | alternate_key | `contact_id`, `case_id` |

### Relation

- **Type :** many-to-many
- **LHS :** module `Contacts`, table `contacts`, clé `id`
- **RHS :** module `Cases`, table `cases`, clé `id`

## Interactions

- **Appelé par :** framework SugarCRM, modules Contacts et Cases
- **Appelle :** rien

## Notes

- Champ `contact_role` : INCONNU — valeurs possibles à vérifier dans les vardefs Cases/Contacts.
