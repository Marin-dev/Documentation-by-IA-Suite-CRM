# routes.php

## Rôle
Fichier de déclaration de toutes les routes de l'API V8 SuiteCRM, basé sur le micro-framework Slim. Définit le routage REST (modules, relations, meta, auth) et applique les middlewares OAuth2 sur l'ensemble des routes protégées.

## Responsabilités
- Déclarer la route POST `/access_token` (émission de token OAuth2) protégée par `AuthorizationServerMiddleware`
- Grouper toutes les routes V8 sous le préfixe `/V8` avec protection `ResourceServerMiddleware`
- Enregistrer les routes CRUD sur les modules : GET liste, GET un enregistrement, POST création, PATCH mise à jour, DELETE suppression
- Enregistrer les routes de gestion des relations : GET, POST (par lien ou générique), DELETE
- Enregistrer les routes utilitaires : logout, current-user, meta (modules, champs, swagger), search-defs, listview
- Charger des routes personnalisées via `CustomLoader::loadCustomRoutes()` sous le préfixe `/V8/custom`
- Associer un middleware de validation des paramètres (`ParamsMiddlewareFactory`) à chaque route

## Dépendances internes
- `Api\V8\Controller\LogoutController` — route POST `/V8/logout`
- `Api\V8\Controller\ListViewSearchController` — route GET `/V8/search-defs/module/{moduleName}`
- `Api\V8\Controller\ListViewController` — route GET `/V8/listview/columns/{moduleName}`
- `Api\V8\Controller\UserController` — route GET `/V8/current-user`
- `Api\V8\Controller\MetaController` — routes GET `/V8/meta/modules`, `/V8/meta/fields/{moduleName}`, `/V8/meta/swagger.json`
- `Api\V8\Controller\UserPreferencesController` — route GET `/V8/user-preferences/{id}`
- `Api\V8\Controller\ModuleController` — routes CRUD `/V8/module`
- `Api\V8\Controller\RelationshipController` — routes relations `/V8/module/{moduleName}/{id}/relationships`
- `Api\V8\Factory\ParamsMiddlewareFactory` — binding des middlewares de validation par route
- `Api\V8\Param\*` — classes de paramètres liées à chaque route
- `Api\Core\Loader\CustomLoader` — chargement des routes custom
- `League\OAuth2\Server\AuthorizationServer` — middleware d'émission de token
- `League\OAuth2\Server\ResourceServer` — middleware de validation de token

## Exports / Points d'entrée
| Méthode | Chemin | Contrôleur::action |
|---------|--------|--------------------|
| POST | `/access_token` | AuthorizationServerMiddleware |
| POST | `/V8/logout` | LogoutController |
| GET | `/V8/search-defs/module/{moduleName}` | ListViewSearchController:getModuleSearchDefs |
| GET | `/V8/listview/columns/{moduleName}` | ListViewController:getListViewColumns |
| GET | `/V8/current-user` | UserController:getCurrentUser |
| GET | `/V8/meta/modules` | MetaController:getModuleList |
| GET | `/V8/meta/fields/{moduleName}` | MetaController:getFieldList |
| GET | `/V8/user-preferences/{id}` | UserPreferencesController:getUserPreferences |
| GET | `/V8/meta/swagger.json` | MetaController:getSwaggerSchema |
| GET | `/V8/module/{moduleName}` | ModuleController:getModuleRecords |
| GET | `/V8/module/{moduleName}/{id}` | ModuleController:getModuleRecord |
| POST | `/V8/module` | ModuleController:createModuleRecord |
| PATCH | `/V8/module` | ModuleController:updateModuleRecord |
| DELETE | `/V8/module/{moduleName}/{id}` | ModuleController:deleteModuleRecord |
| GET | `/V8/module/{moduleName}/{id}/relationships/{linkFieldName}` | RelationshipController:getRelationship |
| POST | `/V8/module/{moduleName}/{id}/relationships` | RelationshipController:createRelationship |
| POST | `/V8/module/{moduleName}/{id}/relationships/{linkFieldName}` | RelationshipController:createRelationshipByLink |
| DELETE | `/V8/module/{moduleName}/{id}/relationships/{linkFieldName}/{relatedBeanId}` | RelationshipController:deleteRelationship |

## Notes techniques
- Toutes les routes `/V8/*` sont protégées par `ResourceServerMiddleware` (validation JWT OAuth2).
- La route `/access_token` est hors groupe V8 et protégée par `AuthorizationServerMiddleware`.
- Les routes custom sont injectées dynamiquement via `CustomLoader::loadCustomRoutes()`.
- Ce fichier est le point d'entrée de routage — il est inclus depuis le bootstrap de l'application (INCONNU : chemin exact du bootstrap non vérifié ici).
