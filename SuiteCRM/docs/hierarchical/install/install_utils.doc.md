# Fichier : install_utils.php

**Chemin :** `install/install_utils.php`
**Type :** installer (bibliotheque utilitaires)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Bibliotheque centrale de fonctions utilitaires pour le wizard d'installation de SuiteCRM. Couvre la gestion des hooks personnalises, des packs de langue, des patches/upgrades, la journalisation, la lecture de config, et les operations DB de setup.

## Role technique
Fichier de fonctions inclus par `install.php` et les autres composants du wizard. Requiert `sugarEntry`. Expose une API complete pour les operations d'installation : hooks, langues, patches, logs, config site, operations DB.

---

## Dependances cles
- **Imports principaux :**
  - `include/utils/php_zip_utils.php` — gestion ZIP (ligne 45)
  - `include/upload_file.php` — upload fichiers (ligne 46)
  - `custom/install/install_hooks.php` — hooks personnalises (optionnel)
  - `ModuleInstall/ModuleInstaller.php` — installation modules
  - `include/entryPoint.php` — point d'entree framework
- **Garde :** `sugarEntry` requise

## Exports / Symboles principaux (liste partielle — fichier tres long)

| Fonction | Role |
|---|---|
| `installerHook($function_name, $options)` | Appelle un hook personnalise depuis `custom/install/install_hooks.php` |
| `parseAcceptLanguage()` | Parse `HTTP_ACCEPT_LANGUAGE` en code langue normalise |
| `commitLanguagePack($uninstall)` | Installe ou desinstalle un pack de langue |
| `commitPatch($unlink, $type)` | Applique un patch ou upgrade via `ModuleInstaller` |
| `getLicenseContents($file)` | Lit le contenu de la licence |
| `get_language_header()` | Retourne l'attribut HTML `lang` selon la langue courante |
| `getInstallDbInstance()` | Retourne l'instance DB pour l'installation |
| `installLog($msg)` | Journalise un message dans le log d'installation |

## Interactions
- **Appele par :** `install.php`, `welcome.php`, `license.php`, `licensePrint.php`, `checkDBSettings.php`, `performSetup.php`, `populateSeedData.php`, et tous les fichiers du wizard
- **Appelle :**
  - `ModuleInstall/ModuleInstaller.php`
  - `DBManagerFactory::getInstance()`
  - `BeanFactory::newBean('Users')`
  - `writeSugarConfig()`

---

## Notes
- `installerHook()` permet d'etendre l'installation avec des hooks personnalises sans modifier le core (pattern extension).
- `commitLanguagePack()` gere l'installation ET la desinstallation des packs de langue (parametre `$uninstall`).
- `commitPatch()` supporte les scripts `pre_install.php` et `post_install.php` dans les zips de patch.
- Ce fichier est un point d'extension critique : tous les appels externes passent par ses fonctions.
