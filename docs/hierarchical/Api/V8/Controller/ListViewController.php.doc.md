# ListViewController.php

## Rôle
Contrôleur HTTP de l'API V8 exposant les définitions des colonnes d'une vue liste (list view) d'un module SuiteCRM. Il reçoit une requête HTTP, délègue le traitement à `ListViewService` et retourne la réponse JSON:API.

## Responsabilités
- Recevoir la requête GET pour les colonnes d'une vue liste
- Déléguer à `ListViewService::getListViewDefs()` la récupération des définitions
- Retourner HTTP 200 avec le résultat JSON:API, ou HTTP 400 en cas d'exception

## Dépendances internes
- `Api\V8\Controller\BaseController` — classe parente (génération de réponses)
- `Api\V8\Service\ListViewService` — service métier gérant les définitions de vue liste
- `Api\V8\Param\ListViewColumnsParams` — objet de paramètres typé injecté par `SuiteInvocationStrategy`

## Exports / Points d'entrée
- `ListViewController` (classe) — contrôleur Slim
- `getListViewColumns(Request, Response, array, ListViewColumnsParams): Response` — action principale

## Notes techniques
- Utilise la garde `sugarEntry` (ligne 43) pour empêcher l'exécution directe hors du contexte SuiteCRM
- L'objet `ListViewColumnsParams` est injecté automatiquement comme quatrième argument grâce à `SuiteInvocationStrategy` et `ParamsMiddleware`
- Toute exception levée par le service est capturée et convertie en réponse 400 via `generateErrorResponse()`
