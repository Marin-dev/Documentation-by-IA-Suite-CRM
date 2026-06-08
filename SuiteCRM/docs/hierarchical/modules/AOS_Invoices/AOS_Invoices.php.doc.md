# Fichier AOS_Invoices.php

**Chemin :** `modules/AOS_Invoices/AOS_Invoices.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Modèle du module Factures (AOS_Invoices). Gère la création et la sauvegarde de factures commerciales avec numérotation automatique séquentielle, lignes de produits/services et groupes de lignes. Hérite de AOS_Invoices_sugar.

## Type
model

---

## Dépendances clés
- `AOS_Invoices_sugar` (classe parente générée)
- `modules/AOS_Products_Quotes/AOS_Utils.php` — `perform_aos_save()` (conversion devises USD)
- `modules/AOS_Line_Item_Groups/AOS_Line_Item_Groups.php` — sauvegarde groupes de lignes
- `modules/AOS_Products_Quotes/AOS_Products_Quotes.php` — suppression des lignes
- `$sugar_config['aos']['invoices']['initialNumber']` — numéro de facture initial
- `$sugar_config['dbconfig']['db_type']` — gestion MSSQL vs MySQL pour le MAX

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `AOS_Invoices` | classe | Bean facture |
| `save()` | méthode | Sauvegarde facture avec auto-incrément du numéro + groupes lignes |
| `mark_deleted()` | méthode | Supprime la facture + toutes les lignes produits associées |

## Interactions
- **Appelé par :** Vue EditView AOS_Invoices, `AOS_Quotes::converToInvoice.php`
- **Appelle :** `perform_aos_save()`, `AOS_Line_Item_Groups::save_groups()`, `AOS_Products_Quotes::mark_lines_deleted()`
- **Table BD :** `aos_invoices`, `aos_line_item_groups`, `aos_products_quotes`

## Notes
- Le numéro de facture est calculé par `MAX(CAST(number AS UNSIGNED))+1` — compatible MSSQL avec `CAST(number AS INT)`.
- Si le numéro calculé est inférieur à `initialNumber` (config), c'est `initialNumber` qui est utilisé.
- Le numérotage n'est initialisé que lors de la création (id vide) ou duplication.
