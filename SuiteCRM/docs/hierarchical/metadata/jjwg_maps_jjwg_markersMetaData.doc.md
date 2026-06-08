# jjwg_maps_jjwg_markersMetaData.php

**Chemin :** `metadata/jjwg_maps_jjwg_markersMetaData.php`
**Type :** config (métadonnées de table de jointure cartographie)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `jjwg_maps_jjwg_markers_c` qui matérialise la relation many-to-many entre les cartes (`jjwg_Maps`) et les marqueurs (`jjwg_Markers`) du module de cartographie JJW Google Maps.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['jjwg_maps_jjwg_markers']` | variable globale PHP | Définition de la table de jointure |

### Structure de la table `jjwg_maps_jjwg_markers_c`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `date_modified` | datetime | Horodatage |
| `deleted` | bool(1) | Soft delete |
| `jjwg_maps_b229wg_maps_ida` | varchar(36) | FK vers `jjwg_maps.id` |
| `jjwg_maps_2e31markers_idb` | varchar(36) | FK vers `jjwg_markers.id` |

### Relation

- **Type :** many-to-many
- **LHS :** module `jjwg_Maps`, table `jjwg_maps`, clé `id`
- **RHS :** module `jjwg_Markers`, table `jjwg_markers`, clé `id`

## Notes

- Généré en 2010-11-12. Structure identique à `jjwg_maps_jjwg_areas`.
- Noms de colonnes avec hachage tronqué (`b229`, `2e31`).
