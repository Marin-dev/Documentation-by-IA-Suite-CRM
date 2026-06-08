# ModuleBuilderParser.php

**Chemin :** `modules/ModuleBuilder/parsers/ModuleBuilderParser.php`
**Type :** PHP (model / classe de base)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Classe de base pour les parsers de layouts ModuleBuilder. Fournit les méthodes utilitaires de lecture et d'écriture des fichiers de définition de vues (viewdefs), ainsi que la gestion des variables de module (format MB vs format standard).

## Type
model (classe abstraite de facto)

## Dépendances clés
- Fonctions globales : `mkdir_recursive()`, `sugar_fopen()`, `sugar_fclose()`, `var_export_helper()`, `sugar_cleanup()`

## Exports/Symboles principaux
- `ModuleBuilderParser` — classe
  - `_loadFromFile($view, $file, $moduleName)` — lit un fichier de viewdefs, normalise les clés module (MB vs standard), retourne `['viewdefs' => ..., 'variables' => ...]`
  - `_writeToFile($file, $view, $moduleName, $defs, $variables)` — écrit les viewdefs dans un fichier PHP
  - `_defMap` — mapping `[view => variableName]` (ex. `listview => listViewDefs`, `editview => viewdefs`)
  - `_fatalError($msg)` — log fatal + die

## Interactions
- **Héritée par :** `ParserDropDown`, `ParserLabel`, `ParserModifyLayoutView`, `ParserModifyListView`, `ParserSearchFields`
- **Appelle :** fonctions globales Sugar

## Notes
- `_loadFromFile()` gère le cas des modules MB où les viewdefs sont indexés sous `$packagekey_$moduleName` au lieu de `$moduleName`. Lignes 97-105.
- `_writeToFile()` gère deux formats d'écriture selon la présence de variables de module : avec `$module_name` variable (format MB) ou avec le nom de module littéral. Ligne 148.
