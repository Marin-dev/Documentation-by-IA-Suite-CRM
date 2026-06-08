# jjwg_Maps.php

**Chemin :** `modules/jjwg_Maps/jjwg_Maps.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Modele principal du module de cartographie jjwg_Maps. Centralise : (1) la gestion de la configuration globale (`$GLOBALS['jjwg_config']`), (2) le geocodage des adresses via l'API Google Maps, (3) la mise a jour des champs personnalises de geocodage sur les beans SuiteCRM.

**Type :** model

---

## Dependances cles
- `modules/jjwg_Maps/jjwg_Maps_sugar.php` — classe parente ORM
- `modules/Administration/Administration.php` — lecture/ecriture de la configuration admin (`jjwg_*`)
- `BeanFactory` — creation de beans (Administration, jjwg_Address_Cache)
- `$GLOBALS['sugar_config']` — limite de ressources
- API Google Maps Geocoding (cURL HTTP vers `geocoding_api_url`)
- `jjwg_Address_Cache` — cache des geocodages

---

## Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `jjwg_Maps` | Classe | Bean + moteur de geocodage |
| `$settings` | Propriete | Tableau de configuration complet (valeurs par defaut + admin) |
| `configuration()` | Methode | Charge les settings admin, peuple `$GLOBALS['jjwg_config']` et `$GLOBALS['jjwg_config_defaults']` |
| `saveConfiguration($data)` | Methode | Sauvegarde les settings via `Administration::saveSetting()` |
| `updateGeocodeInfo(&$bean)` | Methode | Met a jour `jjwg_maps_lat_c/lng_c/address_c/geocode_status_c` avant sauvegarde (hook before_save) |
| `updateRelatedMeetingsGeocodeInfo(&$bean)` | Methode | Propage le geocodage aux reunions liees au bean (hook after_save) |
| `updateMeetingGeocodeInfo(&$bean)` | Methode | Met a jour le geocodage d'une reunion apres sauvegarde (after_save) |
| `updateGeocodeInfoByAssocQuery($table, $display, $aInfo)` | Methode | UPDATE/INSERT SQL sur `{table}_cstm` pour les champs geocodage |
| `updateGeocodeInfoByBeanQuery(&$bean, $aInfo)` | Methode | Idem via bean |
| `deleteAllGeocodeInfoByBeanQuery(&$bean)` | Methode | Reset (NULL) des champs geocodage pour tout un module |
| `getGeocodeAddressesResult($table, $limit, $id)` | Methode | SELECT des enregistrements non geocodes (lat=0 ou NULL) |
| `getGoogleMapsGeocode($address, $return_full_array, $allow_approximate)` | Methode | Appel cURL a l'API Google Maps Geocoding, retourne `['address','status','lat','lng']` |
| `defineMapsAddress($object_name, $display)` | Methode | Determine l'adresse a geocoder selon le type de module et les relations |
| `defineMapsFormattedAddress($display, $type)` | Methode | Formate une adresse concatenee a partir des champs billing/shipping/primary/alt/address |
| `is_valid_lng($lng)` | Methode | Valide une longitude |
| `is_valid_lat($lat)` | Methode | Valide une latitude |
| `logGeocodeInfo($bean)` | Methode | Log filtre des informations de geocodage du bean |
| `getProspectLists()` | Fonction globale | Retourne un tableau id=>name des listes de prospects |

---

## Interactions
- **Appelle :** API Google Maps (cURL), `jjwg_Address_Cache`, `Administration`
- **Appele par :** `jjwg_MapsController`, logics hooks (before_save/after_save) des modules Accounts, Contacts, Leads, etc., `jjwg_Areas::configuration()`, `jjwg_Markers::configuration()`
- **Peuple :** `$GLOBALS['jjwg_config']` et `$GLOBALS['jjwg_config_defaults']` utilises par toutes les vues

---

## Notes
- Les modules geocodables par defaut : Accounts, Contacts, Leads, Opportunities, Cases, Project, Meetings, Prospects (ligne 62-65).
- Seuil anti-quota : `google_geocoding_limit` (defaut 100 requetes/batch), `geocoding_limit` (defaut 250 enregistrements).
- `logic_hooks_enabled` est `false` par defaut (ligne 194) — les hooks de geocodage automatique sont desactives par defaut.
- La methode `defineMapsAddress()` contient une logique de traversal de relations complexe (Opportunity->Account, Case->Account, Project->Account/Opportunity->Account, Meeting->flex_relate).
- `APPROXIMATE` est considere comme un echec si `allow_approximate_location_type` est false.
- Attention : `deleteAllGeocodeInfoByBeanQuery` met a NULL TOUTES les lignes de la table `{module}_cstm` (WHERE 1=1, ligne 838).
