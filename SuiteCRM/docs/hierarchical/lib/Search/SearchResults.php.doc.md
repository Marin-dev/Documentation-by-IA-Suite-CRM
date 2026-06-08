# SearchResults.php

**Chemin :** `lib/Search/SearchResults.php`
**Type :** PHP — Objet valeur (Value Object)
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Conteneur des resultats d'une recherche. Stocke les IDs groupes par module, les scores, le temps de recherche, et le total. Fournit aussi la resolution des beans et le formatage pour l'affichage (enum, multienum, currency, liens).

## Role technique
Constructeur valide la coherence `hits/scores`. Methode `getHitsAsBeans()` charge les beans depuis BeanFactory, formate les valeurs (enum -> label, currency -> format localise), et ajoute des liens HTML pour les champs `name` et `relate`.

---

## Dependances cles
- `BeanFactory`
- `SugarBean`
- `SuiteCRM\Exception\Exception`, `InvalidArgumentException`
- `SuiteCRM\Search\ElasticSearch\ElasticSearchIndexer` (pour reindex en cas de bean manquant)

## Exports / Symboles principaux
- `SearchResults` — classe
  - `getHits(): array` — IDs groupes par module
  - `getHitsAsBeans(): array` — beans resolus et formates
  - `getTotal(): ?int`, `getModuleTotal(string): ?int`
  - `getSearchTime(): ?float`
  - `isGroupedByModule(): bool`
  - `getLargestHitsCount(): int`

## Relations cles
- **Appele par :** `SearchResultsController`, moteurs de recherche
- **Appelle :** `BeanFactory`, `ElasticSearchIndexer::repairElasticsearchIndex()` (fallback)

---

## Points d'attention
- Si un bean ES n'est pas trouve en BDD, tente de reparer l'index ES automatiquement (ligne 136).
- `formatForDisplay()` gere `enum`, `dynamicenum`, `multienum`, et `currency` (avec conversion de devise).
- Les liens HTML generes via `ajaxLink()` — dependance globale SuiteCRM.
