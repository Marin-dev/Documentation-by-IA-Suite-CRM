# 📁 jjwg_Markers

**Chemin :** `modules/jjwg_Markers/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module jjwg_Markers gère les marqueurs personnalisés de la carte JJWG Maps. Les marqueurs représentent des points d'intérêt ou des icônes personnalisées utilisées pour afficher les enregistrements CRM sur la carte.

## ⚙️ Responsabilité technique
Bean `jjwg_Markers` (hérite de `jjwg_Markers_sugar`). Vues spécialisées avec carte pour la définition de la position des marqueurs.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `views/` | Vues carte détail et édition des marqueurs | [→ CONTEXT](views/CONTEXT.md) |
| `Dashlets/` | Dashlet liste des marqueurs | [→ CONTEXT](Dashlets/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues | [→ CONTEXT](metadata/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `jjwg_Markers.php` | Bean marqueur de carte | [→ fiche](jjwg_Markers.php.doc.md) |
| `controller.php` | Contrôleur MVC | [→ fiche](controller.php.doc.md) |
| `vardefs.php` | Schéma de la table des marqueurs | [→ fiche](vardefs.php.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.php.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consommé par :** `jjwg_Maps` (marqueurs affichés sur la carte)

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
