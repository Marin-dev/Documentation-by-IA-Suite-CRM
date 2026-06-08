# Chart_outcome_by_month.php

**Chemin :** `modules/Charts/code/Chart_outcome_by_month.php`
**Type :** PHP - Helper (générateur de graphique legacy)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Classe legacy de génération du graphique "Outcome by Month" (opportunités par résultat de vente regroupées par mois). Génère un fichier XML de données pour le rendu via l'ancien moteur de graphiques SugarCRM (`stackedBarF`).

## Type
helper (legacy)

## Dépendances clés
- `include/charts/Charts.php` — fonctions `create_chart()`, `save_xml_file()`
- `BeanFactory::newBean('Opportunities')` — accès aux données
- Table `opportunities` — source SQL

## Exports / Symboles principaux
- `Chart_outcome_by_month` (classe)
  - `draw($extra_tools)` — affiche le formulaire de filtre et le graphique
  - Méthodes de génération XML INCONNU (non lues complètement)

## Interactions
- **Appelé par :** `modules/Charts/code/predefined_charts.php`
- **Appelle :** `Charts.php`

## Notes
- Code legacy utilisant fichiers XML de cache dans `sugar_cached('xml/')`.
