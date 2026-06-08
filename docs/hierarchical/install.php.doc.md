# install.php

**Chemin :** `install.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-28

---

## Rôle
Assistant d'installation web de SuiteCRM. Orchestre le workflow multi-étapes d'installation initiale (ou de mise à jour), gère l'installation silencieuse via fichier `config_si.php`, et protège l'accès si l'installateur est verrouillé.

## Responsabilités
- Vérifier la version PHP minimale avant tout traitement (bloque l'installation si EOL)
- Gérer la session d'installation et détecter le mode "silent install" (`config_si.php`)
- Définir et parcourir un workflow ordonné de pages d'installation : `welcome.php`, `ready.php`, `installConfig.php`, `performSetup.php`, `complete_install.php`
- Persister les données de configuration dans `$_SESSION` à chaque étape
- Valider les configurations DB (`validate_dbConfig`) et site (`validate_siteConfig`)
- Gérer l'upload du logo entreprise, la vérification système (`installSystemCheck`), et le check DB (`checkDBSettings`) via AJAX
- Appeler les hooks `pre_installFileRequire` / `post_installFileRequire` à chaque chargement de page d'installation
- Bloquer l'accès si `$sugar_config['installer_locked'] == true`

## Dépendances internes
- `include/utils.php` — utilitaires généraux (`check_php_version`, `clean_string`…)
- `sugar_version.php` / `suitecrm_version.php` — versions de l'application
- `install/install_utils.php` — fonctions d'installation (`validate_dbConfig`, `validate_siteConfig`, `setPhpIniSettings`…)
- `install/install_defaults.php` — valeurs par défaut de l'installateur
- `include/entryPoint.php` — bootstrap partiel
- `include/SugarLogger/LoggerManager.php` — logger
- `include/TimeDate.php`, `include/Localization/Localization.php`, `include/SugarTheme/SugarTheme.php`
- `data/SugarBean.php`
- `jssource/minify.php` — minification JS (chargé en mode non-silencieux ou silent install)
- `install/installSystemCheck.php`, `install/checkDBSettings.php` — vérifications AJAX

## Exports / Points d'entrée
- **Point d'entrée HTTP :** `GET|POST /install.php`
- Paramètres clés : `goto` (navigation), `current_step`, `language`, `setup_db_*`, `setup_site_*`
- Fonction locale : `getSupportedInstallLanguages()` — retourne les langues disponibles

## Notes techniques
- Le mode "silent install" (`goto=SilentInstall` ou présence de `config_si.php`) saute l'interface graphique et effectue l'installation en une seule passe programmatique.
- Le workflow est un tableau PHP simple (`$workflow`), navigué par index ; les étapes peuvent être sautées conditionnellement.
- La vérification de session (test `$_SESSION['test_session']`) au step `welcome.php` détecte les problèmes de configuration PHP.
- Risque : les variables `$_SESSION` accumulent toute la configuration DB y compris le mot de passe admin en clair pendant l'installation.
- `installer_locked` dans `config.php` est le verrou de production — doit être `true` après installation.
