# view.relationships.php

**Chemin :** `modules/ModuleBuilder/views/view.relationships.php`
**Type :** PHP (view)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Vue de la liste des relations d'un module. Affiche toutes les relations définies (deployed ou undeployed) avec options de création/suppression.

## Type
view

## Dépendances clés
- `SugarView` (parente)
- `AjaxCompose`, `ModuleBuilder`, `StudioModule`, `StudioBrowser`
- `view.relationship.php` (incluse)

## Exports/Symboles principaux
- `ViewRelationships` — classe

## Interactions
- **Rendue par :** `action_view_map.php` -> `'relationships' => 'relationships'`
