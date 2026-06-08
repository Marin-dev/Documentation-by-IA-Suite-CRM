# 📁 AOS_Invoices

**Chemin :** `modules/AOS_Invoices/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module AOS_Invoices gère les factures commerciales dans SuiteCRM. Il supporte la numérotation automatique incrémentale, la gestion de lignes de produits groupées, la conversion de devises et l'export PDF. Structurellement identique à AOS_Quotes mais pour les factures.

## ⚙️ Responsabilité technique
Bean `AOS_Invoices` (hérite de `AOS_Invoices_sugar`). Numérotation auto via `MAX+1` sur la table. Sauvegarde des groupes de lignes via `AOS_Line_Item_Groups::save_groups()` et `perform_aos_save()`. Supporte MySQL et MSSQL.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `views/` | Vues détail et édition | [→ CONTEXT](views/CONTEXT.md) |
| `Dashlets/` | Dashlet liste des factures | [→ CONTEXT](Dashlets/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues | [→ CONTEXT](metadata/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `AOS_Invoices.php` | Bean principal des factures | [→ fiche](AOS_Invoices.doc.md) |
| `controller.php` | Contrôleur MVC | [→ fiche](controller.doc.md) |
| `Forms.php` | Helpers de formulaire | [→ fiche](Forms.doc.md) |
| `vardefs.php` | Schéma de la table `aos_invoices` | [→ fiche](vardefs.php.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `AOS_Line_Item_Groups`, `AOS_Products_Quotes/AOS_Utils.php`
- **Consommé par :** Module Quotes (conversion devis → facture), module Accounts/Contacts
- **Flux typique :** Création facture → numérotation auto → `save_groups()` → `perform_aos_save()`

---

## ⚠️ Zones INCONNU
- Risque de collision concurrente sur la numérotation (MAX+1 non atomique)
