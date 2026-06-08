# ListViewSearchController.php

## Rôle
Contrôleur HTTP de l'API V8 exposant les définitions de recherche d'une vue liste (search defs) pour un module SuiteCRM. Il délègue à `ListViewSearchService` et retourne la réponse JSON:API.

## Responsabilités
- Recevoir la requête GET pour les définitions de recherche d'une vue liste
- Déléguer à `ListViewSearchService::getListViewSearchDefs()` la récupération des définitions
- Retourner HTTP 200 avec le résultat JSON:API, ou HTTP 400 en cas d'exception

## Dépendances internes
- `Api\V8\Controller\BaseController` — classe parente (génération de réponses)
- `Api\V8\Service\ListViewSearchService` — service métier gérant les définitions de recherche
- `Api\V8\Param\ListViewSearchParams` — objet de paramètres typé injecté par `SuiteInvocationStrategy`

## Exports / Points d'entrée
- `ListViewSearchController` (classe) — contrôleur Slim
- `getModuleSearchDefs(Request, Response, array, ListViewSearchParams): Response` — action principale

## Notes techniques
- Même structure que `ListViewController` : garde `sugarEntry`, injection du quatrième argument param, capture d'exception en 400
- La distinction avec `ListViewController` est que ce contrôleur expose les critères de filtrage/recherche, pas les colonnes à afficher
