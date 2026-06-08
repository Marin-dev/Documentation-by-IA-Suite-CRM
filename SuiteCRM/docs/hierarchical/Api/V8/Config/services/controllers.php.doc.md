# 📄 controllers.php

**Chemin :** `Api/V8/Config/services/controllers.php`
**Type :** PHP (configuration — conteneur DI)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Enregistre toutes les définitions de contrôleurs de l'API V8 dans le conteneur d'injection de dépendances. Chaque contrôleur est instancié avec son service métier correspondant (et `ResourceServer` pour `LogoutController`).

**Type :** config

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `Api\V8\Controller` (namespace) | Tous les contrôleurs V8 |
| `Api\V8\Service\*` (8 services) | Services métier injectés dans les contrôleurs |
| `League\OAuth2\Server\ResourceServer` | Injecté dans `LogoutController` |
| `Psr\Container\ContainerInterface` | Accès au conteneur dans les factories |
| `Api\Core\Loader\CustomLoader` | Fusion avec contrôleurs personnalisés |

---

## Contrôleurs enregistrés

| Clé DI | Service(s) injecté(s) |
|---|---|
| `ListViewSearchController::class` | `ListViewSearchService` |
| `UserPreferencesController::class` | `UserPreferencesService` |
| `UserController::class` | `UserService` |
| `MetaController::class` | `MetaService` |
| `ListViewController::class` | `ListViewService` |
| `ModuleController::class` | `ModuleService` |
| `LogoutController::class` | `LogoutService` + `ResourceServer` |
| `RelationshipController::class` | `RelationshipService` |

---

## Interactions

- **Appelé par :** `Api/V8/Config/services.php` (via `require`)
- **Appelle :** résolution des services dans le conteneur à l'instanciation
- **Position dans le flux :** configuration au démarrage, les contrôleurs sont résolus à la première requête qui les sollicite

---

## Notes

- `LogoutController` est le seul contrôleur à recevoir deux dépendances, dont `ResourceServer` (pour valider/révoquer le token OAuth2).
- `CustomLoader::mergeCustomArray` permet d'ajouter ou de surcharger des contrôleurs via customisation.
