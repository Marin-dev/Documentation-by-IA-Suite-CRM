# AOS_Products.php

**Chemin :** `modules/AOS_Products/AOS_Products.php`
**Type :** PHP - Modele (Model)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Modele du catalogue de produits/services AOS. Represente un article du catalogue avec son prix, sa description, sa categorie et son image. Utilise pour pre-remplir les lignes de devis/factures.

## Role technique
Etend `AOS_Products_sugar`. La methode `save` gere la sauvegarde avec la conversion des prix en USD. Contient une methode utilitaire `getGUID` pour la generation d'UUID (compatible PHP < 5.3).

---

## Dependances / Imports
- `AOS_Products_sugar` (classe parente generee)
- `$sugar_config`, `$mod_strings` (globals SugarCRM)

## Methodes principales
| Methode | Role |
|---|---|
| `save($check_notify)` | Sauvegarde le produit (logique complete INCONNU — suite non lue) |
| `getGUID()` | Genere un UUID compatible (fallback sur md5/uniqid si `com_create_guid` absent) |

**Consommateurs :**
- Interface de catalogue produits
- `AOS_Products_Quotes->save_lines()` — chargement des details produit lors de l'ajout a un devis

## Relations cles
- **Table DB :** `aos_products_catalog` (INCONNU — nom de table a verifier dans vardefs)
- **Relation :** vers `AOS_Product_Categories`

---

## Points d'attention
- `getGUID` utilise une implementation manuelle si `com_create_guid` est absent — peut generer des UUID de qualite moindre.
- La logique complete de `save()` est dans la suite du fichier (limite de lecture) — INCONNU pour les details de conversion prix.
