# 📁 AOS_Products

**Chemin :** `modules/AOS_Products/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module AOS_Products gère le catalogue de produits et services de SuiteCRM. Chaque produit définit un prix, une description, une catégorie et une image. Les produits du catalogue sont utilisés pour pré-remplir les lignes de devis et factures (AOS_Quotes, AOS_Invoices).

## ⚙️ Responsabilité technique
Bean `AOS_Products` (hérite de `AOS_Products_sugar`). Sauvegarde avec conversion de prix en USD. Méthode utilitaire `getGUID()` pour la génération d'UUID. Contrôleur MVC pour la sélection de produits depuis les formulaires de devis.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `views/` | Vue édition du produit | [→ CONTEXT](views/CONTEXT.md) |
| `Dashlets/` | Dashlet liste des produits | [→ CONTEXT](Dashlets/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues | [→ CONTEXT](metadata/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `AOS_Products.php` | Bean produit du catalogue | [→ fiche](AOS_Products.doc.md) |
| `controller.php` | Contrôleur MVC | [→ fiche](controller.doc.md) |
| `Forms.php` | Helpers de formulaire | [→ fiche](Forms.doc.md) |
| `vardefs.php` | Schéma de la table produits catalogue | [→ fiche](vardefs.php.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `AOS_Product_Categories` (relation catégorie)
- **Consommé par :** `AOS_Products_Quotes::save_lines()` (chargement des détails produit), devis/factures
- **Flux typique :** Sélection produit dans devis → `AOS_Products_Quotes::save_lines()` charge les données du produit catalogue

---

## ⚠️ Zones INCONNU
- Logique complète de `save()` non lue (conversion prix)
- Nom exact de la table DB à confirmer dans vardefs
