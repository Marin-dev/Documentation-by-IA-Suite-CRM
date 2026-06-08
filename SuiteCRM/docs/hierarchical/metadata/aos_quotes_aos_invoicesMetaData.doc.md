# aos_quotes_aos_invoicesMetaData.php

**Chemin :** `metadata/aos_quotes_aos_invoicesMetaData.php`
**Type :** config (métadonnées de table de jointure)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `aos_quotes_aos_invoices_c` qui matérialise la relation many-to-many entre les devis (`AOS_Quotes`) et les factures (`AOS_Invoices`). Permet de générer et lier des factures depuis un devis.

## Type

config

## Dépendances clés

- Variable globale `$dictionary` (framework SugarCRM).

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['aos_quotes_aos_invoices']` | variable globale PHP | Définition de la table de jointure |

### Structure de la table `aos_quotes_aos_invoices_c`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `date_modified` | datetime | Horodatage de modification |
| `deleted` | bool(1) | Soft delete (défaut : 0, requis) |
| `aos_quotes77d9_quotes_ida` | varchar(36) | FK vers `aos_quotes.id` |
| `aos_quotes6b83nvoices_idb` | varchar(36) | FK vers `aos_invoices.id` |

### Index

| Nom | Type | Champs |
|---|---|---|
| `aos_quotes_aos_invoicesspk` | primary | `id` |
| `aos_quotes_aos_invoices_alt` | alternate_key | `aos_quotes77d9_quotes_ida`, `aos_quotes6b83nvoices_idb` |

### Relation

- **Type :** many-to-many
- **LHS :** module `AOS_Quotes`, table `aos_quotes`, clé `id`
- **RHS :** module `AOS_Invoices`, table `aos_invoices`, clé `id`

## Interactions

- **Appelé par :** framework SugarCRM (dictionnaire de schéma), module AOS_Quotes
- **Appelle :** rien

## Notes

- Noms de colonnes avec hachage tronqué (`77d9`, `6b83`) : même pattern que `aos_quotes_aos_contracts`, généré automatiquement pour éviter les dépassements de longueur.
