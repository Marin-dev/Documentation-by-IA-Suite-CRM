# Fichier AOS_Product_Categories.php

**Chemin :** `modules/AOS_Product_Categories/AOS_Product_Categories.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Modèle des catégories de produits. Supporte une hiérarchie de catégories avec une catégorie parente. Empêche les cycles dans la hiérarchie (une catégorie ne peut pas être sa propre ancêtre) et vide le parent si la catégorie est marquée "is_parent".

## Type
model

---

## Dépendances clés
- `AOS_Product_Categories_sugar` (classe parente générée)
- `BeanFactory::newBean('AOS_Product_Categories')` — navigation de la hiérarchie

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `AOS_Product_Categories` | classe | Bean catégorie produit |
| `save()` | méthode | Sauvegarde avec vérification anti-cycle de hiérarchie |
| `clearParent()` | méthode (privée) | Vide les champs de catégorie parente |

### Champs importants
| Champ | Rôle |
|---|---|
| `parent_category_id` | ID de la catégorie parente |
| `is_parent` | Si vrai : catégorie racine, pas de parent |

## Interactions
- **Appelé par :** Vue EditView AOS_Product_Categories, AOS_Products (via relate field)
- **Table BD :** `aos_product_categories`

## Notes
- La détection de cycle parcourt la chaîne d'ancêtres en remontant via `parent_category_id` : si l'ID courant est rencontré, `clearParent()` est appelé.
- Pas de limite de profondeur explicite dans la vérification de cycle — boucle potentiellement longue sur de grandes hiérarchies.
