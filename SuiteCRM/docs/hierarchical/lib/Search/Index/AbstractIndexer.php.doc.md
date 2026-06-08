# AbstractIndexer.php

**Chemin :** `lib/Search/Index/AbstractIndexer.php`
**Type :** PHP — Classe abstraite
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Classe de base pour tous les indexeurs de recherche SuiteCRM. Definit le contrat d'interface (indexation, suppression), la configuration (modules, documentifier, indexation differentielle), et le logging via Monolog avec triple sortie (SugarLog, fichier, CLI).

## Role technique
Configure automatiquement un logger Monolog avec trois handlers (`SugarLoggerHandler`, `StreamHandler`, `CliLoggerHandler`). Par defaut utilise `JsonSerializerDocumentifier` et recupere la liste des modules via `SearchWrapper::getModules()`.

---

## Dependances cles
- `SuiteCRM\Search\Index\Documentify\{AbstractDocumentifier, JsonSerializerDocumentifier}`
- `SuiteCRM\Search\SearchWrapper`
- `SuiteCRM\Log\{CliLoggerHandler, SugarLoggerHandler}`
- `Monolog\{Logger, Handler\StreamHandler}`

## Exports / Symboles principaux
- `AbstractIndexer` — classe abstraite
  - `abstract index(): void`
  - `abstract indexModule($module): void`
  - `abstract indexBean(\SugarBean $bean): void`
  - `abstract indexBeans($module, array $beans): void`
  - `abstract removeBean(\SugarBean $bean): void`
  - `abstract removeBeans(array $beans): void`
  - `abstract removeIndex(string $index): void`
  - `isDifferentialIndexing/setDifferentialIndexing`
  - `getDocumentifier/setDocumentifier`
  - `getModulesToIndex/setModulesToIndex/addModulesToIndex`
  - `getLogger(): Logger`

- **Implementeurs :** `ElasticSearchIndexer`

## Relations cles
- **Appele par :** `ElasticSearchHooks`, `ElasticSearchCommands`, scheduler
- **Appelle :** `SearchWrapper::getModules()`, `JsonSerializerDocumentifier`

---

## Points d'attention
- Log file : `search_index.log` a la racine du projet (configurable via `$logFile`).
- Si `CliLoggerHandler` ou `StreamHandler` echoue a s'initialiser, l'erreur est loggee mais l'indexeur continue.
