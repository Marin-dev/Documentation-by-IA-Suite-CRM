# install_utils.php

**Chemin :** `install/install_utils.php`
**Type :** `PHP (installeur — utilitaires)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Bibliothèque de fonctions utilitaires pour le processus d'installation. Fournit des helpers pour les hooks personnalisés, la journalisation, la gestion des packs de langue, l'upload de fichiers, la validation des configurations, la lecture de la licence, et de nombreuses opérations liées au wizard d'installation.

**Type :** installer

---

## Dépendances clés
- `sugarEntry` — protection d'accès
- `include/utils/php_zip_utils.php`, `include/upload_file.php`
- `custom/install/install_hooks.php` — hooks personnalisés optionnels
- `$GLOBALS['customInstallHooksExist']` — cache de présence des hooks
- `installLog()` — journalisation (INCONNU : définition dans ce fichier ou externe)

## Exports / Symboles principaux
- `installerHook(string $function_name, array $options = []) : mixed` — appelle une fonction dans `custom/install/install_hooks.php` si elle existe, retourne `'undefined'` sinon
- Autres fonctions utilitaires (non toutes lues) : probablement `installLog()`, `getLicenseContents()`, `getInstallDbInstance()`, `langPackUnpack()`, `getLangPacks()`, `getInstalledLangPacks()`, `commitModules()`, `uninstallLanguagePack()`, `removeLanguagePack()`, `get_language_header()`, `create_db_user_creds()` (INCONNU — fichier tronqué à 80 lignes)

## Interactions
- **Appelé par :**
  - `install/license.php` (ligne 56)
  - `install/licensePrint.php` (ligne 52)
  - `install/performSetup.php` (ligne 72)
  - `install/checkDBSettings.php` (implicitement via `installLog`, `getInstallDbInstance`)
  - `install/download_modules.php`
- **Appelle :** `custom/install/install_hooks.php` (si présent)
- **Position dans le flux global :** socle utilitaire du wizard d'installation

---

## Notes
- Pattern de hook personnalisé : le fichier `custom/install/install_hooks.php` peut étendre le comportement de l'installeur sans modifier le code core.
- `$GLOBALS['customInstallHooksExist']` est utilisé comme cache pour éviter de tester l'existence du fichier à chaque appel.
