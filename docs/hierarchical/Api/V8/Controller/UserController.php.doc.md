# UserController.php

## Rôle
Contrôleur HTTP de l'API V8 exposant les informations de l'utilisateur courant authentifié. Il délègue à `UserService` et retourne les données au format JSON:API.

## Responsabilités
- Recevoir la requête GET pour l'utilisateur courant
- Déléguer à `UserService::getCurrentUser()` la récupération des informations
- Retourner HTTP 200 avec les données utilisateur, ou HTTP 400 en cas d'exception

## Dépendances internes
- `Api\V8\Controller\BaseController` — classe parente (génération de réponses)
- `Api\V8\Service\UserService` — service métier pour les données utilisateur

## Exports / Points d'entrée
- `UserController` (classe) — contrôleur Slim
- `getCurrentUser(Request, Response, array): Response` — action principale

## Notes techniques
- Utilise la garde `sugarEntry` (ligne 43)
- Contrairement à la majorité des autres contrôleurs, `getCurrentUser` ne reçoit pas de quatrième argument `Params` : la requête elle-même est transmise directement à `UserService`, probablement pour extraire le token OAuth2 ou l'ID utilisateur depuis les attributs
- Contrôleur minimaliste à une seule action
