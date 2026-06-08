# AOS_Quotes.php

**Chemin :** `modules/AOS_Quotes/AOS_Quotes.php`
**Type :** PHP - Modele (Model)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Modele principal des devis commerciaux (Quotes) dans le module AOS. Gere la creation, sauvegarde et suppression des devis avec leur numerotation automatique et leurs lignes de produits groupees.

## Role technique
Etend `AOS_Quotes_sugar` (classe generee). La methode `save` attribue un numero de devis auto-incremente (initialisable via config), execute la conversion des montants en USD (`perform_aos_save`), et sauvegarde les groupes de lignes de produits. Supporte MySQL et MSSQL pour le calcul du numero.

---

## Dependances / Imports
- `AOS_Quotes_sugar` (classe parente generee)
- `modules/AOS_Products_Quotes/AOS_Utils.php` — `perform_aos_save()`
- `modules/AOS_Line_Item_Groups/AOS_Line_Item_Groups.php` — `save_groups()`

## Exports / Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `AOS_Quotes` | Classe | Modele de devis |
| `save($check_notify)` | Methode | Sauvegarde devis + numero auto + groupes de lignes |
| `mark_deleted($id)` | Methode | Supprime le devis et ses lignes produit |

**Consommateurs identifies :**
- `modules/AOS_Quotes/converToInvoice.php` — conversion devis en facture
- `modules/AOS_Quotes/createContract.php` — creation contrat depuis devis
- `modules/AOS_Quotes/createOpportunity.php` — creation opportunite depuis devis

## Relations cles
- **Table DB :** `aos_quotes`
- **Config :** `$sugar_config['aos']['quotes']['initialNumber']` — numero initial des devis
- **Appelle :** `AOS_Products_Quotes->mark_lines_deleted()`, `AOS_Line_Item_Groups->save_groups()`

---

## Points d'attention
- Le numero de devis est calcule via `MAX(CAST(number as UNSIGNED))+1` — risque de collision en cas d'acces concurrent.
- La conversion de montants USD est faite avant `parent::save()` via `perform_aos_save()`.
- Lors d'une duplication (`duplicateSave = true`), les IDs des groupes et produits sont nettoyes du POST.
