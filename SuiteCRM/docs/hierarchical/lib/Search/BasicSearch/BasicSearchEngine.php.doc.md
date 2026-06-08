# BasicSearchEngine.php

**Chemin :** `lib/Search/BasicSearch/BasicSearchEngine.php`
**Type :** PHP — Service (moteur de recherche)
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Moteur de recherche SQL classique de SuiteCRM. Effectue des recherches dans les modules actives via les SearchForms SQL et les `listViewDefs`. Correspond a la recherche globale unifiee historique.

## Role technique
Etend `SearchEngine`. Pour chaque module, charge les `listviewdefs` et `SearchFields`, construit les clauses WHERE via `SearchForm::generateSearchWhere()`, puis execute `ListViewData::getListViewData()`. Stocke les totaux dans `$_SESSION['basicSearchTotal']`.

---

## Dependances cles
- `SuiteCRM\Search\{SearchEngine, SearchModules, SearchQuery, SearchResults}`
- `BeanFactory`, `DBManagerFactory`, `ListViewData`
- `include/SearchForm/SearchForm2.php`

## Exports / Symboles principaux
- `BasicSearchEngine` — classe moteur de recherche
  - `search(SearchQuery $query): SearchResults`
  - `buildFilterFields(SugarBean $bean): array` (protected)

## Relations cles
- **Appele par :** `SearchWrapper` (via `fetchEngine('BasicSearchEngine')`)
- **Appelle :** `SearchModules::getUnifiedSearchModules()`, `SearchForm`, `ListViewData`
- **Position dans le flux global :** moteur de recherche par defaut (sans Elasticsearch ni AOD)

---

## Points d'attention
- Dependance sur `$_SESSION['basicSearchTotal']` pour la pagination (ligne 89, 105).
- Si les defs de listview ont ete personnalisees, le code gere la reconciliation entre defs originales et custom (lignes 137-143).
- Tres lent sur de grandes bases — recommander Elasticsearch a la place.
