# meetings_usersMetaData.php

**Chemin :** `metadata/meetings_usersMetaData.php`
**Type :** config (métadonnées de table de jointure)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `meetings_users` qui matérialise la relation many-to-many entre les réunions (`Meetings`) et les utilisateurs internes (`Users`). Inclut le statut de participation et d'acceptation.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['meetings_users']` | variable globale PHP | Définition de la table de jointure |

### Structure de la table `meetings_users`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `meeting_id` | varchar(36) | FK vers `meetings.id` |
| `user_id` | varchar(36) | FK vers `users.id` |
| `required` | varchar(1) | Participation requise (défaut : `1`) |
| `accept_status` | varchar(25) | Statut d'acceptation (défaut : `none`) |
| `date_modified` | datetime | Horodatage |
| `deleted` | bool(1) | Soft delete (défaut : 0) |

### Relation

- **Type :** many-to-many
- **LHS :** module `Meetings`, table `meetings`, clé `id`
- **RHS :** module `Users`, table `users`, clé `id`

## Notes

- RAS. Pattern identique à `meetings_contacts` et `meetings_leads`.
