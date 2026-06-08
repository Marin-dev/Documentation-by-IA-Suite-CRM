# Fichier : LeadsJjwg_MapsLogicHook.php

**Chemin :** `modules/Leads/LeadsJjwg_MapsLogicHook.php`
**Type :** `PHP`
**Categorie :** logic hook
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Logic hook de geocodage pour le module Leads. Met a jour les coordonnees GPS d'un lead via le module `jjwg_Maps` avant la sauvegarde, et propage le geocodage aux reunions liees apres la sauvegarde.

## Role technique

Classe `LeadsJjwg_MapsLogicHook` similaire a `AccountsJjwg_MapsLogicHook` mais plus simple : deux evenements (`before_save`, `after_save`), sans propagation aux projets/opportunites/cases.

---

## Dependances cles

| Dependance | Role |
| --- | --- |
| `jjwg_Maps` (module) | Fournit `updateGeocodeInfo()` via `get_module_info()` |

## Exports / Symboles principaux

| Symbole | Type | Role |
| --- | --- | --- |
| `LeadsJjwg_MapsLogicHook` | classe | Hook geocodage pour les leads |
| `updateGeocodeInfo($bean, $event, $args)` | methode | before_save : geocode le lead |
| `updateRelatedMeetingsGeocodeInfo($bean, $event, $args)` | methode | after_save : propage aux reunions liees |

## Relations cles

- **Appele par :** Framework SuiteCRM logic hooks (enregistrement dans `logic_hooks.php` du module)

---

## Points d'attention

- Moins de methodes que `AccountsJjwg_MapsLogicHook` : pas de gestion des projets, opportunites ou cases.
- Toutes les operations conditionnees par `logic_hooks_enabled`.
