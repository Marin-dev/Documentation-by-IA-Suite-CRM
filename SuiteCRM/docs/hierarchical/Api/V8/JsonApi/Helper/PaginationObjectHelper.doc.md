# Fichier : PaginationObjectHelper.php

**Chemin :** `Api/V8/JsonApi/Helper/PaginationObjectHelper.php`
**Type :** helper
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Construit les objets de pagination JSON:API : méta-données (`total-pages`, `records-on-this-page`) et liens de navigation (first, prev, next, last). Les liens sont générés à partir de la requête HTTP courante en modifiant le paramètre `page[number]`.

---

## Type

helper

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `Api\V8\JsonApi\Response\MetaResponse` | Objet de retour pour les méta-données de pagination |
| `Api\V8\JsonApi\Response\PaginationResponse` | Objet de retour pour les liens de navigation |
| `Slim\Http\Request` | Fournit l'URI courante et les query params pour construire les liens |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `PaginationObjectHelper` | classe | Helper injectable pour la pagination JSON:API |
| `getPaginationMeta(int $totalPages, int $numOfRecords)` | méthode publique | Retourne un `MetaResponse` avec le nombre total de pages et d'enregistrements |
| `getPaginationLinks(Request $request, int $totalPages, int $number)` | méthode publique | Retourne un `PaginationResponse` avec les liens first/prev/next/last selon la page courante |
| `createPaginationLink(Request $request, int $number)` | méthode privée | Construit l'URL d'une page donnée en réinjectant le numéro dans les query params |

---

## Interactions

**Appelé par :**
- `Api/V8/Service/ModuleService.php`
- `Api/V8/Service/ListViewService.php`
- `Api/V8/Service/ListViewSearchService.php`
- `Api/V8/Service/RelationshipService.php`

**Appelle :**
- `Api\V8\JsonApi\Response\MetaResponse`
- `Api\V8\JsonApi\Response\PaginationResponse`
- `Slim\Http\Request::getQueryParams()` et `getUri()->getPath()`

**Enregistré comme service dans :**
- `Api/V8/Config/services/helpers.php`
- `Api/V8/Config/services/services.php`

---

## Notes

- Les liens `first`/`prev` ne sont ajoutés que si `$number > 1` (ligne 35).
- Les liens `next`/`last` ne sont ajoutés que si la page suivante existe (`$number + 1 <= $totalPages`) (ligne 40).
- La construction du lien préserve tous les query params existants (filtre, tri, etc.) en remplaçant uniquement `page[number]` (ligne 57-59).
