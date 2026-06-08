# 📁 AOS_Product_Categories

**Chemin :** `modules/AOS_Product_Categories/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module AOS_Product_Categories gère les catégories du catalogue de produits/services AOS. Il permet d'organiser les produits en catégories hiérarchiques pour faciliter la navigation et la sélection lors de la création de devis et factures.

## ⚙️ Responsabilité technique
Bean `AOS_Product_Categories` (hérite de `AOS_Product_Categories_sugar`, Module Builder). Classe de personnalisation vide. Vue édition personnalisée.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `views/` | Vue édition | [→ CONTEXT](views/CONTEXT.md) |
| `Dashlets/` | Dashlet liste des catégories | [→ CONTEXT](Dashlets/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues | [→ CONTEXT](metadata/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `AOS_Product_Categories.php` | Bean catégorie de produit | [→ fiche](AOS_Product_Categories.doc.md) |
| `vardefs.php` | Schéma de la table catégories produits | [→ fiche](vardefs.php.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consommé par :** `AOS_Products` (relation catégorie)
- **Flux typique :** Produit → associé à une catégorie → navigation par catégorie dans le catalogue

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
