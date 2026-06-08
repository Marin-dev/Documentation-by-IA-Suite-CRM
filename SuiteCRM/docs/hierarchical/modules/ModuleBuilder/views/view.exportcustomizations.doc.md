# view.exportcustomizations.php

**Chemin :** `modules/ModuleBuilder/views/view.exportcustomizations.php`
**Type :** PHP (view)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Vue du formulaire d'export des personnalisations Studio. Permet de sélectionner les modules à exporter et de générer un ZIP de personnalisations.

## Type
view

## Dépendances clés
- `SugarView` (parente)
- `AjaxCompose`, `MBPackage`

## Exports/Symboles principaux
- `ViewExportcustomizations` (ou similaire) — classe

## Interactions
- **Rendue par :** `action_view_map.php` -> `'exportcustomizations' => 'exportcustomizations'`
