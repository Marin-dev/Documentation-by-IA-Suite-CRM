# AOS_Invoices.php

**Chemin :** `modules/AOS_Invoices/AOS_Invoices.php`
**Type :** PHP - Modele (Model)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Modele principal des factures (Invoices) dans le module AOS. Gere la creation, numerotation automatique et sauvegarde des factures avec leurs lignes de produits groupees. Structurellement identique a `AOS_Quotes` mais pour les factures.

## Role technique
Etend `AOS_Invoices_sugar` (classe generee). Meme pattern que `AOS_Quotes` : numero auto-incremente, conversion USD, sauvegarde des groupes de lignes. Supporte MySQL et MSSQL.

---

## Dependances / Imports
- `AOS_Invoices_sugar` (classe parente generee)
- `modules/AOS_Products_Quotes/AOS_Utils.php` — `perform_aos_save()`
- `modules/AOS_Line_Item_Groups/AOS_Line_Item_Groups.php` — `save_groups()`

## Exports / Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `AOS_Invoices` | Classe | Modele de facture |
| `save($check_notify)` | Methode | Sauvegarde facture + numero auto + groupes de lignes |
| `mark_deleted($id)` | Methode | Supprime la facture et ses lignes (via classe parente) |

## Relations cles
- **Table DB :** `aos_invoices`
- **Config :** `$sugar_config['aos']['invoices']['initialNumber']` — numero initial
- **Appelle :** `AOS_Line_Item_Groups->save_groups()`

---

## Points d'attention
- Le numero de facture utilise la meme logique que les devis (MAX+1) — meme risque de collision concurrente.
- Commentaire en tete : "THIS CLASS IS FOR DEVELOPERS TO MAKE CUSTOMIZATIONS IN" — c'est le point d'extension prevu.
