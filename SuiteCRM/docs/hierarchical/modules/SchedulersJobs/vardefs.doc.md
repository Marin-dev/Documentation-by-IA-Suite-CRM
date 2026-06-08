# Fichier : vardefs.php

**Chemin :** `modules/SchedulersJobs/vardefs.php`
**Type :** PHP — configuration (vardefs SugarCRM)
**Derniere mise a jour doc :** 2026-06-02

---

## Ce que ce fichier configure
Definit le schema de la table `job_queue` pour le module SchedulersJobs. Champs principaux : `id`, `name`, `status`, `resolution`, `target` (URL ou fonction), `data`, `execute_time`, `scheduler_id`, `retry_count`, `failure_count`, `assigned_user_id`, `client`.

## Parametres cles
| Champ | Type | Effet |
|---|---|---|
| `target` | varchar | Nom de la fonction ou `url::...` a executer |
| `status` | enum | queued / running / done |
| `resolution` | enum | success / failure / partial |
| `execute_time` | datetime | Heure d'execution prevue |
| `scheduler_id` | varchar | FK vers le scheduler parent |
| `retry_count` / `failure_count` | int | Gestion des echecs |
| `client` | varchar | ID client proprietaire du job |

## Impacte par / impacte
- Table : `job_queue`
- Consomme par `SchedulersJob.php`, `Scheduler.php`

## Points d'attention
- La table s'appelle `job_queue` (pas `schedulersjobs`) — point d'attention pour les requetes directes.
