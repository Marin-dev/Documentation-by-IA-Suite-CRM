# jjwg_Markers.php

**Chemin :** `modules/jjwg_Markers/jjwg_Markers.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Modele principal du module de marqueurs cartographiques jjwg_Markers. Represente un marqueur personnalise (icone, position lat/lng) pouvant etre associe a une carte jjwg_Maps.

**Type :** model

---

## Dependances cles
- `modules/jjwg_Markers/jjwg_Markers_sugar.php` — classe parente ORM
- `modules/jjwg_Maps/jjwg_Maps.php` — chargement de la configuration
- `BeanFactory::newBean('jjwg_Maps')` — chargement de la config
- `$GLOBALS['jjwg_config']` — parametres de carte (lat/lng par defaut)
- `LoggerManager` — journalisation

---

## Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `jjwg_Markers` | Classe | Bean principal du module marqueurs |
| `configuration()` | Methode | Charge les settings depuis jjwg_Maps |
| `define_loc($marker)` | Methode | Retourne tableau `['name','lat','lng','image']` normalise pour le rendu |
| `is_valid_lng($lng)` | Methode | Valide une longitude |
| `is_valid_lat($lat)` | Methode | Valide une latitude |

---

## Interactions
- **Appelle :** `jjwg_Maps_sugar` (via heritage), `BeanFactory::newBean('jjwg_Maps')`
- **Appele par :** `jjwg_MarkersController`, `jjwg_MapsController::getMarkerDataCustom()` (recupere les marqueurs lies a une carte)
- **Position dans le flux :** Bean racine du module jjwg_Markers ; instancie via `get_module_info('jjwg_Markers')`

---

## Notes
- Beaucoup plus simple que jjwg_Areas : pas d'algorithme geometrique, juste une position lat/lng et une image.
- Le champ `marker_image` est un enum (`marker_image_list`) correspondant a un nom de fichier PNG sans extension dans `custom/themes/default/images/jjwg_Markers/`.
