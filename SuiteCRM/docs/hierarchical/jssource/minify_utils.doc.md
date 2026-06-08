# Fichier : minify_utils.php

**Chemin :** `jssource/minify_utils.php`
**Type :** build (bibliotheque utilitaires JS)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Fournit toutes les fonctions utilitaires du pipeline de minification JavaScript de SuiteCRM : concatenation, compression, sauvegarde, restauration et exclusion de fichiers.

## Role technique
Bibliotheque de fonctions pures incluse par `minify.php` et d'autres points d'entree. Depend de `SugarMin::minify()` pour la minification effective.

---

## Dependances cles
- **Imports principaux :**
  - `jssource/SugarMin.php` (via `CompressFiles()`, ligne 254) — minificateur
  - `jssource/JSGroupings.php` (via `ConcatenateFiles()`, ligne 95) — groupes JS
  - `include/utils/sugar_file_utils.php` — `sugar_fopen()`, `sugar_chmod()`, `sugar_mkdir()`
  - `include/dir_inc.php` — `mkdir_recursive()`
- **Variables d'environnement :** aucune
- **Garde :** `sugarEntry` requise (ligne 1)

## Exports / Symboles principaux

| Fonction | Role |
|---|---|
| `get_exclude_files($prefix)` | Retourne la liste des dossiers/fichiers exclus de la minification |
| `ConcatenateFiles($from_path)` | Concatene les fichiers JS selon `$js_groupings` vers le cache |
| `create_backup_folder($bu_path)` | Cree recursivement le dossier de sauvegarde |
| `CompressFiles($from_path, $to_path)` | Minifie un fichier JS source vers destination |
| `reverseScripts($from_path, $to_path)` | Restaure les JS minifies depuis les sources backup |
| `BackUpAndCompressScriptFiles($from_path, $to_path, $backup)` | Parcourt le repertoire, sauvegarde et compresse recursivement |

## Interactions
- **Appele par :**
  - `jssource/minify.php`
  - INCONNU : potentiellement par des scripts d'administration SuiteCRM
- **Appelle :**
  - `SugarMin::minify()` — compression JS
  - `sugar_cached()` — chemin du cache
  - `sugar_die()` — arret avec message d'erreur

---

## Notes
- Les fichiers exclus incluent : `cache/`, `vendor/`, `yui/`, `modules/Emails/`, `jssource/`, `upload/`, `jquery/` (ligne 62-74).
- `ConcatenateFiles()` fixe `max_execution_time` a 300 secondes (ligne 91) car l'operation peut etre longue.
- `CompressFiles()` preserve le commentaire de licence en tete de fichier (lignes 276-315).
- `BackUpAndCompressScriptFiles()` renomme (mv) les fichiers originaux vers le backup avant minification.
