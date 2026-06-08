# CalendarSyncJobCleaner.php

**Chemin :** `include/CalendarSync/infrastructure/jobs/CalendarSyncJobCleaner.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Service d'annulation des jobs en attente obsoletes pour une operation de synchronisation de reunion. Quand un nouvel evenement de sync est soumis, annule les jobs precedents en file d'attente pour le meme evenement, evitant les conflits d'execution concurrente.

## Role technique

Interroge les `SchedulersJobs` via `get_full_list()` pour trouver les jobs en statut `QUEUED` correspondant a l'operation donnee, puis appelle `resolveJob(JOB_FAILURE, ...)` sur chacun pour les marquer comme annules.

---

## Dependances cles

- **Imports principaux :**
  - `CalendarSyncOperation` — operation de reference
  - `JobStatusHelper` — constantes de cibles et generation de noms

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `CalendarSyncJobCleaner` | classe service | Nettoyage des jobs obsoletes |
| `cancelPendingMeetingJobs(CalendarSyncOperation): int` | methode | Annule les jobs en attente, retourne le nombre annule |

- **Consommateurs identifies :** `CalendarSync::syncMeeting()` (mode async uniquement)

## Relations cles

- **Appele par :** `CalendarSync::syncMeeting()` avant `$this->orchestrator->syncEvent()`
- **Appelle :** `BeanFactory::newBean('SchedulersJobs')`, `$pendingJob->resolveJob()`
- **Position dans le flux global :** pre-traitement avant soumission d'un job de reunion prioritaire

---

## Points d'attention

- Utilise `get_full_list()` sans limite — peut etre couteux si de nombreux jobs en attente existent pour le meme evenement.
- Le `getPendingJobStatusCondition()` reference `job_queue.status` et `job_queue.deleted` — verifie que la table `job_queue` est bien celle utilisee par `SchedulersJob` (alias potentiel).
- `resolveJob(JOB_FAILURE, 'Job overwritten...')` marque les anciens jobs comme FAILURE — peut impacter des metriques de monitoring si surveille.
