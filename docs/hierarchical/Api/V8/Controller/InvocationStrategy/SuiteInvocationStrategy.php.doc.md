# SuiteInvocationStrategy.php

## Rôle
Stratégie d'invocation personnalisée pour le framework Slim, remplaçant la stratégie par défaut. Elle injecte les arguments de route comme attributs de la requête et transmet en quatrième argument un objet `params` éventuellement présent dans les attributs de la requête.

## Responsabilités
- Implémenter l'interface `InvocationStrategyInterface` de Slim
- Injecter chaque argument de route comme attribut PSR-7 sur l'objet `ServerRequestInterface`
- Appeler le callable (action du contrôleur) avec la signature étendue `($request, $response, $routeArguments, $params)`
- Passer `null` comme quatrième argument si aucun attribut `params` n'est défini sur la requête

## Dépendances internes
- `Slim\Interfaces\InvocationStrategyInterface` — contrat Slim à implémenter
- `Psr\Http\Message\ServerRequestInterface` — requête PSR-7
- `Psr\Http\Message\ResponseInterface` — réponse PSR-7

## Exports / Points d'entrée
- `SuiteInvocationStrategy` (classe) — à enregistrer dans le conteneur Slim comme stratégie d'invocation des routes
- `__invoke(callable, ServerRequestInterface, ResponseInterface, array): ResponseInterface` — point d'entrée unique

## Notes techniques
- Le commentaire ligne 24 indique que l'opérateur splat (`...`) n'est pas utilisé pour conserver la compatibilité avec PHP 5.5.9, bien que SuiteCRM soit aujourd'hui sur PHP 7+. Cette contrainte historique peut être revue.
- Le quatrième argument `$params` est l'objet `BaseParam` configuré par `ParamsMiddleware` et stocké sous la clé `'params'` dans les attributs de la requête ; les contrôleurs l'utilisent directement via la signature de leur action.
- Cette stratégie est la pièce qui rend possible l'injection de `BaseParam` dans les actions de contrôleur sans passer par le conteneur DI à chaque fois.
