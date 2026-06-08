# Fichier AOR_Chart.php

**Chemin :** `modules/AOR_Charts/AOR_Chart.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Modèle et moteur de rendu graphique pour les rapports AOR. Représente un graphique associé à un rapport (AOR_Report). Gère la génération d'images via trois bibliothèques distinctes : pChart (image PNG), Chart.js (canvas HTML5), et RGraph (canvas HTML5). Supporte les types bar, line, pie, radar, rose, grouped_bar, stacked_bar.

## Type
model

---

## Dépendances clés
- `Basic` (classe parente)
- `modules/AOR_Charts/lib/pChart/pChart.php` — bibliothèque pChart (pData, pImage, pPie, pRadar)
- `include/SuiteGraphs/RGraphIncludes.php` — bibliothèque RGraph
- `AOR_Report` — référencé pour les constantes CHART_TYPE_*
- `AOR_Field` — passé en paramètre pour `buildChartHTML()`
- `BeanFactory`

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `AOR_Chart` | classe | Bean graphique |
| `COLOUR_DEFAULTS` | constante | 24 couleurs hexadécimales par défaut |
| `save_lines()` | méthode | Sauvegarde/supprime les graphiques depuis POST (appelé par AOR_Report::save) |
| `buildChartHTML()` | méthode | Dispatcher : génère le HTML selon le type de moteur graphique |
| `buildChartImage()` | méthode | Génère une image PNG en base64 (pChart) |
| `buildChartImageBar()` | méthode | Rendu barre pChart |
| `buildChartImageLine()` | méthode | Rendu ligne pChart |
| `buildChartImagePie()` | méthode | Rendu camembert pChart |
| `buildChartImageRadar()` | méthode | Rendu radar pChart |
| `buildChartHTMLChartJS()` | méthode (privée) | Rendu via Chart.js |
| `buildChartHTMLRGraph()` | méthode (privée) | Rendu via RGraph (bar, line, pie, radar, rose, grouped_bar, stacked_bar) |

## Interactions
- **Appelé par :** `AOR_Report::build_report_chart()`, `AOR_Report::save()`
- **Appelle :** `pChart` (pData, pImage, pPie, pRadar), RGraph JavaScript
- **Table BD :** `aor_charts`

## Notes
- Les couleurs sont générées par hash MD5 du label (`getColour()`) si `generateChartColoursFromLabels()` échoue, fallback sur `COLOUR_DEFAULTS`.
- `buildChartImage()` supporte la génération d'image maps (cliquables) pour pChart via `initialiseImageMap`.
- RGraph grouped/stacked bar requiert un champ de groupement principal (`$mainGroupField`) passé depuis `AOR_Report::build_report_chart()`.
- La détection du type se fait par `in_array($this->type, getValidChartTypes())` — types invalides retournent une chaîne vide.
