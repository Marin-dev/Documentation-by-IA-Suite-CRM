# CliRunnerTrait.php

**Chemin :** `lib/Robo/Traits/CliRunnerTrait.php`
**Type :** PHP — Trait
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Trait fournissant un bootstrap complet de SuiteCRM depuis la ligne de commande. Initialise les globals necessaires (`$current_language`, `$app_list_strings`, `$sugar_config`) pour que les classes SugarCRM fonctionnent en contexte CLI.

## Role technique
La methode `bootstrap()` :
1. Definit `sugarEntry = true` et `SUITE_CLI_RUNNER = true`
2. Charge `config.php`, `config_override.php`, et `include/entryPoint.php`
3. Charge optionnellement `tests/config.test.php`
4. Initialise `$current_language = 'en_us'` et `$app_list_strings`
5. Force `resource_management.default_limit` a 999999

---

## Dependances cles
- `config.php`, `config_override.php` (racine projet)
- `include/entryPoint.php` — entrypoint SuiteCRM
- `tests/config.test.php` (optionnel)

## Exports / Symboles principaux
- `CliRunnerTrait` — trait
  - `bootstrap(): void` (protected) — initialise SuiteCRM en CLI

- **Consommateurs identifies :**
  - `lib/Robo/Plugin/Commands/ApiCommands.php`
  - `lib/Robo/Plugin/Commands/CleanCacheCommands.php`
  - `lib/Robo/Plugin/Commands/ElasticSearchCommands.php`

## Relations cles
- **Position dans le flux global :** prerequis d'initialisation pour toutes les taches Robo necessitant un acces BDD

---

## Points d'attention
- `bootstrap()` doit etre appele en premier dans les commandes Robo.
- Le `resource_management.default_limit` a 999999 peut impacter les perfs si utilise en production.
