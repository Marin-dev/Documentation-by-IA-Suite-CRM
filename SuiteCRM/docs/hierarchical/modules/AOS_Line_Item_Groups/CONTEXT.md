# 📁 AOS_Line_Item_Groups

**Chemin :** `modules/AOS_Line_Item_Groups/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module AOS_Line_Item_Groups gère les groupes de lignes de produits/services dans les devis, factures et contrats AOS. Chaque groupe permet de regrouper des lignes avec un sous-total (ex : "Matériel", "Services") et un titre personnalisable.

## ⚙️ Responsabilité technique
Bean `AOS_Line_Item_Groups` (hérite de `AOS_Line_Item_Groups_sugar`). La méthode `save_groups()` orchestre depuis le POST la création/mise à jour des groupes et leurs lignes enfants (`AOS_Products_Quotes::save_lines()`). Gère l'héritage du `assigned_user_id` du document parent.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `AOS_Line_Item_Groups.php` | Bean groupe de lignes avec méthode `save_groups()` | [→ fiche](AOS_Line_Item_Groups.doc.md) |
| `vardefs.php` | Schéma de la table `aos_line_item_groups` | [→ fiche](vardefs.php.doc.md) |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `AOS_Line_Item_Groups_sugar.php` | Classe générée automatiquement |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `AOS_Products_Quotes` (lignes enfants)
- **Consommé par :** `AOS_Quotes::save()`, `AOS_Invoices::save()`, `AOS_Contracts::save()`
- **Flux typique :** Save devis/facture → `AOS_Line_Item_Groups::save_groups($post, $parent)` → pour chaque groupe → `AOS_Products_Quotes::save_lines()`

---

## ⚠️ Zones INCONNU
- Gestion de devise parent : logique complète non lue (limite de lecture atteinte)
