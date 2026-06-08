# view.relationship.php

**Chemin :** `modules/ModuleBuilder/views/view.relationship.php`
**Type :** PHP (view)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Vue du formulaire d'édition d'une relation individuelle. Permet de créer ou modifier une relation entre modules.

## Type
view

## Dépendances clés
- `SugarView` (parente)
- `AjaxCompose`, `ModuleBuilder`, `StudioModuleFactory`, `StudioBrowser`
- `RelationshipFactory`, `constants.php`

## Exports/Symboles principaux
- `ViewRelationship` — classe

## Interactions
- **Rendue par :** `action_view_map.php` -> `'relationship' => 'relationship'`
- **Incluse par :** `view.relationships.php`
