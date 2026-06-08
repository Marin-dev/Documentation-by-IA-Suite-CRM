# 📁 Audit

**Chemin :** `modules/Audit/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module Audit gère les journaux d'audit de SuiteCRM. Il enregistre les modifications apportées aux champs audités de n'importe quel bean (qui a changé quoi et quand), fournissant ainsi une traçabilité complète des modifications.

## ⚙️ Responsabilité technique
Bean `Audit` (hérite de `SugarBean`). Créé automatiquement par le framework `after_save` pour les modules avec des champs marqués `audited = true`. S'appuie sur `field_assoc.php` pour la correspondance des champs.

---

## 📂 Contenu

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `Audit.php` | Bean d'enregistrement d'audit | [→ fiche](Audit.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Appelé par :** Framework SugarBean (automatiquement sur `after_save` pour les champs audités)
- **Consomme :** `field_assoc.php`, `SugarBean`
- **Flux typique :** Sauvegarde bean avec champ audité → framework SugarBean → création enregistrement `Audit`

---

## ⚠️ Zones INCONNU
- `field_assoc.php` : contenu non lu
