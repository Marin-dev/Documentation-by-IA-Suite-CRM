# Fichier view.edit.php

**Chemin :** `modules/AOR_Reports/views/view.edit.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Vue EditView du module AOR_Reports. Prépare et injecte les données des lignes existantes (champs, conditions, graphiques) sous forme de JSON pour l'initialisation du formulaire de configuration dynamique. Injecte également les listes de valeurs (tri, totaux, formats) pour les sélecteurs JS.

## Type
view

---

## Dépendances clés
- `ViewEdit` (classe parente)
- `modules/AOW_WorkFlow/aow_utils.php`, `modules/AOR_Reports/aor_utils.php`
- `getDisplayForField()` — labels des champs/modules
- `jqtree.css` — CSS de l'arbre de sélection de champs
- `BeanFactory`

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `AOR_ReportsViewEdit` | classe | Vue édition des rapports |
| `preDisplay()` | méthode | Injecte JS/CSS et données JSON pour l'éditeur dynamique |
| `getFieldLines()` | méthode (privée) | Charge les champs existants du rapport en tableau JSON |
| `getConditionLines()` | méthode (privée) | Charge les conditions existantes en tableau JSON |
| `getChartLines()` | méthode (privée) | Charge les graphiques existants en tableau JSON |

## Interactions
- **Appelé par :** Framework SuiteCRM (EditView AOR_Reports)
- **Appelle :** `getDisplayForField()`, `BeanFactory::newBean()`

## Notes
- Les données sont injectées dans des variables JS : `fieldLines`, `conditionLines`, `chartLines`.
- Les valeurs de `sort_by_values`, `total_values`, `format_values` sont injectées en JS depuis `$app_list_strings`.
- Le cache JS des langues AOR_Fields et AOR_Conditions est généré si absent.
