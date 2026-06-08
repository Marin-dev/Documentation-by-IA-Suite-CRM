# Fichier view.detail.php

**Chemin :** `modules/AOR_Reports/views/view.detail.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Vue DetailView du module AOR_Reports. Génère et injecte le contenu du rapport (tableau de résultats + graphiques RGraph) et les paramètres de filtrage dynamiques dans la page de détail. Gère le redimensionnement des graphiques selon la largeur disponible.

## Type
view

---

## Dépendances clés
- `ViewDetail` (classe parente)
- `modules/AOW_WorkFlow/aow_utils.php`, `modules/AOR_Reports/aor_utils.php`
- `AOR_Report::buildMultiGroupReport()`, `AOR_Report::build_report_chart()`
- `requestToUserParameters()` — paramètres de filtrage depuis GET/POST
- RGraph JavaScript (chargé par `build_report_chart`)
- `getDisplayForField()` — résolution des labels

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `AOR_ReportsViewDetail` | classe | Vue détail des rapports |
| `preDisplay()` | méthode | Génère le HTML du rapport, les graphiques, injecte les paramètres JS |
| `getReportParameters()` | méthode (privée) | Prépare les conditions paramétrables pour `reportParameters` JS |

## Interactions
- **Appelé par :** Framework SuiteCRM (index.php?module=AOR_Reports&action=DetailView)
- **Appelle :** `AOR_Report::buildMultiGroupReport()`, `AOR_Report::build_report_chart(CHART_TYPE_RGRAPH)`

## Notes
- Les graphiques utilisent le moteur RGraph (pas pChart ni Chart.js).
- `resizeGraphsPerRow()` est une fonction JS inline qui redimensionne les canvas RGraph en fonction de la largeur du panneau divisée par `graphs_per_row`.
- Le cache JS des langues AOR_Conditions est généré à la volée si absent.
- Les paramètres dynamiques sont injectés en `<script>var reportParameters = [...];</script>`.
