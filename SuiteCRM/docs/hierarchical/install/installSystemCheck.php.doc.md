# installSystemCheck.php

**Chemin :** `install/installSystemCheck.php`
**Type :** `PHP (installeur — vérification système)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Effectue la vérification des prérequis système lors de l'installation : version PHP, mémoire disponible, extensions PHP requises, permissions fichiers, configuration du serveur web (IIS/FastCGI, etc.). Retourne le HTML du rapport de vérification.

**Type :** installer

---

## Dépendances clés
- `$install_script` + `$mod_strings` — protections et messages
- `installLog()` — journalisation
- Constantes : `SUGARCRM_MIN_MEM` (40 Mo), `SUITECRM_PHP_MIN_VERSION`, `SUITECRM_PHP_REC_VERSION`
- `$_SERVER['SERVER_SOFTWARE']` — détection serveur web
- `php_sapi_name()`, `ini_get()` — inspection de l'environnement PHP
- `include/Imap/ImapHandlerFactory.php` — vérification IMAP (dans `ready.php`)

## Exports / Symboles principaux
- `runCheck(bool $install_script, array $mod_strings = []) : string` — exécute toutes les vérifications et retourne le HTML du rapport. Met `$_SESSION['setup_license_accept'] = true` si toutes les vérifications passent.

## Interactions
- **Appelé par :** `install.php` (étape de vérification prérequis)
- **Position dans le flux global :** étape 1 du wizard (avant la licence)

---

## Notes
- `$error_found` : si `true`, le bouton "Suivant" est désactivé dans la vue — l'utilisateur ne peut pas continuer.
- Détection IIS + FastCGI avec `fastcgi.logging != 0` : erreur bloquante (ligne 74-78).
- Constante `SUGARCRM_MIN_MEM = 40` Mo minimum PHP.
