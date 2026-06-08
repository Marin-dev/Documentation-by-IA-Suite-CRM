# MetaController.php

## Rôle
Contrôleur HTTP de l'API V8 exposant les métadonnées de SuiteCRM : liste des modules accessibles, liste des champs d'un module, et schéma Swagger de l'API. Il délègue entièrement à `MetaService`.

## Responsabilités
- Exposer `GET /module-list` via `getModuleList()` : liste des modules accessibles à l'utilisateur courant
- Exposer `GET /field-list` via `getFieldList()` : liste des champs d'un module donné
- Exposer `GET /swagger` via `getSwaggerSchema()` : retourner la documentation OpenAPI/Swagger
- Déléguer chaque opération à `MetaService` et normaliser les réponses HTTP 200/400

## Dépendances internes
- `Api\V8\Controller\BaseController` — classe parente (génération de réponses)
- `Api\V8\Service\MetaService` — service métier centralisant la logique de métadonnées
- `Api\V8\Param\GetFieldListParams` — objet de paramètres pour l'action `getFieldList`

## Exports / Points d'entrée
- `MetaController` (classe) — contrôleur Slim
- `getModuleList(Request, Response, array): Response` — action liste des modules
- `getFieldList(Request, Response, array, GetFieldListParams): Response` — action liste des champs
- `getSwaggerSchema(Request, Response): Response` — action schéma Swagger

## Notes techniques
- Note de code (ligne 62-63) : la propriété privée `$metaService` est déclarée avec le type `UserService` par erreur ; elle est en réalité de type `MetaService`. C'est une anomalie de typage (dette technique)
- Utilise la garde `sugarEntry` (ligne 43)
- `getSwaggerSchema` ne reçoit aucun paramètre métier : la génération du schéma est entièrement gérée par `MetaService`
