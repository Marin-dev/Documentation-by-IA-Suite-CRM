# SearchException.php

**Chemin :** `lib/Search/Exceptions/SearchException.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Exception de base du framework de recherche SuiteCRM. Contient des codes d'erreur specifiques a la recherche.

## Role technique
Etend `RuntimeException`. Definit trois constantes : `ZERO_SIZE` (100), `ES_DISABLED` (101), `ES_MODULE_BLACKLISTED` (102). Classe de base pour toutes les exceptions Search.

---

## Dependances cles
- `RuntimeException` (PHP natif)

## Exports / Symboles principaux
- `SearchException` — classe exception
  - `const ZERO_SIZE = 100`
  - `const ES_DISABLED = 101`
  - `const ES_MODULE_BLACKLISTED = 102`

- **Sous-classes :**
  - `SearchEngineNotFoundException`
  - `SearchInvalidRequestException`
  - `SearchUserFriendlyException`

## Relations cles
- **Appele par :** `SearchResultsController`, `ElasticSearchHooks`, `SearchWrapper`

---

## Points d'attention
- RAS.
