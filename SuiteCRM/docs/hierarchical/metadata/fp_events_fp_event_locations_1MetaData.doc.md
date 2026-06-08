# fp_events_fp_event_locations_1MetaData.php

**Chemin :** `metadata/fp_events_fp_event_locations_1MetaData.php`
**Type :** config (métadonnées de table de jointure événements-lieux)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `fp_events_fp_event_locations_1_c` qui matérialise la relation many-to-many entre les événements (`FP_events`) et les lieux d'événement (`FP_Event_Locations`). Relation symétrique à `fp_event_locations_fp_events_1`.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['fp_events_fp_event_locations_1']` | variable globale PHP | Définition de la table de jointure |

### Structure de la table `fp_events_fp_event_locations_1_c`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `date_modified` | datetime | Horodatage |
| `deleted` | bool(1) | Soft delete |
| `fp_events_fp_event_locations_1fp_events_ida` | varchar(36) | FK vers `fp_events.id` |
| `fp_events_fp_event_locations_1fp_event_locations_idb` | varchar(36) | FK vers `fp_event_locations.id` |

### Relation

- **Type :** many-to-many
- **LHS :** module `FP_events`, table `fp_events`, clé `id`
- **RHS :** module `FP_Event_Locations`, table `fp_event_locations`, clé `id`

## Notes

- Généré par Studio le 2013-04-24.
- Relation miroir de `fp_event_locations_fp_events_1MetaData.php` — les deux fichiers définissent la même relation physique depuis des points de vue différents.
