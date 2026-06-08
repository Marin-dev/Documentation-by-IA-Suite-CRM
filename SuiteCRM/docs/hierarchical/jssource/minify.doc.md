# Fichier : minify.php

**Chemin :** `jssource/minify.php`
**Type :** build / script CLI+HTTP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Point d'entree principal pour le pipeline de minification JavaScript de SuiteCRM. Peut etre invoque en ligne de commande (CLI) ou via le navigateur (HTTP). Coordonne la concatenation et la minification des fichiers JS selon les options passees.

## Role technique
Deux chemins d'execution selon l'environnement :
- **Via navigateur** (`$_REQUEST['root_directory']` presente) : recharge `JSGroupings.php` et `minify_utils.php`, compare les dates de modification des fichiers sources vs concatenes, et appelle `ConcatenateFiles()` si necessaire.
- **Via CLI** (`$argv[1]` = chemin racine) : charge les utilitaires, puis execute l'une des actions selon `$argv[2]` :
  - `-r` : `reverseScripts()` — restaure les sources depuis backup
  - `-m` : restaure + minifie
  - `-c` : restaure + minifie + concatene
  - `-mo` : minifie seulement les fichiers existants
  - `-co` : concatene seulement
  - (defaut) : `BackUpAndCompressScriptFiles()` + `ConcatenateFiles()`

---

## Dependances cles
- **Imports principaux :**
  - `jssource/minify_utils.php` — fonctions `ConcatenateFiles`, `BackUpAndCompressScriptFiles`, `reverseScripts`
  - `jssource/JSGroupings.php` — groupes de fichiers JS
  - `include/utils/sugar_file_utils.php` — `sugar_cached()`, `sugar_fopen()`
  - `include/utils.php`, `include/utils/file_utils.php` — utilitaires generaux
- **Variables d'environnement :** aucune
- **Arguments CLI :** `<root_path>` [-r|-m|-c|-mo|-co|-?]

## Exports / Symboles principaux
- Aucun export PHP — script executif uniquement

## Interactions
- **Appele par :** CLI ou appel HTTP depuis l'admin SuiteCRM (INCONNU : point d'entree admin exact)
- **Appelle :** `ConcatenateFiles()`, `BackUpAndCompressScriptFiles()`, `reverseScripts()`

---

## Notes
- La garde `sugarEntry` est definie localement (ligne 3) pour les appels CLI.
- `js_rebuild_concat=rebuild` est le parametre HTTP qui declenche la reconstruction.
- La fonction `sugar_cached()` est definie en fallback local (ligne 97-100) si non disponible.
