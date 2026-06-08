# 📁 views

**Chemin :** `modules/AOK_KnowledgeBase/views/`
**Profondeur :** 4
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Contient les vues personnalisées du module Base de Connaissances. Gère le décodage HTML du contenu des articles pour un rendu correct.

## ⚙️ Responsabilité technique
Vues PHP héritant des classes SuiteCRM (`ViewDetail`, `ViewEdit`). Surcharges pour traiter le contenu HTML des articles.

---

## 📂 Contenu

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `view.detail.php` | Vue détail d'un article KB avec décodage HTML | [→ fiche](view.detail.doc.md) |
| `view.edit.php` | Vue édition d'un article KB | [→ fiche](view.edit.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Appelé par :** Framework MVC SuiteCRM (actions DetailView, EditView du module)
- **Consomme :** Bean `AOK_KnowledgeBase`, champ `description`

---

## ⚠️ Zones INCONNU
- `view.edit.php` : contenu non lu
