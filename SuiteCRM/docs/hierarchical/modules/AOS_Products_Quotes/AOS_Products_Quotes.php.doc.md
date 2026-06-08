# Fichier AOS_Products_Quotes.php

**Chemin :** `modules/AOS_Products_Quotes/AOS_Products_Quotes.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Modèle d'une ligne de produit ou de service dans un devis, une facture ou un contrat. Représente chaque article individuel avec quantité, prix unitaire, remise, TVA et prix total. Gère la sauvegarde en masse et la suppression en cascade des lignes.

## Type
model

---

## Dépendances clés
- `AOS_Products_Quotes_sugar` (classe parente générée)
- `modules/AOS_Products_Quotes/AOS_Utils.php` — `perform_aos_save()` (conversion USD)
- `BeanFactory`

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `AOS_Products_Quotes` | classe | Bean ligne de produit/service |
| `save_lines()` | méthode | Sauvegarde les lignes depuis POST (produits et services) |
| `save()` | méthode | Sauvegarde avec conversion devise USD |
| `mark_lines_deleted()` | méthode | Supprime toutes les lignes liées à un parent (devis/facture/contrat) |

### Champs importants
| Champ | Rôle |
|---|---|
| `parent_id` | ID du parent (devis, facture, contrat) |
| `parent_type` | Type du parent (AOS_Quotes, AOS_Invoices, AOS_Contracts) |
| `group_id` | ID du groupe de lignes (AOS_Line_Item_Groups) |
| `product_id` | ID du produit catalogue (null = service) |
| `product_qty` | Quantité |
| `product_unit_price` | Prix unitaire |
| `product_list_price` | Prix catalogue |
| `product_discount` | Montant de remise |
| `discount` | Type de remise (Amount / Percentage) |
| `vat` | Taux de TVA |
| `vat_amt` | Montant TVA calculé |
| `product_total_price` | Prix total de la ligne |
| `currency_id` | Devise (héritée du parent) |

## Interactions
- **Appelé par :** `AOS_Line_Item_Groups::save_groups()`, `AOS_Invoices::mark_deleted()`, `AOS_Quotes::mark_deleted()`, `AOS_Contracts::mark_deleted()`
- **Table BD :** `aos_products_quotes`

## Notes
- Une ligne n'est sauvegardée que si `product_id`, `name` et `product_unit_price` sont non vides (ligne 95).
- `currency_id` est héritée du parent au moment de la sauvegarde.
- La distinction produit/service se fait par `product_id` : null ou '0' = service.
