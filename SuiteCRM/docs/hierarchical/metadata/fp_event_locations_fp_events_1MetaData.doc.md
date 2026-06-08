# fp_event_locations_fp_events_1MetaData.php

**Chemin :** `metadata/fp_event_locations_fp_events_1MetaData.php`
**Type :** config (métadonnées de table de jointure événements-lieux)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `fp_event_locations_fp_events_1_c` qui matérialise la relation entre les lieux d'événements (`FP_Event_Locations`) et les événements (`FP_events`). Généré par Studio le 2013-04-25.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['fp_event_locations_fp_events_1']` | variable globale PHP | Définition de la table de jointure |

### Structure de la table `fp_event_locations_fp_events_1_c`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `date_modified` | datetime | Horodatage |
| `deleted` | bool(1) | Soft delete |
| `fp_event_locations_fp_events_1fp_event_locations_ida` | varchar(36) | FK vers `fp_event_locations.id` |
| `fp_event_locations_fp_events_1fp_events_idb` | varchar(36) | FK vers `fp_events.id` |

### Relation

- **Type déclaré :** `true_relationship_type = one-to-many` (un lieu → plusieurs événements)
- **LHS :** module `FP_Event_Locations`, table `fp_event_locations`, clé `id`
- **RHS :** module `FP_events`, table `fp_events`, clé `id`

## Notes

- Généré par Studio le 2013-04-25.
- Noms de colonnes très longs.
- Relation inverse à `fp_events_fp_event_locations_1` (même entités, sens inverse).
