# TestRunCommands.php

**Chemin :** `lib/Robo/Plugin/Commands/TestRunCommands.php`
**Type :** PHP — Commandes Robo CLI
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Commandes Robo pour lancer les differentes suites de tests de SuiteCRM (install, API, acceptance, unit) via Codecept et PHPUnit.

## Role technique
Quatre methodes correspondant a quatre types de tests. Chaque methode construit une commande shell et l'execute via `$this->_exec()`. Supporte le mode debug (`-vvv -d`) et l'arret sur premier echec (`--fail-fast`).

---

## Dependances cles
- `Robo\Tasks`
- `Symfony\Console\Input\InputOption`
- `SuiteCRM\Robo\Traits\RoboTrait`

## Exports / Symboles principaux
- `TestRunCommands` — classe commandes Robo
  - `TestsInstall(string $fileOrDirectory, array $opts)` — suite install (Codecept)
  - `TestsAPI(string $fileOrDirectory, array $opts)` — suite API (Codecept)
  - `TestsAcceptance(string $fileOrDirectory, array $opts)` — suite acceptance (Codecept)
  - `TestsUnit(string $fileOrDirectory, array $opts)` — suite unit (PHPUnit)

## Relations cles
- **Appele par :** CLI Robo (`./vendor/bin/robo tests:*`)
- **Appelle :** `./vendor/bin/codecept`, `./vendor/bin/phpunit`

---

## Points d'attention
- Les suites install, acceptance utilisent `--env custom` de Codecept.
- L'option `--filter` (PHPUnit) est disponible pour `TestsUnit` (ligne 146).
