# 📄 _AddJobsHere.php

**Chemin :** `modules/Schedulers/_AddJobsHere.php`
**Type :** PHP — Registre des fonctions de jobs
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Registre central des fonctions de jobs planifiés disponibles dans SuiteCRM. Définit le tableau `$job_strings` listant toutes les fonctions disponibles dans le menu "Job" de l'interface admin Schedulers, et implémente ces fonctions.

## ⚙️ Rôle technique
Inclus par `SchedulersJob::runJob()` avant l'exécution de tout job de type `function::`. Le tableau `$job_strings` nourrit l'interface d'administration. Inclut également `NormalizeRecords` pour un job de normalisation.

---

## 📥 Entrées / Dépendances
- `NormalizeRecords` (`include/Services/NormalizeRecords/NormalizeRecords.php`)
- Toutes les fonctions doivent retourner un booléen
- Ne pas appeler `sugar_cleanup()` dans les fonctions

## 📤 Sorties / Exports
- `$job_strings` — tableau indexé des fonctions disponibles (0..N)
- Jobs référencés (partiels depuis l'extrait) : `refreshJobs`, `pollMonitoredInboxes`, `runMassEmailCampaign`, `pruneDatabase`, `trimTracker`, `pollMonitoredInboxesForBouncedCampaignEmails`, `pollMonitoredInboxesAOP`, `aodIndexUnindexed`, `aodOptimiseIndex`, `aorRunScheduledReports`, `processAOW_Workflow`, ...
- **Consommateurs identifiés :** `SchedulersJob::runJob()`, interface admin Schedulers

## 🔗 Relations clés
- **Appelé par :** `SchedulersJob::runJob()` pour les jobs `function::`
- **Position dans le flux global :** Bibliothèque de toutes les tâches planifiées disponibles

---

## 💡 Points d'attention
- Ce fichier est le point d'extensibilité pour ajouter de nouvelles tâches planifiées.
- Les personnalisations doivent aller dans `custom/modules/Schedulers/_AddJobsHere.php`.
- Ne jamais appeler `sugar_cleanup()` dans les fonctions — interromprait le processus cron.
