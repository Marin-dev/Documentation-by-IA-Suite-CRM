# predefined_charts.php

**Chemin :** `modules/Charts/code/predefined_charts.php`
**Type :** PHP - Configuration
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Définit le tableau `$predefined_charts` listant les 5 graphiques prédéfinis du module Charts avec leurs métadonnées (type, id, libellé localisé, type de graphique).

## Type
config

## Dépendances clés
- `return_module_language()` — chargement des chaînes du module Charts

## Exports / Symboles principaux
- `$predefined_charts` (array) — clés : `Chart_pipeline_by_sales_stage`, `Chart_lead_source_by_outcome`, `Chart_outcome_by_month`, `Chart_pipeline_by_lead_source`, `Chart_my_pipeline_by_sales_stage`

## Interactions
- **Appelé par :** logique de sélection de graphiques (INCONNU — consommateur à identifier)

## Notes
- Fichier de configuration pure, sans logique.
