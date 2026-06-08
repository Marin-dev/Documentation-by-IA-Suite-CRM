# RoboTrait.php

**Chemin :** `lib/Robo/Traits/RoboTrait.php`
**Type :** PHP — Trait
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Trait utilitaire pour les commandes Robo. Fournit des helpers pour les prompts interactifs avec valeur par defaut, et pour lire la configuration SuiteCRM depuis la cle dotted-path.

## Role technique
Inclut `lib/Robo/config.php` au moment du chargement du fichier. Methodes :
- `askDefaultOptionWhenEmpty()` : prompt interactif seulement si `$option` est vide
- `chooseConfigOrDefault()` : lit une cle de config via `SugarConfig::getInstance()->get()`

---

## Dependances cles
- `lib/Robo/config.php` (require_once au niveau fichier)
- `SugarConfig` — singleton de configuration SuiteCRM

## Exports / Symboles principaux
- `RoboTrait` — trait
  - `askDefaultOptionWhenEmpty(string $question, string $default, &$option): void` (private)
  - `chooseConfigOrDefault(string $configKey, string $default): mixed` (private)

- **Consommateurs identifies :**
  - `lib/Robo/Plugin/Commands/ApiCommands.php`
  - `lib/Robo/Plugin/Commands/BuildCommands.php`
  - `lib/Robo/Plugin/Commands/CodeCoverageCommands.php`
  - `lib/Robo/Plugin/Commands/CodingStandardCommands.php`
  - `lib/Robo/Plugin/Commands/TestEnvironmentCommands.php`
  - `lib/Robo/Plugin/Commands/TestRunCommands.php`
  - `lib/Robo/Plugin/Commands/UpgradeCommands.php`

## Relations cles
- **Position dans le flux global :** support transversal pour toutes les taches Robo

---

## Points d'attention
- L'inclusion de `config.php` au niveau global du fichier peut avoir des effets de bord si le trait est utilise hors contexte Robo.
