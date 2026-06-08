# ParamsMiddlewareFactory.php

## Rôle
Factory qui produit des closures de middleware Slim à la demande. Chaque closure instancie un `ParamsMiddleware` en résolvant dynamiquement l'objet `BaseParam` correspondant depuis le conteneur DI, permettant de réutiliser un seul factory pour tous les endpoints paramétrés.

## Responsabilités
- Stocker une référence au conteneur DI Slim (`ContainerInterface`)
- Exposer `bind($containerId)` qui retourne une closure de middleware Slim
- La closure instancie `ParamsMiddleware` avec le `BaseParam` identifié par `$containerId` et le `BeanManager`
- Permettre la réutilisation du factory pour n'importe quel type de paramètre sans dupliquer du code de middleware

## Dépendances internes
- `Api\V8\Middleware\ParamsMiddleware` — le middleware instancié par la factory
- `Api\V8\BeanDecorator\BeanManager` — résolu depuis le conteneur et injecté dans `ParamsMiddleware`
- `Psr\Container\ContainerInterface` — conteneur DI Slim

## Exports / Points d'entrée
- `ParamsMiddlewareFactory` (classe) — factory enregistrée dans le conteneur DI
- `bind(string $containerId): callable` — retourne une closure compatible avec `$app->add()` ou le système de middleware Slim

## Notes techniques
- Utilise `#[\AllowDynamicProperties]`
- Le pattern « factory retournant une closure » permet d'enregistrer ce factory une seule fois dans le conteneur et de l'appeler avec un `$containerId` différent pour chaque route, évitant de créer une classe factory par type de paramètre
- Le `$containerId` doit correspondre à une entrée du conteneur DI qui retourne une instance de `BaseParam` ; si ce n'est pas le cas, une exception sera levée à l'exécution
