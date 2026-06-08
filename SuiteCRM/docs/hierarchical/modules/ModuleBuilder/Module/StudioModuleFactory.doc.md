# StudioModuleFactory.php

**Chemin :** `modules/ModuleBuilder/Module/StudioModuleFactory.php`
**Type :** PHP (helper / factory)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Factory avec cache statique pour les instances `StudioModule`. Supporte les modules ayant une classe de studio personnalisée (`{Module}StudioModule.php`) en cherchant d'abord dans `custom/modules/` puis `modules/`.

## Type
helper (factory)

## Dépendances clés
- `StudioModule` (`Module/StudioModule.php`)

## Exports/Symboles principaux
- `StudioModuleFactory` — classe (méthodes statiques)
  - `getStudioModule($module)` — retourne (ou crée + cache) l'instance `StudioModule` pour le module donné

## Interactions
- **Appelé par :** `ModuleBuilderController`, `ParserFactory`, `StudioBrowser`, `MBPackage`, `StudioModule::getRelationships()`
- **Appelle :** `StudioModule` (ou sous-classe personnalisée)

## Notes
- Cache statique `$loadedMods` — une même instance est réutilisée sur toute la durée de la requête. Ligne 52.
- Lookup d'override : `custom/modules/{Module}/{Module}StudioModule.php` > `modules/{Module}/{Module}StudioModule.php` > `StudioModule` générique.
