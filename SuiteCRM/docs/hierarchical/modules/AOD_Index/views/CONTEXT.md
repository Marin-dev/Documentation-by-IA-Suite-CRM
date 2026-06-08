# 📁 views

**Chemin :** `modules/AOD_Index/views/`
**Profondeur :** 4
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Contient les vues du module AOD_Index. Fournit l'affichage des statistiques de l'index Lucene (modules indexables, état, etc.).

## ⚙️ Responsabilité technique
Vue PHP héritant de `SugarView`, peuplée par le contrôleur `AOD_IndexController`. Module déprécié depuis v7.12.0.

---

## 📂 Contenu

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `view.indexdata.php` | Vue des statistiques et données de l'index Lucene | [→ fiche](view.indexdata.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Appelé par :** `AOD_IndexController::action_indexdata()`
- **Consomme :** `AOD_Index::getIndexableModules()`

---

## ⚠️ Zones INCONNU
Module déprécié depuis v7.12.0.
