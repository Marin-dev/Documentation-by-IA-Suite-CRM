# AOS_Product_Categories.php

**Chemin :** `modules/AOS_Product_Categories/AOS_Product_Categories.php`
**Type :** PHP - Modele (Model)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Modele des categories de produits AOS. Permet d'organiser le catalogue de produits en categories hierarchiques pour faciliter la navigation et le filtrage lors de la creation de devis/factures.

## Role technique
Etend `AOS_Product_Categories_sugar` (classe generee). Structure simple sans logique metier particuliere visible — la fonctionnalite principale est dans la classe parente.

---

## Dependances / Imports
- `AOS_Product_Categories_sugar` (classe parente generee)

## Exports / Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `AOS_Product_Categories` | Classe | Modele de categorie de produit |

**Consommateurs identifies :**
- `AOS_Products` — FK vers categorie
- Interface de gestion du catalogue

## Relations cles
- **Table DB :** `aos_product_categories` (INCONNU — a verifier dans vardefs)
- **Relation :** vers `AOS_Products` (categorie parente des produits)

---

## Points d'attention
- Fichier principalement un point d'extension developer ("THIS CLASS IS FOR DEVELOPERS TO MAKE CUSTOMIZATIONS IN" probable dans la classe sugar).
- Logique metier reelle dans `AOS_Product_Categories_sugar` — non lue dans ce contexte.
