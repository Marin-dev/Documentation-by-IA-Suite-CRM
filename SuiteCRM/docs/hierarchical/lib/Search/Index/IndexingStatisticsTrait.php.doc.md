# IndexingStatisticsTrait.php

**Chemin :** `lib/Search/Index/IndexingStatisticsTrait.php`
**Type :** PHP — Trait
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Trait fournissant le suivi statistique des operations d'indexation : modules indexes, enregistrements indexes, champs indexes, enregistrements supprimes.

## Role technique
Quatre compteurs prives (`$indexedModulesCount`, `$indexedRecordsCount`, `$indexedFieldsCount`, `$removedRecordsCount`). Methode `statistics()` loggue un bilan de performance. `resetCounts()` remet tout a zero.

---

## Dependances cles
- `Monolog\Logger` (propriete `$this->logger` attendue)

## Exports / Symboles principaux
- `IndexingStatisticsTrait` — trait
  - `getRemovedRecordsCount/getIndexedRecordsCount/getIndexedFieldsCount/getIndexedModulesCount(): int`
  - `statistics(float $end, float $start): void` (private) — log bilan
  - `resetCounts(): void` (private)

- **Consommateurs :** `ElasticSearchIndexer`

---

## Points d'attention
- `statistics()` estime le temps pour 200000 enregistrements si plus de 100 records indexes.
- Le calcul de vitesse est lineaire (extrapolation simple).
