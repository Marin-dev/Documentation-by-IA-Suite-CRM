# AOR_Chart.php

**Chemin :** `modules/AOR_Charts/AOR_Chart.php`
**Type :** PHP - Modele (Model)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Modele representant un graphique associe a un rapport AOR. Gere la generation de graphiques en plusieurs moteurs (pChart, Chart.js, RGraph) pour visualiser les donnees des rapports sous forme de barres, courbes, camemberts, radars, etc.

## Role technique
Etend `Basic`. Supporte trois moteurs de rendu : pChart (images PNG base64), Chart.js (canvas HTML5), RGraph (canvas HTML5 interactif). La methode `buildChartHTML` dispatch vers le bon moteur. La methode `save_lines` gere la persistance des graphiques lies a un rapport.

---

## Dependances / Imports
- `Basic` (classe parente SugarCRM)
- `modules/AOR_Charts/lib/pChart/pChart.php` — moteur pChart
- Classes pChart : `pData`, `pImage`, `pPie`, `pRadar`
- `BeanFactory` (framework SugarCRM)

## Exports / Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `AOR_Chart` | Classe | Modele graphique |
| `COLOUR_DEFAULTS` | Constante | Palette de 24 couleurs HEX par defaut |
| `save_lines(array $post, AOR_Report $bean, $postKey)` | Methode | Sauvegarde les graphiques depuis un POST |
| `buildChartHTML($reportData, $fields, $index, $chartType, $mainGroupField)` | Methode | Genere le HTML du graphique |
| `buildChartImage($reportData, $fields, $asDataURI, $generateImageMapId)` | Methode | Genere une image PNG via pChart |

**Types de graphiques supportes :** `bar`, `line`, `pie`, `radar`, `rose`, `grouped_bar`, `stacked_bar`

**Consommateurs :**
- `modules/AOR_Reports/AOR_Report.php` — appelle `buildChartHTML` dans `build_report_chart()`

## Relations cles
- **Appele par :** `AOR_Report->build_report_chart()`
- **Table DB :** `aor_charts`
- **Relation parent :** `aor_report_id` vers `aor_reports`

---

## Points d'attention
- Les couleurs RGraph sont generees par hash MD5 du label (peut produire des couleurs peu contrastees).
- Le moteur pChart genere des images PNG en memoire via `ob_start/ob_get_clean` et retourne un Data URI base64.
- Le moteur Chart.js emettait du JavaScript inline dependant de jQuery et de `SUGAR.util.doWhen`.
- `grouped_bar` et `stacked_bar` necessitent un champ de groupe principal (`mainGroupField`) pour fonctionner correctement.
- `getValidChartTypes()` est la liste d'autorisation des types — tout type non liste est ignore silencieusement.
