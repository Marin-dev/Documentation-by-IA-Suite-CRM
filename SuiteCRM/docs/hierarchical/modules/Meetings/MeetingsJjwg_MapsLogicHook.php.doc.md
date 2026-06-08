# Fichier : MeetingsJjwg_MapsLogicHook.php

**Chemin :** `modules/Meetings/MeetingsJjwg_MapsLogicHook.php`
**Type :** helper (logic hook)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Logic hook d'integration avec le module de cartographie `jjwg_Maps`. Apres la sauvegarde d'une reunion, met a jour les coordonnees de geocodage associees si les logic hooks de la carte sont actives.

## Role technique
Classe avec une methode `updateMeetingGeocodeInfo()` qui delege a `$this->jjwg_Maps->updateMeetingGeocodeInfo($bean)` si le parametre `logic_hooks_enabled` est actif. Le module `jjwg_Maps` est charge via `get_module_info()` dans le constructeur.

---

## Dependances cles
- `jjwg_Maps` (module cartographie, charge via `get_module_info('jjwg_Maps')`)

## Exports / Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `MeetingsJjwg_MapsLogicHook` | classe | logic hook geocodage reunions |
| `updateMeetingGeocodeInfo()` | methode | mise a jour geocodage apres save |

---

## Relations cles
- **Appele par :** framework logic hooks SuiteCRM (after_save sur Meetings)
- **Appelle :** `jjwg_Maps::updateMeetingGeocodeInfo()`

---

## Points d'attention
- N'agit que si `jjwg_Maps->settings['logic_hooks_enabled']` est vrai — desactivable via configuration.
