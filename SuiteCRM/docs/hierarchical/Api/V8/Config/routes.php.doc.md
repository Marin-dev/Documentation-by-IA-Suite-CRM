# 📄 routes.php

**Chemin :** `Api/V8/Config/routes.php`
**Type :** PHP (configuration de routage)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Fichier de déclaration de toutes les routes HTTP de l'API V8 de SuiteCRM. Il enregistre les endpoints REST JSON:API sur l'application Slim, y compris l'authentification OAuth2, les opérations CRUD sur les modules, et la gestion des relations entre beans. Ce fichier est le point d'entrée de la définition du contrat API.

**Type :** config / entrypoint

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `Api\V8\Controller\LogoutController` | Contrôleur de déconnexion |
| `Api\V8\Factory\ParamsMiddlewareFactory` | Fabrique du middleware de validation des paramètres |
| `Api\V8\Param` (namespace) | Classes de paramètres pour chaque route |
| `League\OAuth2\Server\AuthorizationServer` | Serveur OAuth2 (émission de tokens) |
| `League\OAuth2\Server\Middleware\AuthorizationServerMiddleware` | Middleware Slim pour `/access_token` |
| `League\OAuth2\Server\Middleware\ResourceServerMiddleware` | Middleware Slim protégeant tout le groupe `/V8` |
| `League\OAuth2\Server\ResourceServer` | Serveur de ressources OAuth2 (validation des tokens) |
| `Api\Core\Loader\CustomLoader` | Chargement des routes personnalisées |

---

## Exports / Symboles principaux

Ce fichier ne définit pas de classe ni de symbole exportable. Il produit un effet de bord : l'enregistrement des routes sur `$app` (instance Slim).

---

## Routes enregistrées

| Méthode | Chemin | Contrôleur::action | Paramètres middleware |
|---|---|---|---|
| POST | `/access_token` | (AuthorizationServerMiddleware) | — |
| POST | `/V8/logout` | `LogoutController` | — |
| GET | `/V8/search-defs/module/{moduleName}` | `ListViewSearchController::getModuleSearchDefs` | `ListViewSearchParams` |
| GET | `/V8/listview/columns/{moduleName}` | `ListViewController::getListViewColumns` | `ListViewColumnsParams` |
| GET | `/V8/current-user` | `UserController::getCurrentUser` | — |
| GET | `/V8/meta/modules` | `MetaController::getModuleList` | — |
| GET | `/V8/meta/fields/{moduleName}` | `MetaController::getFieldList` | `GetFieldListParams` |
| GET | `/V8/user-preferences/{id}` | `UserPreferencesController::getUserPreferences` | `GetUserPreferencesParams` |
| GET | `/V8/meta/swagger.json` | `MetaController::getSwaggerSchema` | — |
| GET | `/V8/module/{moduleName}` | `ModuleController::getModuleRecords` | `GetModulesParams` |
| GET | `/V8/module/{moduleName}/{id}` | `ModuleController::getModuleRecord` | `GetModuleParams` |
| POST | `/V8/module` | `ModuleController::createModuleRecord` | `CreateModuleParams` |
| PATCH | `/V8/module` | `ModuleController::updateModuleRecord` | `UpdateModuleParams` |
| DELETE | `/V8/module/{moduleName}/{id}` | `ModuleController::deleteModuleRecord` | `DeleteModuleParams` |
| GET | `/V8/module/{moduleName}/{id}/relationships/{linkFieldName}` | `RelationshipController::getRelationship` | `GetRelationshipParams` |
| POST | `/V8/module/{moduleName}/{id}/relationships` | `RelationshipController::createRelationship` | `CreateRelationshipParams` |
| POST | `/V8/module/{moduleName}/{id}/relationships/{linkFieldName}` | `RelationshipController::createRelationshipByLink` | `CreateRelationshipByLinkParams` |
| DELETE | `/V8/module/{moduleName}/{id}/relationships/{linkFieldName}/{relatedBeanId}` | `RelationshipController::deleteRelationship` | `DeleteRelationshipParams` |
| * | `/V8/custom/**` | Routes personnalisées via `CustomLoader::loadCustomRoutes` | — |

---

## Interactions

- **Appelé par :** point d'entrée applicatif (INCONNU — probablement `Api/entryPoint.php`)
- **Appelle :** tous les contrôleurs V8, `ParamsMiddlewareFactory`, `CustomLoader`
- **Position dans le flux :** premier fichier de dispatch HTTP ; tout appel API passe par ces routes

---

## Notes

- Toutes les routes sous `/V8` sont protégées par `ResourceServerMiddleware` : un access token OAuth2 valide est obligatoire.
- La route `/access_token` est gérée directement par `AuthorizationServerMiddleware` (pas de contrôleur PHP explicite).
- Un groupe `/V8/custom` est réservé aux routes métier personnalisées chargées dynamiquement via `CustomLoader`.
- Le middleware de paramètres (`ParamsMiddlewareFactory::bind`) est instancié une fois puis réutilisé pour chaque route — pattern factory + bind.
