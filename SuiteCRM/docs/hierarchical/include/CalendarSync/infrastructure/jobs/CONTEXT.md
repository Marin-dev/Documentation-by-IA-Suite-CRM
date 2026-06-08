# 📁 jobs

**Chemin :** `include/CalendarSync/infrastructure/jobs/`
**Profondeur :** 5
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient les classes d'infrastructure liées à la file de jobs scheduler de SuiteCRM pour la synchronisation calendrier asynchrone. Il couvre la création des jobs (compte ou réunion), le nettoyage des jobs obsolètes avant soumission d'un nouveau job, et la vérification des jobs actifs (anti-doublon).

## ⚙️ Responsabilité technique
Utilise `SugarJobQueue` pour soumettre des jobs au scheduler. `CalendarSyncJobFactory` crée les beans `SchedulersJobs` et les soumet. `CalendarSyncJobCleaner` annule les jobs en statut `QUEUED` obsolètes via `resolveJob(JOB_FAILURE)`. Dépend de `CalendarSyncOperationSerializer` pour encoder les opérations de réunion dans le champ `data` des jobs.

---

## 📂 Contenu

### Sous-dossiers
Aucun.

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `CalendarSyncJobFactory.php` | Fabrique de jobs scheduler (compte ou réunion) pour la sync asynchrone | [→ fiche](CalendarSyncJobFactory.doc.md) |
| `CalendarSyncJobCleaner.php` | Annulation des jobs en attente obsolètes avant soumission d'un nouveau job | [→ fiche](CalendarSyncJobCleaner.doc.md) |

### Fichiers non documentés (volontairement)
Aucun — `JobStatusHelper.php` (utilitaires de constantes et conditions SQL) n'a pas de fiche dans ce périmètre.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `SugarJobQueue`, `BeanFactory`, `CalendarSyncOperationSerializer`, `JobStatusHelper`
- **Expose :** création et gestion de jobs scheduler — consommés par `CalendarSyncOrchestrator` et `CalendarSync`
- **Flux typique :** En mode async, `CalendarSyncOrchestrator` appelle `CalendarSyncJobCleaner::cancelPendingMeetingJobs()` puis `CalendarSyncJobFactory::createMeetingJob()` pour soumettre un nouveau job à la file SugarJobQueue.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre comment un job de sync est créé | [`CalendarSyncJobFactory.php`](CalendarSyncJobFactory.doc.md) |
| Comprendre comment les jobs obsolètes sont nettoyés | [`CalendarSyncJobCleaner.php`](CalendarSyncJobCleaner.doc.md) |

---

## ⚠️ Zones INCONNU
- `CalendarSyncJobFactory` : si le compte n'existe pas, utilise `user_id = '1'` (admin) par défaut — potentiel job sans bon contexte utilisateur.
- `CalendarSyncJobCleaner` : `resolveJob(JOB_FAILURE, ...)` marque les anciens jobs comme FAILURE — peut impacter les métriques de monitoring.
- `JobStatusHelper` non documenté dans ce périmètre.
