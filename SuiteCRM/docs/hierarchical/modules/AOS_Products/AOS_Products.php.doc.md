# Fichier AOS_Products.php

**Chemin :** `modules/AOS_Products/AOS_Products.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Modèle du catalogue de produits. Représente un produit ou service vendable avec prix, image, et lien vers une catégorie. Gère l'upload d'image produit et la conversion des montants en USD. Fournit une requête pour afficher les clients ayant acheté ce produit.

## Type
model

---

## Dépendances clés
- `AOS_Products_sugar` (classe parente générée)
- `modules/AOS_Products_Quotes/AOS_Utils.php` — `perform_aos_save()`
- `include/upload_file.php` — gestion upload
- `has_valid_image_extension()`, `verify_uploaded_image()` — validation image
- `$sugar_config['upload_maxsize']`, `$sugar_config['upload_dir']`

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `AOS_Products` | classe | Bean produit du catalogue |
| `save()` | méthode | Sauvegarde avec gestion upload image + conversion USD |
| `getGUID()` | méthode | Génère un UUID pour le préfixe du nom de fichier image |
| `getCustomersPurchasedProductsQuery()` | méthode | SQL : clients ayant acheté ce produit (via devis acceptés) |

### Champs importants
| Champ | Rôle |
|---|---|
| `product_image` | URL de l'image produit |
| `currency_id` | Devise du produit |
| `price` / `price_usdollar` | Prix et équivalent USD |
| `cost` / `cost_usdollar` | Coût et équivalent USD |

## Interactions
- **Appelé par :** Vue EditView AOS_Products, AOS_Products_Quotes (référence via `product_id`)
- **Appelle :** `perform_aos_save()`, upload_file
- **Table BD :** `aos_products`, `aos_products_quotes` (jointure dans getCustomersPurchasedProductsQuery)

## Notes
- L'upload d'image valide l'extension et le contenu (`has_valid_image_extension`, `verify_uploaded_image`).
- `getCustomersPurchasedProductsQuery()` joint `aos_products` → `aos_products_quotes` → `aos_quotes (stage='Closed Accepted')` → `accounts`.
- La suppression de l'image se fait via `$_POST['deleteAttachment'] == '1'` qui vide `product_image`.
