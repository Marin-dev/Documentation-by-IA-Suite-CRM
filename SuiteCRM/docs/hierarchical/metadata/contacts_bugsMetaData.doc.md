# contacts_bugsMetaData.php

**Chemin :** `metadata/contacts_bugsMetaData.php`
**Type :** config (métadonnées de table de jointure)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `contacts_bugs` qui matérialise la relation many-to-many entre les contacts (`Contacts`) et les bogues (`Bugs`). Inclut le rôle du contact vis-à-vis du bogue.

## Type

config

## Dépendances clés

- Variable globale `$dictionary` (framework SugarCRM).
- Protégé par la constante `sugarEntry`.

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['contacts_bugs']` | variable globale PHP | Définition de la table de jointure |

### Structure de la table `contacts_bugs`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `contact_id` | varchar(36) | FK vers `contacts.id` |
| `bug_id` | varchar(36) | FK vers `bugs.id` |
| `contact_role` | varchar(50) | Rôle du contact pour ce bogue |
| `date_modified` | datetime | Horodatage de modification |
| `deleted` | bool(1) | Soft delete (défaut : 0) |

### Index

| Nom | Type | Champs |
|---|---|---|
| `contacts_bugspk` | primary | `id` |
| `idx_con_bug_con` | index | `contact_id` |
| `idx_con_bug_bug` | index | `bug_id` |
| `idx_contact_bug` | alternate_key | `contact_id`, `bug_id` |

### Relation

- **Type :** many-to-many
- **LHS :** module `Contacts`, table `contacts`, clé `id`
- **RHS :** module `Bugs`, table `bugs`, clé `id`

## Interactions

- **Appelé par :** framework SugarCRM, modules Contacts et Bugs
- **Appelle :** rien

## Notes

- Champ `contact_role` : INCONNU — valeurs possibles non définies dans ce fichier (à chercher dans les vardefs du module Bugs).
