# SearchDefsDocumentifier.php

**Chemin :** `lib/Search/Index/Documentify/SearchDefsDocumentifier.php`
**Type :** PHP — Service
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Documentifier alternatif base sur les fichiers de definition de recherche (`searchdefs`) de chaque module. Produit un document indexable uniquement avec les champs definis dans les searchdefs, ce qui le rend customisable par module.

## Role technique
Etend `AbstractDocumentifier`. Utilise `ParserSearchFields` pour lire les champs de recherche de chaque module. Met en cache les champs par module (`$fields[]`). Applique `ArrayMapper` avec un fichier YAML (`SearchDefsDocumentifier.yml`) pour le mapping des champs. Configure son propre logger Monolog.

---

## Dependances cles
- `ParserSearchFields` (`modules/ModuleBuilder/parsers/parser.searchfields.php`)
- `SuiteCRM\Utility\ArrayMapper`
- `SuiteCRM\Log\{CliLoggerHandler, SugarLoggerHandler}`
- `Monolog\Logger`

## Exports / Symboles principaux
- `SearchDefsDocumentifier` — classe
  - `documentify(\SugarBean $bean, ?ParserSearchFields $parser = null): array`
  - `getFieldsToIndex(string $module, ...): array` (protected)

- **Consommateurs :** `ElasticSearchIndexer` (option searchdefs), `ElasticSearchCommands` (parametre `$searchdefs=1`)

---

## Points d'attention
- Cache par module en memoire (`$fields[]`) — si le meme documentifier est reutilise pour plusieurs modules, les champs sont caches.
- Exclut les champs `favorites_only`, `open_only`, `do_not_call`, `email`, `optinprimary` (ligne 126).
- Mapping via `SearchDefsDocumentifier.yml` — ce fichier YAML definit les renommages de champs.
