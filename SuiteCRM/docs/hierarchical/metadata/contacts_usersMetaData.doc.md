# contacts_usersMetaData.php

**Chemin :** `metadata/contacts_usersMetaData.php`
**Type :** config (métadonnées de table de jointure)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `contacts_users` qui matérialise la relation many-to-many entre les contacts (`Contacts`) et les utilisateurs internes (`Users`).

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['contacts_users']` | variable globale PHP | Définition de la table de jointure |

### Structure de la table `contacts_users`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `contact_id` | varchar(36) | FK vers `contacts.id` |
| `user_id` | varchar(36) | FK vers `users.id` |
| `date_modified` | datetime | Horodatage de modification |
| `deleted` | bool(1) | Soft delete (défaut : 0) |

### Index

| Nom | Type | Champs |
|---|---|---|
| `contacts_userspk` | primary | `id` |
| `idx_con_users_con` | index | `contact_id` |
| `idx_con_users_user` | index | `user_id` |
| `idx_contacts_users` | alternate_key | `contact_id`, `user_id` |

### Relation

- **Type :** many-to-many
- **LHS :** module `Contacts`, table `contacts`, clé `id`
- **RHS :** module `Users`, table `users`, clé `id`

## Interactions

- **Appelé par :** framework SugarCRM
- **Appelle :** rien

## Notes

- RAS.
