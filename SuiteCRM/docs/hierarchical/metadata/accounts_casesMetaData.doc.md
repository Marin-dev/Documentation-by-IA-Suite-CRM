# accounts_casesMetaData.php

**Chemin :** `metadata/accounts_casesMetaData.php`
**Type :** config (métadonnées de table de jointure)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `accounts_cases` qui matérialise la relation entre les comptes (`Accounts`) et les cas support (`Cases`). Utilisé par le framework SugarCRM pour la gestion du schéma de base de données.

## Type

config

## Dépendances clés

- Variable globale `$dictionary` (framework SugarCRM).
- Protégé par la constante `sugarEntry`.

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['accounts_cases']` | variable globale PHP | Définition de la table de jointure |

### Structure de la table `accounts_cases`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `account_id` | varchar(36) | FK vers `accounts.id` |
| `case_id` | varchar(36) | FK vers `cases.id` |
| `date_modified` | datetime | Horodatage de modification |
| `deleted` | bool(1) | Soft delete (défaut : 0) |

### Index

| Nom | Type | Champs |
|---|---|---|
| `accounts_casespk` | primary | `id` |
| `idx_acc_case_acc` | index | `account_id` |
| `idx_acc_acc_case` | index | `case_id` |

### Relation

- **Type :** INCONNU (pas de bloc `relationships` dans ce fichier)
- **LHS :** module `Accounts`
- **RHS :** module `Cases`

## Interactions

- **Appelé par :** framework SugarCRM (dictionnaire de schéma)
- **Appelle :** rien

## Notes

- Contrairement à `accounts_bugsMetaData.php`, ce fichier ne contient pas de section `relationships`. La relation est vraisemblablement définie ailleurs (module Cases ou Accounts).
- Pas d'index `alternate_key` : l'unicité de la combinaison `account_id`/`case_id` n'est pas garantie au niveau base de données par ce fichier.
