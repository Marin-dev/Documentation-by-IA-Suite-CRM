# ElasticSearchCommands.php

**Chemin :** `lib/Robo/Plugin/Commands/ElasticSearchCommands.php`
**Type :** PHP — Commandes Robo CLI
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Commandes Robo pour gerer l'index Elasticsearch de SuiteCRM depuis la CLI : recherche, indexation complete ou differentielle, suppression de l'index.

## Role technique
Etend `Robo\Tasks` + `RoboTrait` + `CliRunnerTrait`. Bootstrap SuiteCRM avant chaque commande. Delegue a `ElasticSearchIndexer` et `SearchWrapper` pour les operations.

---

## Dependances cles
- `Robo\Tasks`
- `SuiteCRM\Robo\Traits\{RoboTrait, CliRunnerTrait}`
- `SuiteCRM\Search\ElasticSearch\ElasticSearchIndexer`
- `SuiteCRM\Search\Index\Documentify\{JsonSerializerDocumentifier, SearchDefsDocumentifier}`
- `SuiteCRM\Search\{SearchQuery, SearchResults, SearchWrapper}`
- `SuiteCRM\Utility\BeanJsonSerializer`
- `BeanFactory`

## Exports / Symboles principaux
- `ElasticSearchCommands` — classe commandes Robo
  - `elasticSearch(string $query, int $size, bool $showJson): void` — recherche ES
  - `elasticIndex(int $differential, int $searchdefs): void` — indexation (0=full, 1=diff)
  - `elasticRmIndex(): void` — suppression de l'index

## Relations cles
- **Appele par :** CLI Robo (`./vendor/bin/robo elastic:*`)
- **Appelle :** `ElasticSearchIndexer`, `SearchWrapper`, `BeanJsonSerializer`
- **Position dans le flux global :** administration de l'index de recherche

---

## Points d'attention
- `elastic:index` : parametre `1` (differentiel) par defaut — plus rapide mais ne reindex pas tout.
- Parametres CLI `0/1` a la place de `true/false` (note dans le code ligne 113).
