# controllers.php

**Chemin :** `Api/V8/Config/services/controllers.php`
**Type :** PHP (configuration DI)
**Dernière mise à jour doc :** 2026-05-28

## Rôle

Enregistre dans le conteneur DI l'ensemble des contrôleurs de l'API V8. Chaque contrôleur est instancié avec son service métier correspondant, injecté depuis le conteneur. Ce fichier est le câblage Contrôleur ↔ Service de la couche HTTP.

## Responsabilités

Enregistrer huit contrôleurs, chacun recevant un service en injection :

| Contrôleur | Service injecté |
|---|---|
| `ListViewSearchController` | `ListViewSearchService` |
| `UserPreferencesController` | `UserPreferencesService` |
| `UserController` | `UserService` |
| `MetaController` | `MetaService` |
| `ListViewController` | `ListViewService` |
| `ModuleController` | `ModuleService` |
| `LogoutController` | `LogoutService` + `ResourceServer` |
| `RelationshipController` | `RelationshipService` |

## Dépendances internes

| Symbole | Source | Rôle |
|---|---|---|
| `Api\V8\Controller\*` | `Api/V8/Controller/` | Classes contrôleurs HTTP |
| `Api\V8\Service\*` | `Api/V8/Service/` | Services métier injectés |
| `League\OAuth2\Server\ResourceServer` | vendor League | Requis uniquement par `LogoutController` pour valider le token |
| `CustomLoader` | `Api\Core\Loader\CustomLoader` | Surcharge custom |

## Exports / Points d'entrée

Ce fichier retourne un tableau de closures indexées par FQCN de contrôleur. Il est inclus (via `require`) dans `services.php` et fusionné dans le conteneur principal.

- **Consommateurs :** `Api/V8/Config/services.php` (ligne 22 : `require __DIR__ . '/services/controllers.php'`)
- Les contrôleurs sont ensuite résolus par le routeur Slim lors de la correspondance des routes définies dans `routes.php`.

## Notes techniques

- `LogoutController` est le seul contrôleur à recevoir deux dépendances : un service métier ET `ResourceServer`. Cela suggère qu'il valide lui-même le token OAuth2 avant de révoquer la session.
- L'absence de contrôleur `AuthController` indique que l'émission de tokens est gérée directement par League OAuth2 Server (côté `middlewares.php` / `AuthorizationServer`), non par un contrôleur custom.
