# view.marker_detail_map.php

**Chemin :** `modules/jjwg_Markers/views/view.marker_detail_map.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Vue de detail cartographique d'un marqueur. Affiche la position du marqueur sur Google Maps avec son icone personnalisee et l'adresse la plus proche via geocodage inverse.

**Type :** view

---

## Dependances cles
- `SugarView` — classe parente
- Google Maps API JS (CDN, cle API dans `$GLOBALS['jjwg_config']`)
- `$GLOBALS['loc']` — position et image du marqueur (injecte par le controleur)

---

## Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `Jjwg_MarkersViewMarker_Detail_Map` | Classe | Vue SugarView |
| `display()` | Methode | Genere la page HTML avec marqueur fixe (non draggable) et geocodage inverse |

---

## Interactions
- **Appelee par :** `jjwg_MarkersController::action_marker_detail_map()`

---

## Notes
- Marqueur non deplacable (`draggable: false`).
- L'icone est chargee depuis `themes/default/images/jjwg_Markers/{image}.png`.
- Le geocodage inverse (`geocoder.geocode({latLng})`) affiche l'adresse la plus proche dans `#address`.
