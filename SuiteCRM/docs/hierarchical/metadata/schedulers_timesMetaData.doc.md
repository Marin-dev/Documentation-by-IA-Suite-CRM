# schedulers_timesMetaData.php

**Chemin :** `metadata/schedulers_timesMetaData.php`
**Type :** config (métadonnées de table de planification)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table `schedulers_times` qui enregistre les instances d'exécution planifiées des jobs du planificateur (`Schedulers`). Permet de suivre les dates d'exécution prévues et leur statut.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['SchedulersTimes']` | variable globale PHP | Définition de la table d'exécutions planifiées |

### Structure de la table `schedulers_times`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | id | Clé primaire UUID (requis) |
| `deleted` | bool | Soft delete (défaut : 0) |
| `date_entered` | datetime | Date de création de l'entrée (requis) |
| `date_modified` | datetime | Horodatage (requis) |
| `scheduler_id` | id | FK vers le planificateur (requis) |
| `execute_time` | datetime | Date d'exécution prévue (requis) |
| `status` | varchar(25) | Statut d'exécution (défaut : `ready`) |

### Index

| Nom | Type | Champs |
|---|---|---|
| `schedulers_timespk` | primary | `id` |
| `idx_scheduler_id` | index | `scheduler_id`, `execute_time` |

## Interactions

- **Appelé par :** module Schedulers, cron SuiteCRM
- **Appelle :** rien

## Notes

- `status = 'ready'` par défaut : INCONNU — valeurs possibles au-delà de `ready` (ex. `running`, `done`, `error`) à vérifier dans le module Schedulers.
- Index composite sur `(scheduler_id, execute_time)` : optimise la recherche des prochaines exécutions prévues.
