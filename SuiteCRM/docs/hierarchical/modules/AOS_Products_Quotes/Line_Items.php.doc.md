# Fichier Line_Items.php

**Chemin :** `modules/AOS_Products_Quotes/Line_Items.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Bibliothèque de rendu des lignes de commande pour les vues EditView et DetailView des modules AOS (Quotes, Invoices, Contracts). Génère le HTML du tableau de lignes produits/services avec groupes, totaux, remises, TVA.

## Type
helper / vue

---

## Dépendances clés
- `modules/AOS_Products_Quotes/AOS_Products_Quotes.php`
- `modules/AOS_Line_Item_Groups/AOS_Line_Item_Groups.php`
- `$sugar_config['aos']['lineItems']['enableGroups']` — activation des groupes
- `$sugar_config['aos']['lineItems']['totalTax']` — affichage taxe totale
- `$locale->getPrecision()` — précision numérique
- JavaScript `line_items.js` (EditView) — calcul côté client
- `BeanFactory`

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `display_lines()` | fonction | Génère le HTML du tableau de lignes (EditView : JS/canvas, DetailView : tableau HTML statique) |
| `display_shipping_vat()` | fonction | Génère le champ de TVA sur frais de port (EditView : input, DetailView : valeur formatée) |
| `display_tax_detail_view()` | fonction | Formate un taux de TVA en pourcentage pour la DetailView |
| `stripDecimalPointsAndTrailingZeroes()` | fonction | Supprime les zéros décimaux superflus dans l'affichage des quantités |
| `get_discount_string()` | fonction | Formate la remise (montant ou pourcentage) |

## Interactions
- **Appelé par :** Vues EditView/DetailView de AOS_Quotes, AOS_Invoices, AOS_Contracts (via vardefs function fields)
- **Appelle :** `BeanFactory::newBean('AOS_Products_Quotes')`, `BeanFactory::newBean('AOS_Line_Item_Groups')`

## Notes
- En EditView, le rendu repose sur du JavaScript (`insertLineItems()`, `insertGroup()`) qui récupère les données en JSON.
- `$enable_groups` peut désactiver l'affichage des groupes de lignes (config `aos.lineItems.enableGroups`).
- La requête SQL de chargement joint `aos_products_quotes` et `aos_line_item_groups` triés par numéro de groupe puis numéro de ligne.
