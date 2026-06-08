# ElasticSearchIndexer.php

**Chemin :** `lib/Search/ElasticSearch/ElasticSearchIndexer.php`
**Type :** PHP — Service (indexeur)
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Indexeur Elasticsearch principal de SuiteCRM. Cree, met a jour et supprime les index Elasticsearch a partir des donnees SugarBeans. Supporte l'indexation complete et differentielle.

## Role technique
Etend `AbstractIndexer`, utilise les traits `IndexingStatisticsTrait`, `IndexingLockFileTrait`, `IndexingSchedulerTrait`. Envoie des requetes bulk Elasticsearch. L'indexation differentielle utilise un fichier lock et les metadonnees d'index (`last_index`) pour ne traiter que les beans modifies depuis la derniere execution.

---

## Dependances cles
- `SuiteCRM\Search\Index\AbstractIndexer`
- `SuiteCRM\Search\Index\{IndexingStatisticsTrait, IndexingLockFileTrait, IndexingSchedulerTrait}`
- `SuiteCRM\Search\Index\Documentify\{AbstractDocumentifier, SearchDefsDocumentifier}`
- `SuiteCRM\Search\ElasticSearch\{ElasticSearchClientBuilder, ElasticSearchModuleDataPuller}`
- `Elasticsearch\Client`
- `Carbon\Carbon`

## Exports / Symboles principaux
- `ElasticSearchIndexer` — classe indexeur
  - `static isEnabled(): ?bool`
  - `static repairElasticsearchIndex(bool $differential, int $searchdefs): void` — entrypoint scheduler/Robo
  - `index(): void` — indexation complete ou differentielle
  - `indexModule($module): void`, `indexBeans($module, array $beans): void`, `indexBean(SugarBean $bean): void`
  - `removeBean(SugarBean $bean): void`, `removeBeans(array $beans, $ignore404): void`
  - `removeIndex(string $index): void`, `createIndex(string $index, ?array $body): void`
  - `ping(): int|false`
  - `putMeta(string $module, array $meta): void`, `getMeta(string $module): ?array`
  - `getBatchSize()/setBatchSize(int): void`

## Relations cles
- **Appele par :** `ElasticSearchHooks`, `ElasticSearchCommands`, schedulers
- **Appelle :** `ElasticSearchClientBuilder`, `ElasticSearchModuleDataPuller`, `AbstractDocumentifier`
- **Position dans le flux global :** coeur du sous-systeme d'indexation Elasticsearch

---

## Points d'attention
- Indexation bulk : taille configurable via `setBatchSize()` (defaut 1000).
- Metadonnees stockees dans `_meta` de chaque index (`last_index`, `module_name`).
- Config requise : `$sugar_config['search']['ElasticSearch']['enabled']`.
