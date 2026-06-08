# vardefs.php (jjwg_Markers)

**Chemin :** `modules/jjwg_Markers/vardefs.php`
**Type :** PHP — configuration de schema
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Definit le schema de la table `jjwg_markers` : champs specifiques (coordonnees, icone) et relation vers jjwg_Maps.

**Type :** config

---

## Champs principaux

| Champ | Type | Role |
|---|---|---|
| city / state / country | varchar(255) | Localisation textuelle |
| jjwg_maps_lat | float(10,8) | Latitude du marqueur |
| jjwg_maps_lng | float(11,8) | Longitude du marqueur |
| marker_image | enum (marker_image_list) | Icone du marqueur (defaut: 'company') |
| jjwg_maps_jjwg_markers | link | Relation vers jjwg_Maps |

---

## Notes
- `optimistic_locking` active.
- Les icones referencees dans `marker_image_list` doivent exister dans `custom/themes/default/images/jjwg_Markers/{valeur}.png`.
