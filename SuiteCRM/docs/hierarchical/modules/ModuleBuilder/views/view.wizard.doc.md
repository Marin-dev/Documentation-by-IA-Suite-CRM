# view.wizard.php

**Chemin :** `modules/ModuleBuilder/views/view.wizard.php`
**Type :** PHP (view)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Vue du wizard de navigation ModuleBuilder/Studio. Affiche le panneau central avec l'arborescence des sous-sections disponibles pour un module (layouts, subpanels, search, etc.).

## Type
view

## Dépendances clés
- `SugarView` (parente)
- `StudioModuleFactory`, `AjaxCompose`

## Exports/Symboles principaux
- `ViewWizard` (ou similaire) — classe

## Interactions
- **Rendue par :** `ModuleBuilderController::action_wizard()` -> `$this->view = 'wizard'`
