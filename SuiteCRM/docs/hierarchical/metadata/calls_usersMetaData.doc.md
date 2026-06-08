# calls_usersMetaData.php

**Chemin :** `metadata/calls_usersMetaData.php`
**Type :** config (métadonnées de table de jointure)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `calls_users` qui matérialise la relation many-to-many entre les appels (`Calls`) et les utilisateurs internes (`Users`). Permet d'enregistrer quels utilisateurs ont participé à un appel et leur statut d'acceptation.

## Type

config

## Dépendances clés

- Variable globale `$dictionary` (framework SugarCRM).
- Protégé par la constante `sugarEntry`.

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['calls_users']` | variable globale PHP | Définition de la table de jointure appels-utilisateurs |

### Structure de la table `calls_users`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `call_id` | varchar(36) | FK vers `calls.id` |
| `user_id` | varchar(36) | FK vers `users.id` |
| `required` | varchar(1) | Participation requise (défaut : `1`) |
| `accept_status` | varchar(25) | Statut d'acceptation (défaut : `none`) |
| `date_modified` | datetime | Horodatage de modification |
| `deleted` | bool(1) | Soft delete (défaut : 0) |

### Index

| Nom | Type | Champs |
|---|---|---|
| `calls_userspk` | primary | `id` |
| `idx_usr_call_call` | index | `call_id` |
| `idx_usr_call_usr` | index | `user_id` |
| `idx_call_users` | alternate_key | `call_id`, `user_id` |

### Relation

- **Type :** many-to-many
- **LHS :** module `Calls`, table `calls`, clé `id`
- **RHS :** module `Users`, table `users`, clé `id`

## Interactions

- **Appelé par :** framework SugarCRM, module Calls
- **Appelle :** rien

## Notes

- Structure identique à `calls_contacts` et `calls_leads`.
- Trinité d'invités à un appel : contacts externes, prospects, utilisateurs internes.
