# 📁 AOS_Quotes

**Chemin :** `modules/AOS_Quotes/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module AOS_Quotes gère les devis commerciaux dans SuiteCRM. Il supporte la numérotation automatique, les lignes de produits groupées, la conversion de devises, et les conversions vers d'autres documents (facture, contrat, opportunité). C'est le module central du cycle de vente AOS.

## ⚙️ Responsabilité technique
Bean `AOS_Quotes` (hérite de `AOS_Quotes_sugar`). Numérotation auto via `MAX+1`. Sauvegarde des groupes de lignes via `AOS_Line_Item_Groups::save_groups()` et conversion USD via `perform_aos_save()`. Scripts de conversion (`converToInvoice`, `createContract`, `createOpportunity`) créent des documents liés.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `views/` | Vues détail et édition | [→ CONTEXT](views/CONTEXT.md) |
| `Dashlets/` | Dashlet liste des devis | [→ CONTEXT](Dashlets/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues | [→ CONTEXT](metadata/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `AOS_Quotes.php` | Bean principal des devis | [→ fiche](AOS_Quotes.doc.md) |
| `converToInvoice.php` | Script de conversion devis → facture | [→ fiche](converToInvoice.doc.md) |
| `createContract.php` | Script de création contrat depuis devis | [→ fiche](createContract.doc.md) |
| `createOpportunity.php` | Script de création opportunité depuis devis | [→ fiche](createOpportunity.doc.md) |
| `controller.php` | Contrôleur MVC | [→ fiche](controller.doc.md) |
| `Forms.php` | Helpers de formulaire | [→ fiche](Forms.doc.md) |
| `vardefs.php` | Schéma de la table `aos_quotes` | [→ fiche](vardefs.php.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `AOS_Line_Item_Groups`, `AOS_Products_Quotes/AOS_Utils.php`
- **Consommé par :** `converToInvoice` (→ `AOS_Invoices`), `createContract` (→ `AOS_Contracts`), `createOpportunity` (→ `Opportunities`)
- **Flux typique :** Création devis → lignes produits → sauvegarde → conversion optionnelle en facture/contrat/opportunité

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le bean principal devis | [`AOS_Quotes.php`](AOS_Quotes.doc.md) |
| Voir la conversion devis → facture | [`converToInvoice.php`](converToInvoice.doc.md) |
| Voir la création de contrat depuis devis | [`createContract.php`](createContract.doc.md) |

---

## ⚠️ Zones INCONNU
- Risque de collision concurrente sur la numérotation (MAX+1 non atomique)
