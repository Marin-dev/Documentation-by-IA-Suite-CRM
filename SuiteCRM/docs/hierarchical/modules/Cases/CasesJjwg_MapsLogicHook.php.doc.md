# 📄 CasesJjwg_MapsLogicHook.php

**Chemin :** `modules/Cases/CasesJjwg_MapsLogicHook.php`
**Type :** PHP — logic hook
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Logic hook reliant le module Cases au module de cartographie jjwg_Maps. Met à jour les informations de géocodage d'un cas et de ses réunions associées lors des sauvegardes et modifications de relations.

## Rôle technique

Classe `CasesJjwg_MapsLogicHook`. Les méthodes sont déclenchées par les events `before_save`, `after_save`, `after_relationship_add`, `after_relationship_delete`. Toutes les opérations sont conditionnées à `logic_hooks_enabled`.

---

## Exports / Symboles principaux

| Méthode | Event | Rôle |
|---|---|---|
| `updateGeocodeInfo()` | `before_save` | Met à jour les coordonnées géo du cas |
| `updateRelatedMeetingsGeocodeInfo()` | `after_save` | Met à jour les réunions liées |
| `addRelationship()` | `after_relationship_add` | Recalcule le géocodage après ajout de relation |
| `deleteRelationship()` | `after_relationship_delete` | Recalcule le géocodage après suppression de relation |

---

## Relations clés

- **Appelé par :** framework logic hooks SugarCRM (module Cases)
- **Appelle :** `jjwg_Maps::updateGeocodeInfo()`, `jjwg_Maps::updateRelatedMeetingsGeocodeInfo()`
- **Position dans le flux global :** intégration cartographique optionnelle sur les cas

---

## Notes

- Toutes les opérations sont no-op si `jjwg_Maps->settings['logic_hooks_enabled']` est false.
