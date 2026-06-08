# install.php

**Chemin :** `install.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle fonctionnel

Assistant d'installation interactif de SuiteCRM. Orchestre le workflow multi-étapes permettant de configurer la base de données, les paramètres du site, et d'initialiser le schéma complet. Supporte également l'installation silencieuse via `config_si.php`.

**Type :** entrypoint (installeur)

## Rôle technique

Gère un workflow de pages PHP (`$workflow` array) avec navigation Suivant/Précédent via `$_REQUEST['goto']`. Chaque étape valide et stocke les données en session. Charge dynamiquement les fichiers de l'installateur (`install/*.php`). Supporte deux modes : interactif (wizard) et silencieux (`SilentInstall` via `config_si.php`).

---

## Dépendances clés

- **Imports principaux :**
  - `include/utils.php` — utilitaires généraux (`check_php_version`, `clean_string`…)
  - `sugar_version.php` / `suitecrm_version.php` — versions de l'application
  - `install/install_utils.php` — fonctions de l'installateur (`validate_dbConfig`, `validate_siteConfig`…)
  - `install/install_defaults.php` — valeurs par défaut de l'installation
  - `include/TimeDate.php` — gestion des dates
  - `include/Localization/Localization.php` — localisation
  - `include/SugarTheme/SugarTheme.php` — gestion du thème
  - `data/SugarBean.php` — base ORM
  - `include/entryPoint.php` — environnement SuiteCRM
  - `jssource/minify.php` — minification JS (pour installation non-silencieuse)
- **Paramètres d'entrée ($_REQUEST) :**
  - `goto` — navigation (`LBL_NEXT`, `LBL_BACK`, `SilentInstall`, `oc_convert`)
  - `current_step` — index de l'étape courante
  - `install_type` — `custom` pour installation personnalisée
  - `language` — langue sélectionnée par l'utilisateur
  - `checkInstallSystem`, `checkDBSettings`, `storeConfig`, `uploadLogo` — appels AJAX partiels
- **Configuration :**
  - `$sugar_config['installer_locked']` — bloque l'installateur post-installation (sécurité critique)

## Workflow des étapes

| Fichier | Rôle |
|---|---|
| `old_php.php` | Avertissement version PHP non recommandée (conditionnel) |
| `welcome.php` | Page d'accueil, acceptation licence |
| `ready.php` | Vérification prérequis |
| `installConfig.php` | Config DB + site (étape principale) |
| `performSetup.php` | Exécution de l'installation |
| `complete_install.php` | Confirmation de fin |

## Relations clés

- **Appelé par :** navigateur web lors de la première installation
- **Appelle :** fichiers sous `install/` via `require($the_file)`, avec hooks `installerHook('pre_installFileRequire')` et `installerHook('post_installFileRequire')`

---

## Points d'attention

- **Sécurité critique :** `installer_locked` doit être `true` en production (sinon l'installateur reste accessible et peut réinitialiser la base).
- L'upload du logo d'entreprise est validé par type MIME (`exif_imagetype`) mais stocké dans `custom/` (ligne 251).
- L'installation silencieuse lit `config_si.php` (non versionné) et redirige automatiquement.
- La session est utilisée intensivement pour stocker l'état entre les étapes — des données de configuration sensibles (mot de passe admin) y transitent.
- `make_writable` et `recursive_make_writable` sont appelés sur plusieurs répertoires lors de l'installation silencieuse — nécessite des permissions OS adéquates.
