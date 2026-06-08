# run_job.php

**Chemin :** `run_job.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-28

---

## Rôle
Script CLI pour l'exécution individuelle d'un job planifié SuiteCRM. Invoqué par le démon de scheduler ou directement en ligne de commande pour lancer un job spécifique identifié par son ID et son client ID.

## Responsabilités
- Vérifier que l'exécution est en mode CLI uniquement (interdit en mode web)
- Valider la présence des arguments `$argv[1]` (job ID) et `$argv[2]` (client ID)
- Charger l'environnement SuiteCRM via `include/entryPoint.php`
- Récupérer l'utilisateur système (`getSystemUser`) comme contexte d'exécution
- Déléguer l'exécution du job à `SchedulersJob::runJobId($argv[1], $argv[2])`
- Gérer le résultat : afficher un message d'erreur si le job retourne une chaîne
- Appeler `sugar_cleanup()` puis déconnecter la DB explicitement
- Quitter avec le code de retour `0` (succès) ou `1` (échec)

## Dépendances internes
- `include/entryPoint.php` — bootstrap global
- `modules/SchedulersJobs/SchedulersJob.php` — classe `SchedulersJob`, méthode statique `runJobId()`
- `BeanFactory::newBean('Users')` + `getSystemUser()` — contexte utilisateur système

## Exports / Points d'entrée
- **CLI uniquement :** `php run_job.php {job_id} {client_id}`
- Code de sortie : `0` si succès, `1` si échec

## Notes techniques
- Le `chdir(__DIR__)` en début de script garantit que les chemins relatifs fonctionnent correctement quel que soit le répertoire de travail du processus appelant.
- La double déconnexion DB (via `sugar_cleanup` puis `DBManagerFactory::getInstance()->disconnect()`) est un contournement explicite documenté dans le code : certains jobs appellent `sugar_cleanup()` eux-mêmes, rendant la déconnexion principale inopérante.
- Ce script est le point d'intégration entre le planificateur OS (cron) et le moteur de jobs SuiteCRM.
