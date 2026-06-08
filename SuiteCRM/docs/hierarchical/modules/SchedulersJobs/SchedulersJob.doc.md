# 📄 SchedulersJob.php

**Chemin :** `modules/SchedulersJobs/SchedulersJob.php`
**Type :** PHP — Modèle (SugarBean) / Exécuteur de job
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Représente un job individuel dans la file d'exécution de SuiteCRM. Gère l'exécution effective des tâches planifiées (fonctions PHP, URLs via cURL, ou classes `RunnableSchedulerJob`), le cycle de vie du job (queued → running → done), la gestion des erreurs et les tentatives de reprise.

## ⚙️ Rôle technique
Étend `Basic`, table `job_queue`. `runJob()` dispatch selon le préfixe de `$target` : `function::`, `url::`, ou `class::`. Pour `function::`, charge `_AddJobsHere.php` et appelle la fonction. Pour `url::`, utilise cURL. Pour `class::`, instancie une classe implémentant `RunnableSchedulerJob`. `resolveJob()` gère succès/échec et la logique de retry.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `Basic` — classe parente
  - `modules/Schedulers/_AddJobsHere.php` — fonctions de jobs disponibles
  - `BeanFactory` — chargement user
  - `TimeDate` — gestion dates
- **Table DB :** `job_queue`
- **Constantes :** `JOB_STATUS_QUEUED/RUNNING/DONE`, `JOB_SUCCESS/FAILURE/PARTIAL/PENDING`

## 📤 Sorties / Exports
- `SchedulersJob extends Basic` — bean de job
- `RunnableSchedulerJob` — interface pour les jobs sous forme de classe
- `runJob(): bool` — exécute le job selon le type de target
- `resolveJob(string $resolution, ?string $message): bool` — termine le job (succès/échec)
- `failJob()` / `succeedJob()` / `postponeJob()` — helpers de résolution
- `fireUrl(string $job): bool` — exécution via cURL
- `runJobId(string $id, string $client): bool|string` — statique — exécute un job par ID
- `unexpectedExit()` — handler d'arrêt inattendu (register_shutdown_function)

## 🔗 Relations clés
- **Appelé par :** `Scheduler::createJob()`, processus worker de la file (INCONNU exact)
- **Appelle :** `_AddJobsHere.php` (fonctions PHP), cURL (URLs), `RunnableSchedulerJob::run()`
- **Position dans le flux global :** Exécuteur effectif de chaque tâche planifiée

---

## 💡 Points d'attention
- `sudo()` modifie `$GLOBALS['current_user']` et régénère la session — effets de bord importants sur l'environnement d'exécution.
- SSL désactivé pour cURL (`CURLOPT_SSL_VERIFYHOST/VERIFYPEER = false`) — risque sécurité en production.
- `unexpectedExit()` est enregistré via `register_shutdown_function` — garantit que le job est marqué Failed même sur crash.
- `min_interval` configurable via `sugar_config['jobs']['min_retry_interval']` (défaut 30 secondes).
