# siteConfig_a.php

**Chemin :** `install/siteConfig_a.php`
**Type :** `PHP (installeur — configuration site étape A)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Initialise les variables de session pour la configuration du site à partir de la configuration existante (`config.php`) si elle est présente. Prépare les paramètres de langue, thème, charset, devise, et charge les scénarios d'installation disponibles.

**Type :** installer (logique de session)

---

## Dépendances clés
- `sugarEntry` + `$install_script` — protections
- `config.php` — configuration SuiteCRM existante (si présente)
- `$sugar_config` — tableau de configuration global
- `install/suite_install/scenarios.php` — scénarios d'installation
- `$mod_strings`, `$validation_errors` — globaux wizard

## Exports / Symboles principaux
Aucun. Peuple `$_SESSION` avec les paramètres de configuration du site.

Paramètres session initialisés :
- `$_SESSION['site_default_theme']`
- `$_SESSION['default_language']`
- `$_SESSION['default_charset']`
- `$_SESSION['default_currency_name/symbol/iso4217']`
- `$_SESSION['installation_scenarios']`
- `$_SESSION['setup_site_sugarbeet']`, `setup_site_defaults`
- `$_SESSION['setup_site_custom_session_path']`, `setup_site_custom_log_dir`, `setup_site_specify_guid`

## Interactions
- **Appelé par :** `install.php` avant l'affichage de l'étape de configuration du site (ancienne version du wizard)
- **Appelle :** `require_once('install/suite_install/scenarios.php')`
- **Position dans le flux global :** initialisation de session pour l'étape de configuration du site (wizard ancien)

---

## Notes
- Ce fichier fait partie de l'ancien wizard (pattern `siteConfig_a/b`). La nouvelle version est dans `installConfig.php`.
- Le chargement de `config.php` est conditionnel (`is_file("config.php")`) — pré-remplit les champs si SuiteCRM est déjà installé.
- Les langues disponibles sont encodées en session via `urlencode(implode(",", ...))` pour transmission entre pages (lignes 1636-1638).
