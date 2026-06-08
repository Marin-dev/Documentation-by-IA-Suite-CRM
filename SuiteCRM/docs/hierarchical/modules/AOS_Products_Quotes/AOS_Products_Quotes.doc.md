# AOS_Products_Quotes.php

**Chemin :** `modules/AOS_Products_Quotes/AOS_Products_Quotes.php`
**Type :** PHP - Modele (Model)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Modele representant une ligne de produit/service dans un devis, une facture ou un contrat AOS. Chaque instance correspond a un article de la commande avec son prix, quantite, remise et totaux.

## Role technique
Etend `AOS_Products_Quotes_sugar`. La methode `save_lines` parse le POST pour creer/mettre a jour/supprimer les lignes de produits d'un document (devis, facture, contrat). Gere la suppression logique et la re-numerotation.

---

## Dependances / Imports
- `AOS_Products_Quotes_sugar` (classe parente generee)

## Methodes principales
| Methode | Role |
|---|---|
| `save_lines($post_data, $parent, $groups, $key)` | Sauvegarde les lignes produit depuis le POST |
| `mark_lines_deleted($parent)` | Supprime toutes les lignes d'un document (appele lors de `mark_deleted` du parent) |

**Consommateurs :**
- `AOS_Quotes->mark_deleted()` — appelle `mark_lines_deleted()`
- `AOS_Line_Item_Groups->save_groups()` — appelle `save_lines()`

## Relations cles
- **Table DB :** `aos_products_quotes`
- **Relation parent :** FK vers `aos_quotes`, `aos_invoices`, ou `aos_contracts` selon le contexte

---

## Points d'attention
- La methode `save_lines` prend en parametre `$groups` — les lignes sont organisees par groupes.
- Le `$key` est le prefixe du champ POST (ex: `product_`) — permet de traiter plusieurs tables de lignes.
- La logique complete de `save_lines` est dans la suite du fichier (limite de lecture a 60 lignes) — INCONNU pour les details de formatage des montants.
