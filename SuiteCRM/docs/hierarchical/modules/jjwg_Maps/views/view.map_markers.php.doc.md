# view.map_markers.php

**Chemin :** `modules/jjwg_Maps/views/view.map_markers.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Vue principale de rendu cartographique. Affiche la carte Google Maps avec tous les marqueurs, zones polygonales et marqueurs personnalises. Integre DataTables pour le listing des marqueurs, un systeme de legende par groupe, le clustering de marqueurs et des outils de dessin de selection.

**Type :** view

---

## Dependances cles
- `SugarView` — classe parente
- Google Maps API JS + librairies `drawing`, `geometry` (CDN)
- jQuery
- `markerclusterer_packed.js` — clustering des marqueurs
- DataTables 1.9.4 + TableTools 2.1.5 (CDN cdnjs)
- `$this->bean` — donnees preparees par `jjwg_MapsController::action_map_markers()`
- `$GLOBALS['jjwg_config']` — configuration (cle API, limites, etc.)

---

## Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `Jjwg_MapsViewMap_Markers` | Classe | Vue SugarView |
| `display()` | Methode | Genere la page HTML complete (autonome, dans iframe) |
| `initialize()` | Fonction JS | Initialise Google Map, marqueurs, clusterer, legende |
| `setCenterMarker()` | Fonction JS | Pose le marqueur central (point de reference) |
| `setMarkers()` | Fonction JS | Pose tous les marqueurs du resultat |
| `setCustomMarkers()` | Fonction JS | Pose les marqueurs jjwg_Markers avec icones custom |
| `setCustomAreas()` | Fonction JS | Trace les polygones jjwg_Areas |
| `setODataTable()` | Fonction JS | Initialise DataTable avec donnees des marqueurs |
| `toggleMarkerGroupVisibility()` | Fonction JS | Bascule visibilite d'un groupe |
| `clickMarkerById()` | Fonction JS | Clique programmatiquement sur un marqueur |
| `listSelectedShape()` | Fonction JS | Filtre la DataTable selon la selection polygonale |

---

## Interactions
- **Chargee par :** `Jjwg_MapsViewMap_Display` (via iframe)
- **Recoit depuis controleur :** `$this->bean->map_markers`, `map_center`, `map_markers_groups`, `custom_markers`, `custom_areas`, `list_array`
- **Emet vers controleur :** formulaire POST `add_to_target_list` (AJAX)

---

## Notes
- Affiche un message d'erreur si `google_maps_api_key` est vide (ligne 939-941).
- Le choix du repertoire d'icones (0-10, 0-25, 0-100, 0-216) depend du nombre de groupes (lignes 141-152).
- Jusqu'a 216 groupes distincts supportes.
- Le clustering est gere par `MarkerClustererPlus v2.1.1`.
- Les infowindows sont generes par Smarty (`{Module}InfoWindow.tpl`), preparees cote PHP dans le controleur.
- La DataTable supporte export Copy/CSV/XLS/PDF/Print.
- Appel parent possible via `window.parent.resizeDataTables()` pour le redimensionnement de l'iframe.
