# CodingStandardCommands.php

**Chemin :** `lib/Robo/Plugin/Commands/CodingStandardCommands.php`
**Type :** PHP — Commandes Robo CLI
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Commandes Robo pour verifier et corriger les standards de code PSR-2 de SuiteCRM via `php-cs-fixer`.

## Role technique
Trois commandes : correction complete, dry-run (verification sans modification), et correction des fichiers modifies (git diff). Utilise `Paths::getProjectPath()` pour les chemins absolus.

---

## Dependances cles
- `Robo\Tasks`
- `SuiteCRM\Robo\Traits\RoboTrait`
- `SuiteCRM\Utility\Paths` — chemins projet
- `./vendor/bin/php-cs-fixer` — outil de correction

## Exports / Symboles principaux
- `CodingStandardCommands` — classe commandes Robo
  - `stylePHPCSFixer(): void` — correction complete
  - `stylePHPCSFixerDryRun()` — verification seule
  - `stylePHPCSFixerModified(): void` — correction des fichiers git modifies

## Relations cles
- **Appele par :** CLI Robo ou pre-commit hooks
- **Appelle :** `php-cs-fixer`, `git diff`

---

## Points d'attention
- Utilise `.php_cs.dist` comme fichier de config php-cs-fixer.
- `stylePHPCSFixerModified()` cree un fichier temporaire `diff.txt` via Robo `taskTmpFile()`.
