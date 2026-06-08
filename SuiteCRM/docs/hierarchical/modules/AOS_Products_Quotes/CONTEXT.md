# 📁 AOS_Products_Quotes

**Chemin :** `modules/AOS_Products_Quotes/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module AOS_Products_Quotes gère les lignes de produits/services individuelles dans les devis, factures et contrats AOS. Chaque ligne représente un article avec sa quantité, son prix unitaire, sa remise et ses totaux. Ce module est aussi le fournisseur d'utilitaires partagés (`AOS_Utils`) pour la conversion de devises de tous les modules AOS.

## ⚙️ Responsabilité technique
Bean `AOS_Products_Quotes` (hérite de `AOS_Products_Quotes_sugar`). `save_lines()` gère la persistance depuis le POST. `AOS_Utils.php` fournit `perform_aos_save()` pour la conversion USD de tous les montants. `Line_Items.php` fournit des helpers de rendu des lignes.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Sous-panneaux de configuration | [→ CONTEXT](metadata/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `AOS_Products_Quotes.php` | Bean ligne de produit dans un document AOS | [→ fiche](AOS_Products_Quotes.doc.md) |
| `AOS_Utils.php` | Utilitaires partagés AOS (conversion devise, formatting) | [→ fiche](AOS_Utils.doc.md) |
| `Line_Items.php` | Helpers de rendu des lignes produit | [→ fiche](Line_Items.doc.md) |
| `vardefs.php` | Schéma de la table `aos_products_quotes` | [→ fiche](vardefs.php.doc.md) |
| `Forms.php` | Helpers de formulaire | [→ fiche](Forms.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `AOS_Products` (catalogue produits pour pré-remplissage)
- **Consommé par :** `AOS_Line_Item_Groups::save_groups()` (appelle `save_lines()`), `AOS_Quotes::mark_deleted()` (appelle `mark_lines_deleted()`)
- **`AOS_Utils.php` consommé par :** `AOS_Quotes::save()`, `AOS_Invoices::save()`, `AOS_Contracts::save()`
- **Flux typique :** Document AOS sauvegardé → `save_groups()` → `save_lines()` → persistance des lignes individuelles

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre la conversion USD des montants | [`AOS_Utils.php`](AOS_Utils.doc.md) |
| Voir la gestion des lignes produit | [`AOS_Products_Quotes.php`](AOS_Products_Quotes.doc.md) |

---

## ⚠️ Zones INCONNU
- Logique complète de `save_lines()` (formatting des montants) non lue entièrement
- `Line_Items.php` : contenu non lu
