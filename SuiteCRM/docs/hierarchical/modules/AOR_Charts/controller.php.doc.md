# Fichier controller.php

**Chemin :** `modules/AOR_Charts/controller.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Contrôleur du module AOR_Charts. Gère les actions AJAX de rendu et de récupération des image maps des graphiques pChart.

## Type
controller

---

## Dépendances clés
- `SugarController` (classe parente)
- `AOR_Chart` (bean graphique)
- `AOR_Report` (bean rapport)
- `modules/AOR_Reports/aor_utils.php`

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `AOR_ChartsController` | classe | Contrôleur AOR_Charts |
| `action_getImageMap()` | méthode | Retourne le contenu de l'image map pChart pour un graphique |

## Interactions
- **Appelé par :** Vue DetailView AOR_Reports (appel AJAX pour les image maps pChart)
- **Appelle :** `AOR_Chart::buildChartImage()`, cache ImageMap

## Notes
- Utilisé uniquement pour le moteur pChart (les autres moteurs génèrent le HTML côté client).
