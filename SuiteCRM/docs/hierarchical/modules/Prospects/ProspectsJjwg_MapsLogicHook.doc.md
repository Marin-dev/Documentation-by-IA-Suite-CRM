# ProspectsJjwg_MapsLogicHook.php

**Chemin :** `modules/Prospects/ProspectsJjwg_MapsLogicHook.php`
**Type :** PHP - Logic Hook (géocodage)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Logic hook intégrant le géocodage JJW Google Maps pour les Prospects. Déclenche la mise à jour des coordonnées géographiques lors de la sauvegarde d'un prospect (before_save) et met à jour les réunions liées (after_save).

## Type
helper (logic hook)

## Dépendances clés
- `get_module_info('jjwg_Maps')` — module de cartographie JJW Google Maps
- `$this->jjwg_Maps->settings['logic_hooks_enabled']` — activation/désactivation

## Exports / Symboles principaux
- `ProspectsJjwg_MapsLogicHook` (classe)
  - `$jjwg_Maps` — référence au module de cartographie
  - `updateGeocodeInfo(&$bean, $event, $arguments)` — before_save : géocodage du prospect
  - `updateRelatedMeetingsGeocodeInfo(&$bean, $event, $arguments)` — after_save : mise à jour des réunions liées

## Interactions
- **Appelé par :** logic hooks framework SuiteCRM (`before_save`, `after_save` sur Prospects)
- **Appelle :** `jjwg_Maps::updateGeocodeInfo()`, `jjwg_Maps::updateRelatedMeetingsGeocodeInfo()`

## Notes
- Conditionné par `logic_hooks_enabled` — peut être désactivé depuis la config JJW Maps.
