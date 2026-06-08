# BuildCommands.php

**Chemin :** `lib/Robo/Plugin/Commands/BuildCommands.php`
**Type :** PHP — Commandes Robo CLI
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Commandes Robo pour la compilation des themes CSS (SASS) de SuiteCRM. Permet de compiler le theme SuiteP ou tout autre theme avec des schemas de couleurs specifiques.

## Role technique
Etend `Robo\Tasks` + `RoboTrait`. Utilise `pscss` (vendor Composer) pour la compilation SCSS. Detecte automatiquement les sous-themes disponibles via parcours du dossier `themes/`. La compatibilite OS est geree par `OperatingSystem::toOsPath()`.

---

## Dependances cles
- `Robo\Tasks`
- `SuiteCRM\Utility\OperatingSystem` — conversion des chemins OS
- `SuiteCRM\Robo\Traits\RoboTrait`

## Exports / Symboles principaux
- `BuildCommands` — classe commandes Robo
  - `buildTheme(array $opts): void` — compile un theme SCSS (`--theme=SuiteP --color-scheme=Dawn`)
  - `buildSuiteP(array $opts): void` — raccourci pour SuiteP

## Relations cles
- **Appele par :** CLI Robo (`./vendor/bin/robo build:theme`)
- **Appelle :** `OperatingSystem`, `./vendor/bin/pscss`
- **Position dans le flux global :** etape de build front-end (pre-production)

---

## Points d'attention
- `buildColorScheme()` efface `style.css` s'il existe avant de recompiler (ligne 132).
- Necessite `vendor/bin/pscss` installe via Composer.
