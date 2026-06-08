# run_job.php

**Chemin :** `run_job.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle fonctionnel

Script CLI pour exécuter un job planifié SuiteCRM spécifique, identifié par son ID et son ID client. Permet l'exécution individuelle d'un job hors du cycle CRON normal (utile pour le débogage ou les relances manuelles).

**Type :** entrypoint (CLI uniquement)

## Rôle technique

Vérifie que l'exécution est en mode CLI, valide les deux arguments requis (`jobId` et `clientId`), initialise l'utilisateur système, puis appelle `SchedulersJob::runJobId($argv[1], $argv[2])`. Retourne `0` en cas de succès, `1` en cas d'échec.

---

## Dépendances clés

- **Imports principaux :**
  - `include/entryPoint.php` — initialisation complète de SuiteCRM
  - `modules/SchedulersJobs/SchedulersJob.php` — logique d'exécution des jobs
- **Arguments CLI :**
  - `$argv[1]` — ID du job à exécuter
  - `$argv[2]` — ID du client (processus cron)
- **Variables de configuration :**
  - `$sugar_config['default_language']` — langue pour les chaînes

## Sorties / Comportement

- Exécute `SchedulersJob::runJobId($argv[1], $argv[2])`
- Affiche un message d'erreur sur stdout si `$result` est une chaîne
- Code de sortie : `0` (succès) ou `1` (échec)
- Déconnecte explicitement la base de données après l'exécution

## Relations clés

- **Appelé par :** CLI manuellement ou potentiellement par le driver CRON pour lancer des jobs en sous-processus
- **Appelle :** `SchedulersJob::runJobId()`, `BeanFactory::newBean('Users')->getSystemUser()`

---

## Points d'attention

- **Réservé CLI uniquement** — tue le processus si appelé via HTTP (ligne 51).
- Requiert exactement 3 arguments (`$argv[0]` = nom script, `$argv[1]` = jobId, `$argv[2]` = clientId) — ligne 54.
- `chdir(__DIR__)` en ligne 44 garantit que les chemins relatifs fonctionnent quelle que soit la cwd.
- Pattern similaire à `cron.php` pour le nettoyage des ressources après exécution.
