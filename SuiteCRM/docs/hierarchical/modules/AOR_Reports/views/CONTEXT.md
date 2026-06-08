# 📁 views

**Chemin :** `modules/AOR_Reports/views/`
**Profondeur :** 4
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Contient les vues personnalisées du module AOR_Reports : affichage et édition des rapports avec rendu des résultats, graphiques et options d'export.

## ⚙️ Responsabilité technique
Vues PHP héritant de `ViewDetail` et `ViewEdit`. La vue détail intègre le rendu des résultats, graphiques, totaux et options CSV/PDF.

---

## 📂 Contenu

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `view.detail.php` | Vue détail avec affichage des résultats et graphiques | [→ fiche](view.detail.doc.md) |
| `view.edit.php` | Vue édition avec configuration des champs et conditions | [→ fiche](view.edit.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `AOR_Report::build_report_html()`, `build_report_chart()`, `build_report_csv()`
- **Appelé par :** Framework MVC SuiteCRM (actions DetailView, EditView)

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
