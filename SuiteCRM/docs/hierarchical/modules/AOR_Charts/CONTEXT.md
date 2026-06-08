# 📁 AOR_Charts

**Chemin :** `modules/AOR_Charts/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module AOR_Charts gère les graphiques associés aux rapports AOR (Advanced OpenReports). Il permet de visualiser les données des rapports sous forme de barres, courbes, camemberts, radars, etc. avec trois moteurs de rendu disponibles.

## ⚙️ Responsabilité technique
Bean `AOR_Chart` (hérite de `Basic`). Trois moteurs de rendu : pChart (images PNG base64), Chart.js (canvas HTML5), RGraph (canvas HTML5 interactif). La méthode `buildChartHTML` dispatche vers le bon moteur. Librairie pChart embarquée dans `lib/`.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `language/` | Traductions anglaises du module | [→ CONTEXT](language/CONTEXT.md) |
| `lib/` | Librairie pChart pour génération d'images | [→ CONTEXT](lib/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `AOR_Chart.php` | Bean graphique avec multi-moteurs de rendu | [→ fiche](AOR_Chart.doc.md) |
| `controller.php` | Contrôleur AJAX pour les image maps pChart | [→ fiche](controller.php.doc.md) |
| `vardefs.php` | Schéma de la table `aor_charts` | [→ fiche](vardefs.php.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `AOR_Reports` (relation parent `aor_report_id`), librairie pChart, Chart.js, RGraph
- **Consommé par :** `AOR_Report::build_report_chart()` qui appelle `buildChartHTML()`
- **Flux typique :** Rapport AOR → `build_report_chart()` → `AOR_Chart::buildChartHTML()` → rendu HTML/PNG selon moteur configuré

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre la génération de graphiques | [`AOR_Chart.php`](AOR_Chart.doc.md) |
| Voir les image maps pChart (AJAX) | [`controller.php`](controller.php.doc.md) |

---

## ⚠️ Zones INCONNU
- Couleurs RGraph générées par hash MD5 — peut produire des couleurs peu contrastées
- `grouped_bar` et `stacked_bar` nécessitent un champ de groupe explicite
