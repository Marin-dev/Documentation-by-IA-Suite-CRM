# fp_events_fp_event_delegates_1MetaData.php

**Chemin :** `metadata/fp_events_fp_event_delegates_1MetaData.php`
**Type :** config (métadonnées de table de jointure événements-délégués)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `fp_events_fp_event_delegates_1_c` qui matérialise la relation entre les événements (`FP_events`) et les délégués d'événement (`FP_Event_delegates`). Permet d'associer des délégués à un événement.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['fp_events_fp_event_delegates_1']` | variable globale PHP | Définition de la table de jointure |

### Structure de la table `fp_events_fp_event_delegates_1_c`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `date_modified` | datetime | Horodatage |
| `deleted` | bool(1) | Soft delete |
| `fp_events_fp_event_delegates_1fp_events_ida` | varchar(36) | FK vers `fp_events.id` |
| `fp_events_fp_event_delegates_1fp_event_delegates_idb` | varchar(36) | FK vers `fp_event_delegates.id` |

### Relation

- **Type déclaré :** `true_relationship_type = one-to-many` (un événement → plusieurs délégués)
- **LHS :** module `FP_events`, table `fp_events`, clé `id`
- **RHS :** module `FP_Event_delegates`, table `fp_event_delegates`, clé `id`

## Notes

- Généré par Studio le 2013-04-30.
- Table custom (suffixe `_c`).
