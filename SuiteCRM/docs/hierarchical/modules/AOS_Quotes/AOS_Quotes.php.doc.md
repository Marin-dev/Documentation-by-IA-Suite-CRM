# Fichier AOS_Quotes.php

**Chemin :** `modules/AOS_Quotes/AOS_Quotes.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Modèle du module Devis (AOS_Quotes). Gère la création et la sauvegarde de devis avec numérotation automatique séquentielle, lignes de produits/services et groupes de lignes. Point de départ du flux commercial : un devis peut être converti en facture, en contrat ou en opportunité.

## Type
model

---

## Dépendances clés
- `AOS_Quotes_sugar` (classe parente générée)
- `modules/AOS_Products_Quotes/AOS_Utils.php` — `perform_aos_save()` (conversion devises)
- `modules/AOS_Line_Item_Groups/AOS_Line_Item_Groups.php` — sauvegarde groupes de lignes
- `modules/AOS_Products_Quotes/AOS_Products_Quotes.php` — suppression lignes
- `$sugar_config['aos']['quotes']['initialNumber']` — numéro initial des devis

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `AOS_Quotes` | classe | Bean devis |
| `save()` | méthode | Sauvegarde devis avec auto-incrément numéro + groupes lignes |
| `mark_deleted()` | méthode | Supprime le devis + toutes les lignes produits |

## Interactions
- **Appelé par :** Vue EditView AOS_Quotes
- **Fichiers de conversion :** `converToInvoice.php`, `createContract.php`, `createOpportunity.php` (dans le même module)
- **Appelle :** `perform_aos_save()`, `AOS_Line_Item_Groups::save_groups()`, `AOS_Products_Quotes::mark_lines_deleted()`
- **Table BD :** `aos_quotes`, `aos_line_item_groups`, `aos_products_quotes`

## Notes
- Même pattern que AOS_Invoices pour la numérotation.
- La conversion en facture/contrat/opportunité est gérée par des scripts séparés dans le même dossier (converToInvoice.php, createContract.php, createOpportunity.php).
