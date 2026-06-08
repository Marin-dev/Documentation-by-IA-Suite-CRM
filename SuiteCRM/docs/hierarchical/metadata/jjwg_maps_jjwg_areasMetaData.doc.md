# jjwg_maps_jjwg_areasMetaData.php

**Chemin :** `metadata/jjwg_maps_jjwg_areasMetaData.php`
**Type :** config (métadonnées de table de jointure cartographie)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `jjwg_maps_jjwg_areas_c` qui matérialise la relation many-to-many entre les cartes (`jjwg_Maps`) et les zones géographiques (`jjwg_Areas`) du module de cartographie JJW Google Maps de SuiteCRM.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['jjwg_maps_jjwg_areas']` | variable globale PHP | Définition de la table de jointure |

### Structure de la table `jjwg_maps_jjwg_areas_c`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `date_modified` | datetime | Horodatage |
| `deleted` | bool(1) | Soft delete |
| `jjwg_maps_5304wg_maps_ida` | varchar(36) | FK vers `jjwg_maps.id` |
| `jjwg_maps_41f2g_areas_idb` | varchar(36) | FK vers `jjwg_areas.id` |

### Relation

- **Type :** many-to-many
- **LHS :** module `jjwg_Maps`, table `jjwg_maps`, clé `id`
- **RHS :** module `jjwg_Areas`, table `jjwg_areas`, clé `id`

## Notes

- Généré en 2010-11-12. Module cartographique tiers intégré à SuiteCRM.
- Noms de colonnes avec hachage tronqué (`5304`, `41f2`).
