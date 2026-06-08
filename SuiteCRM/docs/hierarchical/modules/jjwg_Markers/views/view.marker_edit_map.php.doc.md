# view.marker_edit_map.php

**Chemin :** `modules/jjwg_Markers/views/view.marker_edit_map.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Vue d'edition cartographique d'un marqueur. Affiche un marqueur draggable sur Google Maps. Le deplacement du marqueur met a jour en temps reel les champs `jjwg_maps_lat` et `jjwg_maps_lng` dans le formulaire parent (via `parent.document`).

**Type :** view

---

## Dependances cles
- `SugarView` — classe parente
- Google Maps API JS (CDN)
- `$GLOBALS['loc']` — position et image initiales
- `$GLOBALS['current_user']` — preferences de separateur decimal et groupement numerique
- `$GLOBALS['sugar_config']` — separateurs par defaut

---

## Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `Jjwg_MarkersViewMarker_Edit_Map` | Classe | Vue SugarView |
| `display()` | Methode | Carte avec marqueur draggable + callbacks JS |
| `updateEditFormLatLng(latLng)` | Fonction JS | Ecrit lat/lng dans `parent.document.getElementById('jjwg_maps_lat/lng')` avec conversion locale |

---

## Interactions
- **Appelee par :** `jjwg_MarkersController::action_marker_edit_map()`
- **Ecrit dans :** `parent.document.getElementById('jjwg_maps_lat')` et `'jjwg_maps_lng'` + `'description'` (adresse la plus proche)

---

## Notes
- Respecte les parametres de localisation de l'utilisateur (separateur decimal) pour la conversion des coordonnees.
- Fonctionne dans une iframe du formulaire d'edition.
