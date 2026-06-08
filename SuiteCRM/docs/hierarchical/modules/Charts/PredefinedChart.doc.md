# PredefinedChart.php

**Chemin :** `modules/Charts/PredefinedChart.php`
**Type :** PHP - Helper / Service
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Génère les requêtes SQL pour les graphiques prédéfinis du CRM : pipeline par étape de vente, résultats par source de prospect, résultats par mois, pipeline par source de prospect, et utilisation des modules. Les paramètres de filtre (dates, étapes, utilisateurs) proviennent des préférences utilisateur ou de `$_REQUEST`.

## Type
helper / model

## Dépendances clés
- `BeanFactory` / `Opportunity` — objet opportunité
- `DBManagerFactory` — conversion de dates SQL selon le SGBD
- `$current_user->getPreference/setPreference` — persistance des filtres
- `$timedate` — gestion des dates
- `$app_list_strings` — libellés pour les enums (sales_stage, lead_source)
- `get_user_array()` — liste d'utilisateurs
- `custom/Charts/{chart}.php` — surcharge de graphique (méthode `customChartQuery`)

## Exports / Symboles principaux
- `PredefinedChart` (classe)
  - `predefinedChartQuery($chart, $params)` — dispatcher vers la bonne méthode
  - `pipelineBySalesStageQuery()` — SQL pipeline par étape
  - `leadSourceByOutcomeQuery($filters)` — SQL sources/résultats
  - `outcomeByMonthQuery()` — SQL résultats par mois
  - `pipelineByLeadSourceQuery($filters)` — SQL pipeline par source
  - `myModuleUsageLast30Days()` — SQL utilisation modules 30 derniers jours
  - `customChartQuery($chart)` — délégation à `custom/Charts/`

## Interactions
- **Appelé par :** dashlets de Charts (`PipelineBySalesStageDashlet`, etc.)
- **Appelle :** `DBManagerFactory`, `BeanFactory`, préférences utilisateur

## Notes
- Construction de SQL dynamique avec interpolation de valeurs utilisateur — bien que passées par `$db->quote()`, vigilance recommandée.
- Utilisation de `$GLOBALS['log']->fatal()` pour du debug (lignes 246-255) — vestige de développement.
