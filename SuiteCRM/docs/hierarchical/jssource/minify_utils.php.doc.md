# minify_utils.php

**Chemin :** `jssource/minify_utils.php`
**Type :** `PHP (utilitaires build JS)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Bibliothèque de fonctions utilitaires pour le pipeline de build JavaScript. Fournit les fonctions de concaténation, compression, sauvegarde et restauration des fichiers JS. Utilisée aussi bien depuis la CLI que depuis l'interface d'administration.

**Type :** build

---

## Dépendances clés
- `sugarEntry` — protection d'accès direct (ligne 1-4)
- `jssource/JSGroupings.php` — tableau `$js_groupings` (chargé dynamiquement)
- `jssource/SugarMin.php` — classe `SugarMin` pour la minification
- `include/utils/php_zip_utils.php`, `include/upload_file.php`
- `include/dir_inc.php` — `mkdir_recursive()`
- Fonctions Sugar : `sugar_cached()`, `sugar_fopen()`, `sugar_chmod()`, `sugar_mkdir()`

## Exports / Symboles principaux
- `get_exclude_files(string $prefix = '') : array` — retourne la liste des dossiers exclus de la minification (cache, vendor, yui, Emails, jssource, upload, ModuleBuilder, jquery, etc.)
- `ConcatenateFiles(string $from_path)` — concatène les fichiers sources JS en bundles selon `$js_groupings`, en minifiant chaque fichier au passage via `SugarMin::minify()`
- `create_backup_folder(string $bu_path)` — crée récursivement le dossier de sauvegarde dans `jssource/src_files/`
- `CompressFiles(string $from_path, string $to_path)` — lit un fichier JS, préserve l'en-tête de licence, minifie via `SugarMin::minify()` et écrit le résultat
- `reverseScripts(string $from_path, string $to_path = '')` — restaure les fichiers JS originaux depuis `jssource/src_files/`
- `BackUpAndCompressScriptFiles(string $from_path, string $to_path = '', bool $backup = true)` — parcourt récursivement les dossiers, sauvegarde et minifie tous les `.js` hors liste d'exclusion

## Interactions
- **Appelé par :** `jssource/minify.php`
- **Appelle :** `SugarMin::minify()`, `JSGroupings.php`, fonctions Sugar utilitaires
- **Position dans le flux global :** noyau du pipeline de build JS, entre la lecture des sources et l'écriture dans `cache/`

---

## Notes
- `ConcatenateFiles` utilise `$_REQUEST['root_directory']` pour choisir le chemin des includes : comportement différent selon l'origine HTTP vs CLI.
- Les fichiers déjà minifiés (suffixe `-min.js`) sont utilisés tels quels sans retraitement (ligne 111-115).
- En cas d'échec de création du dossier cible, `sugar_die()` est appelé avec un message explicatif (ligne 162-163).
- `BackUpAndCompressScriptFiles` avec `$backup = false` : utile en mode développement pour recompresser sans déplacer les sources.
