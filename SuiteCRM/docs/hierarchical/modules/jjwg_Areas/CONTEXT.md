# 📁 jjwg_Areas

**Chemin :** `modules/jjwg_Areas/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module jjwg_Areas gère les zones géographiques définies dans le sous-système JJWG Maps. Les zones sont des polygones géographiques (régions commerciales, zones de service) utilisées pour les analyses et rapports géographiques.

## ⚙️ Responsabilité technique
Bean `jjwg_Areas` (hérite de `jjwg_Areas_sugar`). Vues spécialisées avec carte pour la définition des zones.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `views/` | Vues carte détail et édition des zones | [→ CONTEXT](views/CONTEXT.md) |
| `Dashlets/` | Dashlet liste des zones | [→ CONTEXT](Dashlets/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues | [→ CONTEXT](metadata/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `jjwg_Areas.php` | Bean zone géographique | [→ fiche](jjwg_Areas.php.doc.md) |
| `controller.php` | Contrôleur MVC | [→ fiche](controller.php.doc.md) |
| `vardefs.php` | Schéma de la table des zones | [→ fiche](vardefs.php.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.php.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consommé par :** `jjwg_Maps` (affichage des zones sur la carte)

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
