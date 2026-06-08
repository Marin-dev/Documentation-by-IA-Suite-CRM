# CalendarSyncJobFactory.php

**Chemin :** `include/CalendarSync/infrastructure/jobs/CalendarSyncJobFactory.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Fabrique de jobs pour la file du scheduler SuiteCRM. Cree des jobs de type "compte" (synchronisation complete d'un compte calendrier) ou de type "reunion" (synchronisation d'un evenement individuel). Permet egalement de recuperer l'instance du scheduler associe a CalendarSync.

## Role technique

Utilise `SugarJobQueue` pour soumettre les jobs. Les jobs de reunion sont serialises via `CalendarSyncOperationSerializer` pour encoder l'operation dans le champ `data` du job. Cree des beans `SchedulersJobs` via `BeanFactory` avec statut `QUEUED` et resolution `PENDING`. Lazy-initialise la queue (`$queue` est cree a la premiere soumission).

---

## Dependances cles

- **Imports principaux :**
  - `SugarJobQueue` (`include/SugarQueue/SugarJobQueue.php`) — file de jobs
  - `CalendarSyncOperationSerializer` — serialisation de l'operation pour le champ data
  - `JobStatusHelper` — noms de jobs et cibles (constants)

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `CalendarSyncJobFactory` | classe fabrique | Creation de jobs scheduler |
| `createAccountJob(string): ?string` | methode | Job de sync d'un compte (retourne job ID) |
| `createMeetingJob(CalendarSyncOperation): ?string` | methode | Job de sync d'une reunion (retourne job ID) |
| `getScheduler(): ?Scheduler` | methode | Instance du scheduler CalendarSync |

- **Consommateurs identifies :** `CalendarSyncOrchestrator`, `CalendarSync::getScheduler()`

## Relations cles

- **Appele par :** `CalendarSyncOrchestrator::createAsyncAccountJob()`, `CalendarSyncOrchestrator::syncEvent()` (mode async)
- **Appelle :** `SugarJobQueue::submitJob()`, `BeanFactory::newBean('SchedulersJobs')`, `CalendarSyncOperationSerializer::serialize()`
- **Position dans le flux global :** infrastructure de soumission des jobs asynchrones

---

## Points d'attention

- `createAccountJob()` lit le `calendar_user_id` du compte pour assigner le job — si le compte n'existe pas, utilise `'1'` (admin) par defaut (ligne 93). Potentiel job sans bon contexte utilisateur.
- En cas d'echec de `submitJob()`, retourne `null` sans relancer d'exception — l'appelant doit verifier la valeur de retour.
- `getScheduler()` cherche un scheduler existant non-supprime avec la cle `JobStatusHelper::SCHEDULER_JOB` — si absent, retourne `null` sans en creer un.
