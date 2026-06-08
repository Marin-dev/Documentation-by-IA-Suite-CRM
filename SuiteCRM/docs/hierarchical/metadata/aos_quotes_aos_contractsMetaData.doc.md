# aos_quotes_aos_contractsMetaData.php

**Chemin :** `metadata/aos_quotes_aos_contractsMetaData.php`
**Type :** config (métadonnées de table de jointure)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `aos_quotes_os_contracts_c` qui matérialise la relation many-to-many entre les devis (`AOS_Quotes`) et les contrats (`AOS_Contracts`). Permet de lier un devis à un ou plusieurs contrats.

## Type

config

## Dépendances clés

- Variable globale `$dictionary` (framework SugarCRM).

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['aos_quotes_aos_contracts']` | variable globale PHP | Définition de la table de jointure |

### Structure de la table `aos_quotes_os_contracts_c`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `date_modified` | datetime | Horodatage de modification |
| `deleted` | bool(1) | Soft delete (défaut : 0, requis) |
| `aos_quotese81e_quotes_ida` | varchar(36) | FK vers `aos_quotes.id` |
| `aos_quotes4dc0ntracts_idb` | varchar(36) | FK vers `aos_contracts.id` |

### Index

| Nom | Type | Champs |
|---|---|---|
| `aos_quotes_aos_contractsspk` | primary | `id` |
| `aos_quotes_aos_contracts_alt` | alternate_key | `aos_quotese81e_quotes_ida`, `aos_quotes4dc0ntracts_idb` |

### Relation

- **Type :** many-to-many
- **LHS :** module `AOS_Quotes`, table `aos_quotes`, clé `id`
- **RHS :** module `AOS_Contracts`, table `aos_contracts`, clé `id`

## Interactions

- **Appelé par :** framework SugarCRM (dictionnaire de schéma)
- **Appelle :** rien

## Notes

- Noms de colonnes de jointure tronqués et avec hachage (`e81e`, `4dc0`) : typique des relations générées par Studio quand les noms dépassent la longueur maximale autorisée.
- Nom de table de jointure `aos_quotes_os_contracts_c` (tronqué : `a` manquant dans `aos`) : anomalie de génération à surveiller.
