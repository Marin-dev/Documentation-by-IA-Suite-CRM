# 📄 Scheduler.php

**Chemin :** `modules/Schedulers/Scheduler.php`
**Type :** PHP — Modèle (SugarBean) / Planificateur
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Représente un planificateur de tâche périodique (équivalent cron). Chaque instance définit une tâche à exécuter (fonction PHP ou URL), son intervalle (format cron étendu `min::hr::dates::mon::days`), ses plages horaires (`time_from`, `time_to`) et son statut (Active/Inactive). Vérifie si une tâche est qualifiée pour s'exécuter à l'instant T.

## ⚙️ Rôle technique
Étend `SugarBean`, table `schedulers`. `fireQualified()` parse l'intervalle cron et vérifie si l'heure courante correspond. `checkPendingJobs()` parcourt tous les schedulers actifs et soumet les jobs qualifiés dans la queue via `SugarJobQueue`. `createJob()` instancie un `SchedulersJob` prêt à être exécuté. `initUser()` récupère l'utilisateur admin (ID 1 par défaut) pour exécuter les jobs.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `SchedulersJob` (`modules/SchedulersJobs/SchedulersJob.php`) — bean de la file de jobs
  - `BeanFactory` — instanciation users/jobs
  - `DBManagerFactory` — requêtes admin user
  - `TimeDate` — heure courante
  - `SugarJobQueue` — file de jobs (INCONNU exact)
- **Table DB :** `schedulers`
- **Champs clés :** `job` (target), `job_interval` (cron), `status`, `date_time_start/end`, `time_from/to`, `catch_up`

## 📤 Sorties / Exports
- `Scheduler` — classe planificateur
- `fireQualified(): bool` — vérifie si le scheduler doit s'exécuter maintenant
- `checkPendingJobs(SugarJobQueue $queue)` — soumet les jobs qualifiés
- `createJob(): SchedulersJob` — crée un job à partir de ce scheduler
- `deriveDBDateTimes(Scheduler): array|false` — calcule les datetimes valides selon l'intervalle cron
- `initUser(): User|false` — statique — récupère l'admin pour exécution
- **Consommateurs identifiés :** `cron.php` ou `SugarJobQueue` (INCONNU exact)

## 🔗 Relations clés
- **Appelé par :** Processus cron système (INCONNU exact)
- **Appelle :** `SchedulersJob`, `SugarJobQueue::submitJob()`
- **Position dans le flux global :** Déclencheur de la file de jobs planifiés

---

## 💡 Points d'attention
- `deriveDBDateTimes()` est un parseur de cron maison complexe — format `min::hr::dates::mon::days` différent du cron Unix standard (5 champs avec `::` comme séparateur).
- Si aucun admin (ID 1) n'existe, fallback sur le premier admin actif — si aucun, retourne `false` et log fatal.
- `catch_up` : comportement INCONNU (champ présent mais logique non visible dans l'extrait lu).
