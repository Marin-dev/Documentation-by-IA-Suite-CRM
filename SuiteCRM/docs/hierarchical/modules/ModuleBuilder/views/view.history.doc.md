# view.history.php

**Chemin :** `modules/ModuleBuilder/views/view.history.php`
**Type :** PHP (view)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Vue de l'historique des versions d'un layout. Permet de naviguer entre les versions sauvegardées et de restaurer une version précédente.

## Type
view

## Dépendances clés
- `SugarView` (parente)
- `History` (`parsers/views/History.php`)
- `ParserFactory`

## Exports/Symboles principaux
- `ViewHistory` (ou similaire) — classe

## Interactions
- **Rendue par :** `ModuleBuilderController::action_history()` -> `$this->view = 'history'`
