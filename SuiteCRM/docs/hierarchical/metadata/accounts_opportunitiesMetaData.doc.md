# accounts_opportunitiesMetaData.php

**Chemin :** `metadata/accounts_opportunitiesMetaData.php`
**Type :** config (métadonnées de table de jointure)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `accounts_opportunities` qui matérialise la relation many-to-many entre les comptes (`Accounts`) et les opportunités commerciales (`Opportunities`).

## Type

config

## Dépendances clés

- Variable globale `$dictionary` (framework SugarCRM).
- Protégé par la constante `sugarEntry`.

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['accounts_opportunities']` | variable globale PHP | Définition de la table et de la relation |

### Structure de la table `accounts_opportunities`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `opportunity_id` | varchar(36) | FK vers `opportunities.id` |
| `account_id` | varchar(36) | FK vers `accounts.id` |
| `date_modified` | datetime | Horodatage de modification |
| `deleted` | bool(1) | Soft delete (défaut : 0) |

### Index

| Nom | Type | Champs |
|---|---|---|
| `accounts_opportunitiespk` | primary | `id` |
| `idx_account_opportunity` | alternate_key | `account_id`, `opportunity_id` |
| `idx_oppid_del_accid` | index | `opportunity_id`, `deleted`, `account_id` |

### Relation

- **Type :** many-to-many
- **LHS :** module `Accounts`, table `accounts`, clé `id`
- **RHS :** module `Opportunities`, table `opportunities`, clé `id`
- **Table de jointure :** `accounts_opportunities`

## Interactions

- **Appelé par :** framework SugarCRM (dictionnaire de schéma)
- **Appelle :** rien

## Notes

- Index composite `(opportunity_id, deleted, account_id)` optimise les requêtes cherchant toutes les opportunités non supprimées d'un compte.
