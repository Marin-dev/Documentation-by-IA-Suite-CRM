# ParamsMiddleware.php

## Rôle
Middleware Slim exécuté avant chaque action de contrôleur paramétrée. Il identifie l'utilisateur courant à partir du token OAuth2, charge l'objet `current_user` global, puis configure et attache l'objet `BaseParam` à la requête pour qu'il soit disponible en quatrième argument dans les actions.

## Responsabilités
- Résoudre l'utilisateur courant depuis le token OAuth2 (`oauth_access_token_id`) via `BeanManager`
- Vérifier que l'utilisateur est actif (`isEnabled()`) ; lever une `RuntimeException` sinon
- Injecter l'utilisateur dans `$GLOBALS['current_user']` pour les appels SuiteCRM legacy
- Fusionner les paramètres de route, query string et corps de la requête
- Configurer l'objet `BaseParam` via `configure()` avec ces paramètres fusionnés
- Attacher l'objet `BaseParam` configuré comme attribut `'params'` de la requête PSR-7
- En cas d'erreur : logger en `fatal` via `LoggerManager` et retourner HTTP 400 JSON

## Dépendances internes
- `Api\V8\Param\BaseParam` — objet de paramètres à configurer (injecté par `ParamsMiddlewareFactory`)
- `Api\V8\BeanDecorator\BeanManager` — accès aux beans SuiteCRM (`OAuth2Tokens`, `Users`)
- `Api\V8\JsonApi\Response\ErrorResponse` — objet de réponse d'erreur JSON:API
- `LoggerManager` — logger SuiteCRM global

## Exports / Points d'entrée
- `ParamsMiddleware` (classe) — middleware Slim invocable
- `__invoke(Request, Response, callable $next): Response` — point d'entrée du middleware

## Notes techniques
- Ce middleware est le pivot de la sécurité applicative : il est exécuté avant chaque action et garantit que `$GLOBALS['current_user']` est valide
- La récupération du token utilise `retrieve_by_string_fields()` sur le bean `OAuth2Tokens` — si le token est introuvable, `$oauth2Token->assigned_user_id` sera vide et `getBeanSafe('Users', '')` peut lever une exception ou retourner un bean vide (comportement à vérifier)
- `getParameters()` (ligne 97) décode les valeurs de route avec `urldecode()` mais pas les query params ni le body — cohérence INCONNU
- Les valeurs booléennes dans les arguments de route sont préservées sans urldecode (ligne 100)
- En cas d'exception, le middleware log en `fatal` ET retourne 400 au client, ce qui est un niveau de log potentiellement trop élevé pour des erreurs de validation client ordinaires
