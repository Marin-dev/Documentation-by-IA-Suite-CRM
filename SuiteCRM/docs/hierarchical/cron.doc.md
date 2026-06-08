# cron.php

**Chemin :** `cron.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle fonctionnel

Script CLI exécuté par le planificateur système (cron OS) pour déclencher le traitement des jobs planifiés SuiteCRM. Il gère la file d'attente des tâches périodiques (envoi d'emails, rapports, synchronisations, etc.).

**Type :** entrypoint (CLI uniquement)

## Rôle technique

Initialise l'environnement SuiteCRM, vérifie que l'exécution est bien en mode CLI et que l'utilisateur système est autorisé, puis instancie le driver de cron (par défaut `SugarCronJobs` ou personnalisé via `$sugar_config['cron_class']`) et appelle `runCycle()`. Nettoie les ressources et déconnecte la base de données à la fin.

---

## Dépendances clés

- **Imports principaux :**
  - `include/entryPoint.php` — initialisation complète de SuiteCRM
  - `include/utils.php` — fournit `getRunningUser()` et `is_windows()`
  - `include/SugarQueue/{cron_driver}.php` — driver de la file de jobs (ex: `SugarCronJobs`)
- **Variables de configuration :**
  - `$sugar_config['cron_class']` — nom du driver CRON (défaut : `SugarCronJobs`)
  - `$sugar_config['cron']['allowed_cron_users']` — liste blanche des utilisateurs autorisés à lancer cron
  - `$sugar_config['default_language']` — langue pour les chaînes applicatives

## Sorties / Comportement

- Exécute `$jobq->runCycle()` — traite un cycle de jobs en attente
- Retourne le code de sortie `0` (succès) ou `1` (échec) selon `$jobq->runOk()`
- Appelle `sugar_cleanup(false)` puis déconnecte explicitement la DB

## Relations clés

- **Appelé par :** crontab système (tâche planifiée OS)
- **Appelle :** `BeanFactory::newBean('Users')->getSystemUser()` (impersonne l'utilisateur système), `DBManagerFactory::getInstance()->disconnect()`
- **Override possible :** `custom/include/SugarQueue/{cron_class}.php` prioritaire sur `include/SugarQueue/`

---

## Points d'attention

- **Réservé CLI uniquement** — tue le processus si appelé via HTTP (ligne 52 : `sugar_die("cron.php is CLI only.")`).
- Sous Linux, vérifie l'utilisateur courant contre `allowed_cron_users` ; si la liste est absente de `config.php`, un avertissement est loggué mais l'exécution continue.
- L'exécution en tant que `root` est explicitement déconseillée (ligne 66) — utiliser le compte du serveur web.
- `sugar_cleanup()` peut être appelé une seconde fois par des jobs mal écrits ; la déconnexion DB explicite en ligne 109 compense ce cas.
