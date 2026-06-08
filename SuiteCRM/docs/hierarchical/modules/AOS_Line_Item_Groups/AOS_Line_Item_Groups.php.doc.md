# Fichier AOS_Line_Item_Groups.php

**Chemin :** `modules/AOS_Line_Item_Groups/AOS_Line_Item_Groups.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Modèle des groupes de lignes pour les devis, factures et contrats AOS. Un groupe permet d'organiser les lignes de produits/services en sections distinctes avec leurs propres totaux (total_amt, discount_amount, subtotal_amount, tax_amount, total_amount). Orchestre la sauvegarde de l'ensemble lignes + groupes.

## Type
model

---

## Dépendances clés
- `AOS_Line_Item_Groups_sugar` (classe parente générée)
- `modules/AOS_Products_Quotes/AOS_Utils.php` — `perform_aos_save()`
- `modules/AOS_Products_Quotes/AOS_Products_Quotes.php` — sauvegarde des lignes produits/services
- `BeanFactory`

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `AOS_Line_Item_Groups` | classe | Bean groupe de lignes |
| `save_groups()` | méthode | Sauvegarde les groupes et leurs lignes (produits + services) depuis POST |
| `save()` | méthode | Sauvegarde avec conversion USD via `perform_aos_save()` |

### Champs importants
| Champ | Rôle |
|---|---|
| `parent_id` | ID du parent (devis/facture/contrat) |
| `parent_type` | Type du parent |
| `number` | Ordre du groupe |
| `total_amt` | Total avant remise du groupe |
| `discount_amount` | Remise totale du groupe |
| `subtotal_amount` | Sous-total après remise |
| `tax_amount` | Total TVA du groupe |
| `total_amount` | Grand total du groupe |

## Interactions
- **Appelé par :** `AOS_Contracts::save()`, `AOS_Invoices::save()`, `AOS_Quotes::save()`
- **Appelle :** `AOS_Products_Quotes::save_lines()` (pour produits ET services)
- **Table BD :** `aos_line_item_groups`

## Notes
- `save_groups()` orchestre toute la chaîne de sauvegarde des lignes : 1) groupes, 2) lignes produits (key='product_'), 3) lignes services (key='service_').
- L'ID du groupe est injecté dans `$_POST` (`$post_data[$key.'id'][$i]`) pour être récupéré par les lignes produits.
- Un groupe supprimé (`deleted=1`) n'appelle pas la suppression des lignes produits — potentiel orphelins (à surveiller).
