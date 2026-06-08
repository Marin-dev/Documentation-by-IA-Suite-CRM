# users_last_importMetaData.php

**Chemin :** `metadata/users_last_importMetaData.php`
**Type :** config (metadonnees de table)
**Derniere mise a jour doc :** 2026-05-31

---

## Role

Definit la structure de la table `users_last_import` qui enregistre le dernier import effectue par chaque utilisateur. Utilise par le systeme d'import de donnees pour tracer les historiques d'importation par utilisateur et par type de bean.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['users_last_import']` | variable globale PHP | Definition de la table de traçage des imports |

### Structure de la table `users_last_import`

| Colonne | Type SQL | Role |
|---|---|---|
| `id` | varchar(36) | Cle primaire UUID |
| `assigned_user_id` | varchar(36) | FK vers `users.id` — utilisateur ayant effectue l'import |
| `bean_type` | varchar(36) | Type de module importe (ex. : Contacts, Leads) |
| `bean_id` | varchar(36) | ID du dernier bean importe |
| `date_modified` | datetime | Horodatage de modification |
| `deleted` | bool | Soft delete (nullable) |

### Index

| Nom | Type | Champs |
|---|---|---|
| `users_last_importpk` | primary | `id` |
| `idx_user_id` | index | `assigned_user_id` |

### Relation

- Pas de bloc `relationships` explicite dans ce fichier.

## Interactions

- **Appele par :** framework SugarCRM (dictionnaire de schema), module Import
- **Appelle :** rien

## Notes

- Protege par la constante `sugarEntry`.
- Utile pour reprendre un import interrompu ou identifier le dernier enregistrement importe par un utilisateur.
