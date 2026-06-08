# accounts_bugsMetaData.php

**Chemin :** `metadata/accounts_bugsMetaData.php`
**Type :** config (métadonnées de table de jointure)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `accounts_bugs` qui matérialise la relation many-to-many entre les comptes (`Accounts`) et les bogues (`Bugs`) dans SuiteCRM. Ce fichier est utilisé par le framework SugarCRM pour créer ou mettre à jour la table en base de données.

## Type

config

## Dépendances clés

- Aucun import PHP explicite. Alimenté par le framework SugarCRM via la variable globale `$dictionary`.
- Protégé par la constante `sugarEntry` (sécurité point d'entrée SugarCRM).

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['accounts_bugs']` | variable globale PHP | Définition complète de la table de jointure et de la relation |

### Structure de la table `accounts_bugs`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `account_id` | varchar(36) | FK vers `accounts.id` |
| `bug_id` | varchar(36) | FK vers `bugs.id` |
| `date_modified` | datetime | Horodatage de modification |
| `deleted` | bool(1) | Soft delete (défaut : 0) |

### Index

| Nom | Type | Champs |
|---|---|---|
| `accounts_bugspk` | primary | `id` |
| `idx_acc_bug_acc` | index | `account_id` |
| `idx_acc_bug_bug` | index | `bug_id` |
| `idx_account_bug` | alternate_key | `account_id`, `bug_id` |

### Relation

- **Type :** many-to-many
- **LHS :** module `Accounts`, table `accounts`, clé `id`
- **RHS :** module `Bugs`, table `bugs`, clé `id`
- **Table de jointure :** `accounts_bugs`

## Interactions

- **Appelé par :** framework SugarCRM (chargement du dictionnaire de schéma, outil Repair/Rebuild)
- **Appelle :** rien directement

## Notes

- Pattern standard SugarCRM : tous les fichiers `*MetaData.php` dans ce dossier suivent le même patron.
- Le champ `deleted` permet la suppression logique (soft delete) sans suppression physique de la ligne.
- L'index `alternate_key` sur `(account_id, bug_id)` garantit l'unicité du doublon.
