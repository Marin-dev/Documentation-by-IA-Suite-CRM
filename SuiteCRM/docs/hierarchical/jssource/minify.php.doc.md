# minify.php

**Chemin :** `jssource/minify.php`
**Type :** `PHP (point d'entrée build JS)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Script de build JavaScript à double mode d'exécution (CLI et requête HTTP). Il orchestre la minification et la concaténation de tous les fichiers JS de SuiteCRM selon les groupements définis dans `JSGroupings.php`. Depuis un navigateur (admin), il vérifie les fichiers modifiés et regroupe ; depuis la CLI, il supporte plusieurs modes (`-r`, `-m`, `-c`, `-mo`, `-co`).

**Type :** build

---

## Dépendances clés
- `jssource/minify_utils.php` — fonctions `ConcatenateFiles`, `BackUpAndCompressScriptFiles`, `reverseScripts`
- `jssource/JSGroupings.php` — tableau `$js_groupings`
- `include/utils/sugar_file_utils.php` — `sugar_cached()`
- `include/utils.php`, `include/utils/file_utils.php` — utilitaires fichiers
- `$_REQUEST['root_directory']` — chemin racine (mode navigateur)
- `$argv` — arguments CLI (mode ligne de commande)

## Exports / Symboles principaux
Aucune fonction ni classe exportée. Logique procédurale directe.

## Interactions
- **Appelé par :** admin SuiteCRM (outil "Réparer" → "Reconstruire les JS groupés") via requête HTTP, ou manuellement en CLI
- **Appelle :** `ConcatenateFiles()`, `BackUpAndCompressScriptFiles()`, `reverseScripts()`
- **Position dans le flux global :** déclencheur du pipeline de build JS complet

---

## Notes
- Mode CLI : `minify <root_path>` sans option = sauvegarde + compression + concaténation
- Option `-r` : restauration des sources originales depuis `jssource/src_files/`
- Option `-m` : restauration + minification
- Option `-c` : restauration + minification + concaténation
- Option `-mo` : minification uniquement (sans restauration)
- Option `-co` : concaténation uniquement
- Depuis le navigateur, seule l'action `rebuild` est autorisée (ligne 27).
