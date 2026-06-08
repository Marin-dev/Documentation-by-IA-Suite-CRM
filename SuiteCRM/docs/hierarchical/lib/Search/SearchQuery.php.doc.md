# SearchQuery.php

**Chemin :** `lib/Search/SearchQuery.php`
**Type :** PHP — Objet valeur (Value Object)
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Objet encapsulant une requete de recherche avec toutes ses options : chaine de recherche, moteur, pagination (size/from), modules cibles, options supplementaires. Immuable apres construction (constructeur prive).

## Role technique
Implementer `JsonSerializable`. Constructeur prive, utiliser `fromString()`, `fromRequestArray()`, ou `fromGetRequest()` pour instancier. `getDefaultEngine()` lit `$sugar_config['search']['defaultEngine']` et gere le cas `BasicAndAodEngine` (bascule vers Lucene ou Basic selon AOD).

---

## Dependances cles
- `SuiteCRM\Search\SearchWrapper` — pour les modules par defaut et les preferences utilisateur
- `$sugar_config` global — cles `search.defaultEngine`, `search.query_size`, `search.pagination.min`

## Exports / Symboles principaux
- `SearchQuery` — classe value object
  - `const DEFAULT_SEARCH_SIZE = 10`
  - `static fromString(string, $size, $from, $engine, $options, $modules): SearchQuery`
  - `static fromRequestArray(array $request): SearchQuery`
  - `static fromGetRequest(): SearchQuery`
  - `getSearchString/getEngine/getSize/getFrom/getModules/getOptions/isEmpty`
  - Mutateurs : `trim/toLowerCase/replace/stripSlashes/escapeRegex/convertEncoding`
  - `jsonSerialize(): array`

## Relations cles
- **Appele par :** `SearchWrapper`, moteurs de recherche, `SearchResultsController`
- **Position dans le flux global :** DTO de la requete de recherche

---

## Points d'attention
- `fromRequestArray()` lit et sauvegarde les preferences de modules via `SearchWrapper::getUserSelectedModules()`.
- `getDefaultEngine()` : si `BasicAndAodEngine` est configure, choisit entre Lucene et Basic selon `$sugar_config['aod']['enable_aod']` et `$_REQUEST['showGSDiv']`/`search_fallback`.
