# uw_ajax.php

**Chemin :** `modules/UpgradeWizard/uw_ajax.php`
**Type :** PHP - Helper (AJAX wizard de mise à jour)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Fournit les fonctions AJAX pour le suivi de la progression SQL lors du wizard de mise à jour. Affiche la progression des requêtes SQL (preflight et exécution) sous forme de pourcentage et d'état.

## Type
helper

## Dépendances clés
- `$mod_strings` — traductions (LBL_UW_PREFLIGHT_QUERY, LBL_UW_DONE, LBL_UW_PREFLIGHT_QUERIES_LEFT)
- `$persistence` — tableau de persistance contenant l'état SQL

## Exports / Symboles principaux
- `ajaxSqlProgress($persistence, $sql, $type)` (fonction) — génère le HTML de progression SQL avec pourcentage, requête courante, et textarea de débogage

## Interactions
- **Appelé par :** scripts de mise à jour (preflight/commit) via AJAX
- **Appelle :** `ob_start()`

## Notes
- Calcul de progression : `(sql_total - whatsLeft) / sql_total * 100` arrondi à 1 décimale.
