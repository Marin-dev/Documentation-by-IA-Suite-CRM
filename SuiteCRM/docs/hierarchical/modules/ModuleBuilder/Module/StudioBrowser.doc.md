# StudioBrowser.php

**Chemin :** `modules/ModuleBuilder/Module/StudioBrowser.php`
**Type :** PHP (helper)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Charge la liste des modules accessibles dans Studio (ceux qui ont `metadata/studio.php` et qui sont dans `$beanList`). Filtre selon les droits du `current_user`. Retourne les noeuds de navigation pour l'arbre Studio.

## Type
helper

## Dépendances clés
- `StudioModuleFactory` (`Module/StudioModuleFactory.php`)

## Exports/Symboles principaux
- `StudioBrowser` — classe
  - `loadModules()` — charge les modules accessibles (filtrés par droits admin/développeur)
  - `loadRelatableModules()` — charge tous les modules Studio sans filtre de droits (pour les relations)
  - `getNodes()` — retourne les noeuds triés alphabétiquement
- `cmp($a, $b)` — fonction globale de comparaison pour `uksort`

## Interactions
- **Appelé par :** `StudioTree`, `AbstractRelationships::findRelatableModules()`
- **Appelle :** `StudioModuleFactory::getStudioModule()`

## Notes
- `loadModules()` et `loadRelatableModules()` sont deux méthodes distinctes car les droits d'accès diffèrent (Studio filtre, les relations non). Ligne 53 vs 69.
- Le tri `uksort($nodes, 'cmp')` impose l'ordre alphabétique insensible à la casse pour la cohérence de l'arbre. Ligne 88.
