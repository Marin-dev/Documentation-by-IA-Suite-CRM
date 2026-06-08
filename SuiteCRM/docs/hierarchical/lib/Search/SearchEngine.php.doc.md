# SearchEngine.php

**Chemin :** `lib/Search/SearchEngine.php`
**Type :** PHP — Classe abstraite
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Classe abstraite definissant le contrat de tous les moteurs de recherche SuiteCRM. Fournit aussi les methodes d'affichage (formulaire + resultats) via les composants MVC du framework Search.

## Role technique
Une methode abstraite `search(SearchQuery): SearchResults`. Methodes concretes : `searchAndDisplay()` (valide + affiche form + resultats), `displayForm()` (via `SearchFormController`), `displayResults()` (via `SearchResultsController`). `validateQuery()` effectue un `trim()` par defaut.

---

## Dependances cles
- `SuiteCRM\Search\{SearchQuery, SearchResults}`
- `SuiteCRM\Search\Exceptions\SearchInvalidRequestException`
- `SuiteCRM\Search\UI\{SearchFormController, SearchResultsController}`

## Exports / Symboles principaux
- `SearchEngine` — classe abstraite
  - `abstract search(SearchQuery): SearchResults`
  - `searchAndDisplay(SearchQuery): void`
  - `displayForm(SearchQuery): void`
  - `displayResults(SearchQuery, SearchResults): void`
  - `validateQuery(SearchQuery): void` (protected)

- **Implementeurs :** `BasicSearchEngine`, `LuceneSearchEngine`, `ElasticSearchEngine`, `SimpleSqlSearchEngine`

## Relations cles
- **Appele par :** `SearchWrapper`

---

## Points d'attention
- Les sous-classes peuvent surcharger `validateQuery()` pour des validations supplementaires.
