# view.config.php

**Chemin :** `modules/jjwg_Maps/views/view.config.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Vue du formulaire de configuration admin du module jjwg_Maps. Permet de configurer la cle Google Maps API, les modules geocodables, les types d'adresses, les limites de geocodage, les parametres de carte et le cache d'adresses.

**Type :** view

---

## Dependances cles
- `SugarView` — classe parente
- `$GLOBALS['jjwg_config']` et `$GLOBALS['jjwg_config_defaults']` — valeurs courantes et defauts
- `$GLOBALS['mod_strings']` — labels

---

## Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `Jjwg_MapsViewConfig` | Classe | Vue formulaire config |
| `display()` | Methode | Genere le formulaire HTML de configuration |

## Sections du formulaire

| Section | Parametres cles |
|---|---|
| API Google Maps | google_maps_api_key |
| Modules geocodables | valid_geocode_modules, valid_geocode_tables |
| Types d'adresses | address_type_{Module} pour chaque module |
| Champs de groupement | grouping_field_{Module} |
| Geocodage | geocoding_api_url, geocoding_api_secret, geocoding_limit, google_geocoding_limit, allow_approximate_location_type, export_addresses_limit |
| Cache d'adresses | address_cache_get_enabled, address_cache_save_enabled |
| Logic Hooks | logic_hooks_enabled |
| Marqueurs | map_markers_limit, map_default_center_latitude/longitude, map_default_unit_type, map_default_distance, map_duplicate_marker_adjustment, map_clusterer_grid_size, map_clusterer_max_zoom |

---

## Interactions
- **Appelee par :** `jjwg_MapsController::action_config()` (admin seulement)
- **Soumet vers :** `action_config()` (POST-GET-Redirect pattern)

---

## Notes
- Accessible uniquement aux administrateurs (`$GLOBALS['current_user']->is_admin`).
- Les modules custom (hors liste par defaut) sont detectes et des selects sont generes dynamiquement.
