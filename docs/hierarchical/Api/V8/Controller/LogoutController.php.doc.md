# LogoutController.php

## Rôle
Contrôleur HTTP de l'API V8 gérant la déconnexion d'un utilisateur OAuth2. Il valide le token d'accès courant via le `ResourceServer` OAuth2, puis révoque ce token via `LogoutService`.

## Responsabilités
- Valider la requête authentifiée via `ResourceServer::validateAuthenticatedRequest()`
- Extraire l'identifiant du token d'accès (`oauth_access_token_id`) depuis les attributs de la requête PSR-7
- Déléguer la révocation du token à `LogoutService::logout()`
- Retourner HTTP 200 en cas de succès ou HTTP 400 en cas d'exception

## Dépendances internes
- `Api\V8\Controller\BaseController` — classe parente (génération de réponses)
- `Api\V8\Service\LogoutService` — service métier qui révoque le token OAuth2
- `League\OAuth2\Server\ResourceServer` — serveur de ressources OAuth2 (bibliothèque `league/oauth2-server`)

## Exports / Points d'entrée
- `LogoutController` (classe) — contrôleur Slim invocable
- `__invoke(Request, Response): Response` — action unique, appelée directement comme callable Slim

## Notes techniques
- Ce contrôleur utilise le pattern callable (`__invoke`) plutôt qu'une méthode nommée, ce qui est différent des autres contrôleurs V8
- L'attribut `oauth_access_token_id` est ajouté par le middleware d'authentification OAuth2 de `league/oauth2-server` en amont
- Aucun objet `Params` n'est injecté ici : le contrôleur n'a pas de quatrième argument, ce qui est cohérent avec l'absence de paramètres métier
