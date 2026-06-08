# user_feedsMetaData.php

**Chemin :** `metadata/user_feedsMetaData.php`
**Type :** config (metadonnees de table de relation)
**Derniere mise a jour doc :** 2026-05-31

---

## Role

Definit la structure de la table `users_feeds` qui associe des utilisateurs (`Users`) a des flux d'activite (`feeds`). Permet de stocker les abonnements des utilisateurs a des fils d'activite dans le CRM.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['users_feeds']` | variable globale PHP | Definition de la table de relation |

### Structure de la table `users_feeds`

| Colonne | Type SQL | Role |
|---|---|---|
| `user_id` | varchar(36) | FK vers `users.id` |
| `feed_id` | varchar(36) | FK vers la table feeds (INCONNU : pas de FK explicite) |
| `rank` | int | Ordre d'affichage du feed (nullable) |
| `date_modified` | datetime | Horodatage de modification |
| `deleted` | bool | Soft delete (defaut : 0, nullable) |

### Index

| Nom | Type | Champs |
|---|---|---|
| `idx_ud_user_id` | index | `user_id`, `feed_id` |

### Relation

- Pas de bloc `relationships` explicite dans ce fichier.
- La table n'a pas de cle primaire `id` definie : la cle est impliquee par la combinaison `user_id`/`feed_id`.

## Interactions

- **Appele par :** framework SugarCRM (dictionnaire de schema)
- **Appelle :** rien

## Notes

- Absence de cle primaire `id` : inhabituel par rapport aux autres tables MetaData. Cela peut indiquer une table legacy ou une gestion differente de l'unicite.
- La table des feeds (`feed_id`) n'est pas definie dans ce dossier `metadata/` ; son module source est INCONNU.
- Protege par la constante `sugarEntry`.
