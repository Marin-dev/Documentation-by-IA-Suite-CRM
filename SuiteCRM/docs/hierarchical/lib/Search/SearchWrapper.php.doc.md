# SearchWrapper.php

**Chemin :** `lib/Search/SearchWrapper.php`
**Type :** PHP — Service / Factory
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Point d'entree principal du framework de recherche SuiteCRM. Resout et instancie le moteur de recherche demande, expose les moteurs disponibles (y compris custom), et gere les preferences de modules par utilisateur.

## Role technique
Classe statique. Registre des moteurs dans `$engines`. Cherche d'abord dans le registre, puis dans `custom/Extension/SearchEngines/*.php`. La methode `fetchEngine()` valide l'heritage de `SearchEngine` avant instanciation. Gere les preferences utilisateur via `$current_user->getPreference/setPreference('globalSearch', ...)`.

---

## Dependances cles
- `SuiteCRM\Search\{SearchEngine, SearchQuery, SearchResults, SearchModules}`
- `SuiteCRM\Search\{AOD\LuceneSearchEngine, BasicSearch\BasicSearchEngine, ElasticSearch\ElasticSearchEngine}`
- `SuiteCRM\Search\Exceptions\SearchEngineNotFoundException`
- `$sugar_config` global

## Exports / Symboles principaux
- `SearchWrapper` — classe statique
  - `static searchAndDisplay(SearchQuery): void`
  - `static search(string|SearchEngine, SearchQuery): SearchResults`
  - `static addEngine(string, string, $fqn): void`
  - `static getEngines(): array`
  - `static getDefaultEngine(): string`
  - `static getController(): ?string`
  - `static getModules(): ?array`
  - `static getModulesForDisplay(): array`
  - `static getUserSelectedModules($users_modules = null): array`

## Relations cles
- **Appele par :** modules de recherche, controllers de recherche, `SearchQuery`, CLI Robo
- **Appelle :** moteurs de recherche, `SearchModules`
- **Position dans le flux global :** dispatcher central du framework de recherche

---

## Points d'attention
- Moteurs custom a placer dans `custom/Extension/SearchEngines/{EngineName}.php`.
- Config requise : `$sugar_config['search']['defaultEngine']` et `$sugar_config['search']['controller']`.
- `getUserSelectedModules()` sauvegarde les modules selectionnes dans les preferences utilisateur a chaque appel.
