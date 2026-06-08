# ElasticSearchEngine.php

**Chemin :** `lib/Search/ElasticSearch/ElasticSearchEngine.php`
**Type :** PHP — Service (moteur de recherche)
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Moteur de recherche Elasticsearch de SuiteCRM. Effectue des recherches presque en temps reel via l'API Elasticsearch, avec support du wildcard, de l'encodage et de la pagination.

## Role technique
Etend `SearchEngine`. Pour chaque module (index), construit un objet `query_string` Elasticsearch avec wildcard automatique (`*` en fin) et operateur OR. Ajoute le wildcard en debut si `search_wildcard_infront` est configure. Parse les hits en les groupant par module.

---

## Dependances cles
- `SuiteCRM\Search\{SearchEngine, SearchQuery, SearchResults}`
- `SuiteCRM\Search\ElasticSearch\ElasticSearchClientBuilder`
- `Elasticsearch\Client`
- `SuiteCRM\Exception\InvalidArgumentException`

## Exports / Symboles principaux
- `ElasticSearchEngine` — classe moteur de recherche
  - `search(SearchQuery $query): SearchResults`

- **Consommateurs identifies :**
  - `lib/Search/SearchWrapper.php`

## Relations cles
- **Appele par :** `SearchWrapper::fetchEngine('ElasticSearchEngine')`
- **Appelle :** `ElasticSearchClientBuilder::getClient()`, API Elasticsearch
- **Position dans le flux global :** moteur de recherche avance (temps reel)

---

## Points d'attention
- Config `$sugar_config['search_wildcard_char']` : permet de substituer le caractere wildcard front-end.
- Config `$sugar_config['search_wildcard_infront']` : ajoute `*` en debut de requete.
- `minimum_should_match` fixe a `66%` (ligne 154) — au moins 2/3 des mots doivent correspondre.
- Les index ES sont en minuscules (noms de modules lowercased).
