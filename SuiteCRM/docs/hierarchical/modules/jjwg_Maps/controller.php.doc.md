# controller.php (jjwg_Maps)

**Chemin :** `modules/jjwg_Maps/controller.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Controleur central du module jjwg_Maps. Orchestre toutes les actions : affichage de carte, geocodage par lot, configuration admin, recherche par rayon, gestion du cache d'adresses et export CSV.

**Type :** controller

---

## Dependances cles
- `SugarController` — classe parente
- `include/utils.php`, `include/export_utils.php` — utilitaires SuiteCRM
- `include/Sugar_Smarty.php` — moteur de templates pour les info-bulles de marqueurs
- `modules/jjwg_Maps/jjwg_Maps.php` — bean principal (instancie via `BeanFactory::newBean`)
- `jjwg_Address_Cache` — cache geocodage
- Modules CRM (Accounts, Contacts, etc.) via `get_module_info()`

---

## Actions principales

| Action | Methode | Role |
|---|---|---|
| geocoded_counts | `action_geocoded_counts()` | Statistiques de geocodage par module et statut |
| geocode_addresses | `action_geocode_addresses()` | Geocodage par lot (cURL Google + cache) |
| geocoding_test | `action_geocoding_test()` | Test unitaire d'une adresse |
| config | `action_config()` | Formulaire de configuration admin (POST-GET-Redirect) |
| reset_geocoding | `action_reset_geocoding()` | Reset des geocodages d'un module (admin seulement) |
| delete_all_address_cache | `action_delete_all_address_cache()` | Suppression du cache d'adresses (admin seulement) |
| quick_radius | `action_quick_radius()` | Formulaire de recherche par adresse+rayon |
| quick_radius_display | `action_quick_radius_display()` | Affiche la carte radius dans une iframe |
| map_display | `action_map_display()` | Encapsule la vue map_markers dans une iframe |
| map_markers | `action_map_markers()` | Charge les donnees de marqueurs et les passe a la vue |
| add_to_target_list | `action_add_to_target_list()` | Ajoute les marqueurs selectionnes a une liste de prospects (JSON) |
| export_geocoding_addresses | `action_export_geocoding_addresses()` | Export CSV des adresses non geocodees |
| donate | `action_donate()` | Page donate |

## Methodes de support

| Methode | Role |
|---|---|
| `configuration()` | Charge `$GLOBALS['jjwg_config']` depuis le bean |
| `getMarkerData($module, $display, $center, $mod_strings)` | Construit un tableau de donnees de marqueur + HTML Smarty |
| `getMarkerDataCustom($marker_object)` | Donnees de marqueur personnalise (jjwg_Markers) |
| `getAreaDataCustom($area_object)` | Donnees de zone personnalisee (jjwg_Areas) |
| `defineMapsAddressCustom($aInfo, $object_name, $display)` | Point d'extension pour la logique d'adresse custom |
| `is_valid_lat/lng()` | Validation coordonnees |
| `do_list_csv_output()` / `list_row_to_csv()` | Export CSV |

---

## Interactions
- **Appelle :** `jjwg_Maps` (bean), `jjwg_Address_Cache`, API Google Maps (via bean), modules CRM
- **Appele par :** framework MVC SuiteCRM (dispatcher), `jjwg_Maps_Router.php` (cron)
- **Passe donnees aux vues via :** `$this->bean->map_markers`, `map_center`, `custom_markers`, `custom_areas`, `geocoded_counts`

---

## Notes
- `action_map_markers()` est la plus complexe : gere 3 modes (record, list_id, uid/current_post) et calcule la distance via SQL (formule Haversine simplifiee en degres, lignes 756-758).
- La throttle du geocodage (sleep 1s tous les 10 enregistrements, ligne 289) est necessaire pour respecter les quotas Google (10 req/s).
- `getMarkerData()` charge des templates Smarty depuis `modules/jjwg_Maps/tpls/{ModuleType}InfoWindow.tpl` ou `custom/` en override.
- Bug potentiel dans `getAreaDataCustom()` ligne 1200 : `$this->sugarSmarty->fetch()` sans argument (l'URL du template est manquante pour la version custom).
- `$map_marker_data_points` sert a deduplication des marqueurs a position identique en appliquant `map_duplicate_marker_adjustment`.
