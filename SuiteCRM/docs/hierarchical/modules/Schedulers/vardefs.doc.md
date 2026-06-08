# Fichier : vardefs.php

**Chemin :** `modules/Schedulers/vardefs.php`
**Type :** PHP — configuration (vardefs SugarCRM)
**Derniere mise a jour doc :** 2026-06-02

---

## Ce que ce fichier configure
Definit le schema des champs du module Schedulers pour le framework SugarCRM (types, labels, validation). Utilise par SugarCRM pour les vues, l'API et la validation des donnees.

## Parametres cles
- Table : `schedulers`
- Champs principaux : `name`, `job`, `job_interval`, `date_time_start`, `date_time_end`, `time_from`, `time_to`, `last_run`, `status`, `catch_up`
- Relations definies : subpanel vers `SchedulersJobs`

## Impacte par / impacte
- Consomme par le framework SugarCRM (BeanFactory, vues, API)
- Lie a `modules/Schedulers/Scheduler.php`

## Points d'attention
- INCONNU : contenu exact du fichier non lu en totalite (lecture tronquee). Se referer au fichier source pour les details complets des types de champs.
