# Fichier : ModuleController.php

**Chemin :** `lib/API/v8/Controller/ModuleController.php`
**Type :** PHP — controller
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Contrôleur principal de l'API v8 pour toutes les opérations CRUD sur les modules SuiteCRM. Il expose les endpoints permettant de lire, créer, mettre à jour et supprimer des enregistrements (beans) et leurs relations, ainsi que des endpoints méta (liste des modules, menus, favoris, éléments consultés récemment, layouts, langue, attributs).

**Type :** controller

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `BeanFactory` | Création / récupération de beans SugarCRM |
| `SugarBean` | Type de base des enregistrements |
| `SuiteCRM\API\v8\Library\ModulesLib` | Helper : pagination, filtrage, liens |
| `SuiteCRM\API\JsonApi\v1\Resource\SuiteBeanResource` | Sérialisation bean → JSON:API |
| `SuiteCRM\API\JsonApi\v1\Resource\Relationship` | Gestion des relations JSON:API |
| `SuiteCRM\API\JsonApi\v1\Links` | Construction des objets `links` |
| `SuiteCRM\API\v8\Exception\*` | Exceptions métier (400, 403, 404, 409…) |
| `SugarView` | Récupération des menus par module |
| `Favorites` / `Tracker` | Favoris et historique de consultation |
| `GroupedTabStructure` | Structure des onglets groupés |
| `ParserFactory` | Parseur de layouts de vues |

---

## Exports / Symboles principaux

| Méthode | Route | Verbe | Description |
|---|---|---|---|
| `getModulesMetaList` | `/api/v8/modules/meta/list` | GET | Liste de tous les modules disponibles |
| `getModulesMetaMenuModules` | `/api/v8/modules/meta/menu/modules` | GET | Menus de tous les modules |
| `getModulesMetaMenuFilters` | `/api/v8/modules/meta/menu/filters` | GET | Filtres/onglets de navigation |
| `getModulesMetaViewed` | `/api/v8/modules/viewed` | GET | Éléments consultés récemment (tous modules) |
| `getModulesMetaFavorites` | `/api/v8/modules/favorites` | GET | Favoris de l'utilisateur (tous modules) |
| `getModuleRecords` | `/api/v8/modules/{module}` | GET | Liste paginée des enregistrements d'un module |
| `createModuleRecord` | `/api/v8/modules/{module}` | POST | Créer un enregistrement |
| `getModuleRecord` | `/api/v8/modules/{module}/{id}` | GET | Lire un enregistrement |
| `updateModuleRecord` | `/api/v8/modules/{module}/{id}` | PATCH | Mettre à jour un enregistrement |
| `deleteModuleRecord` | `/api/v8/modules/{module}/{id}` | DELETE | Supprimer (soft-delete) un enregistrement |
| `getModuleMetaLanguage` | `/api/v8/modules/{module}/meta/language` | GET | Chaînes de traduction d'un module |
| `getApplicationMetaLanguages` | `/api/v8/meta/languages` | GET | Chaînes de traduction de l'application |
| `getModuleMetaAttributes` | `/api/v8/modules/{module}/meta/attributes` | GET | `field_defs` du bean |
| `getModuleMetaLayout` | `/api/v8/modules/{module}/meta/view/{view}` | GET | Layout d'une vue (via ParserFactory) |
| `getModuleRelationship` | `/api/v8/modules/{module}/{id}/relationships/{link}` | GET | Lire une relation |
| `createModuleRelationship` | `/api/v8/modules/{module}/{id}/relationships/{link}` | POST | Créer une relation |
| `updateModuleRelationship` | `/api/v8/modules/{module}/{id}/relationships/{link}` | PATCH | Mettre à jour une relation |
| `deleteModuleRelationship` | `/api/v8/modules/{module}/{id}/relationships/{link}` | DELETE | Supprimer une relation |

---

## Interactions

**Appelé par :**
- `lib/API/v8/route/moduleRoutes.php` (mapping routes → méthodes)
- `lib/API/v8/container/ModuleController.php` (instanciation DI)

**Appelle :**
- `BeanFactory::newBean()` / `BeanFactory::getBean()` — accès aux beans SugarCRM
- `ModulesLib::generatePaginatedModuleRecords()` / `generatePaginatedLinksFromModuleRecords()` (pagination)
- `SugarBean::ACLAccess()` — vérification des droits ACL
- `ApiController::generateJsonApiResponse()` / `generateJsonApiErrorResponse()` (héritage)
- Containers DI : `SuiteBeanResource`, `Resource`, `Relationship`, `ResourceIdentifier`, `Links`, `ConfigurationManager`, `DateTimeConverter`, `CurrentLanguage`, `ModuleLanguage`, `ApplicationLanguages`

---

## Notes

- La suppression est un **soft-delete** : `$sugarBean->deleted = 1; $sugarBean->save()` — ligne 701-703.
- `createModuleRecord` vérifie l'existence d'un bean avec l'ID fourni et lève `IdAlreadyExistsException` — ligne 455.
- Les query params `include` et `filter` dans `getModuleRecord` lèvent `BadRequestException` (non implémentés) — lignes 511-520.
- Les relations to-many et to-one sont gérées via le switch sur `SugarBeanRelationshipType::fromSugarBeanLink()` — logique complexe aux lignes 1068-1145, 1236-1333.
- `getModuleMetaFields` est un alias de `getModuleMetaAttributes` (ligne 820).
- Les variables globales `$current_user`, `$sugar_config`, `$app_strings` sont utilisées directement — couplage fort avec l'environnement global SuiteCRM.
