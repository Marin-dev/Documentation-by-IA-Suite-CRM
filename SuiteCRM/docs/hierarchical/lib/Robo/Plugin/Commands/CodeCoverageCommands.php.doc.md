# CodeCoverageCommands.php

**Chemin :** `lib/Robo/Plugin/Commands/CodeCoverageCommands.php`
**Type :** PHP — Commandes Robo CLI
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Commande Robo pour generer un rapport de couverture de code via PHPUnit. Supporte les environnements CI (Travis CI).

## Role technique
Detecte l'environnement via `getenv('TRAVIS')` et `getenv('TRAVIS_COMMIT_RANGE')`. Execute PHPUnit avec `--coverage-clover` vers `tests/_output/coverage.xml`. Utilise `OperatingSystem::toOsPath()` pour la compatibilite multi-OS.

---

## Dependances cles
- `Robo\Tasks`
- `SuiteCRM\Utility\OperatingSystem`
- `SuiteCRM\Robo\Traits\RoboTrait`

## Exports / Symboles principaux
- `CodeCoverageCommands` — classe commandes Robo
  - `codeCoverage($opts): void` — option `--ci` pour CI

## Relations cles
- **Appele par :** CLI Robo ou pipeline CI
- **Appelle :** `./vendor/bin/phpunit --configuration ./tests/phpunit.xml.dist`

---

## Points d'attention
- Variable d'environnement utilisee : `TRAVIS`, `TRAVIS_COMMIT_RANGE`.
- Le `getCommitRangeForTravisCi()` est appele mais `$range` n'est jamais utilise dans `generateCodeCoverageFile()` (ligne 65) — dead code potentiel.
