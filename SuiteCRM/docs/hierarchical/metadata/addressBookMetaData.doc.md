# addressBookMetaData.php

**Chemin :** `metadata/addressBookMetaData.php`
**Type :** config (métadonnées de table)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table `address_book` qui stocke les entrées du carnet d'adresses personnel d'un utilisateur. Permet à un utilisateur de marquer des beans (contacts, comptes, etc.) comme favoris ou entrées de son carnet d'adresses.

## Type

config

## Dépendances clés

- Variable globale `$dictionary` (framework SugarCRM).
- Protégé par la constante `sugarEntry`.

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['AddressBook']` | variable globale PHP | Définition de la table `address_book` |

### Structure de la table `address_book`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `assigned_user_id` | id (varchar36) | FK vers l'utilisateur propriétaire (requis) |
| `bean` | varchar(50) | Nom du module/type du bean lié (requis) |
| `bean_id` | id (varchar36) | UUID du bean lié (requis) |

### Index

| Nom | Type | Champs |
|---|---|---|
| `ab_user_bean_idx` | index | `assigned_user_id`, `bean` |

## Interactions

- **Appelé par :** framework SugarCRM (dictionnaire de schéma), module carnet d'adresses
- **Appelle :** rien

## Notes

- Pas de champ `deleted` dans cette table : la suppression est vraisemblablement physique.
- Pas de clé primaire `id` déclarée explicitement (pas de champ `id` dans la liste des fields) : INCONNU si la table possède une PK ou utilise la combinaison `assigned_user_id + bean + bean_id`.
- Le champ `bean` est polymorphe : il peut référencer n'importe quel module SugarCRM (`Contacts`, `Accounts`, etc.).
- `reportable: false` sur tous les champs : ces données n'apparaissent pas dans les rapports.
