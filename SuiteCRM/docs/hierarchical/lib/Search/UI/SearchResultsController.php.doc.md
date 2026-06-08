# SearchResultsController.php

**Chemin :** `lib/Search/UI/SearchResultsController.php`
**Type :** PHP — Controller MVC
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Controleur d'affichage des resultats de recherche. Construit les donnees de pagination, les en-tetes de colonnes (listviewdefs), resout les beans depuis les resultats, et transmet tout au template Smarty.

## Role technique
Etend `Controller`. `display()` calcule la pagination (page courante, precedent/suivant/dernier). Charge les `listviewdefs` de chaque module via `ViewList::getMetaDataFile()`. Assigne les beans formates et les labels de modules au template. Utilise `SearchResults::getHitsAsBeans()`.

---

## Dependances cles
- `SuiteCRM\Search\{SearchQuery, SearchResults}`
- `SuiteCRM\Search\UI\{SearchResultsView, MVC\Controller}`
- `SuiteCRM\{ErrorMessageException, LangText}`
- `BeanFactory`, `SugarBean`, `ViewList`

## Exports / Symboles principaux
- `SearchResultsController` — controleur
  - `display(): void`
  - `getQuery(): SearchQuery`
  - `getResults(): SearchResults`

- **Consommateurs :** `SearchEngine::displayResults()`

---

## Points d'attention
- Si `total > 1` et `size === 0` : leve `SearchException::ZERO_SIZE`.
- `getListViewHeaders()` peut echouer silencieusement avec warning (catch Exception, ligne 107).
- Variables Smarty assignees : `total`, `headers`, `results`, `APP`, `APP_CONFIG`, `SITE_URL`, `moduleLabel`, `resultsAsBean`.
