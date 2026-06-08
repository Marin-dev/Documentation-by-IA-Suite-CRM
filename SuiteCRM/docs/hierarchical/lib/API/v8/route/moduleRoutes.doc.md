# Fichier : moduleRoutes.php

**Chemin :** `lib/API/v8/route/moduleRoutes.php`
**Type :** PHP — configuration (routes)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit toutes les routes Slim de l'API v8 relatives aux modules CRM. Mappe chaque URL vers la méthode correspondante de `ModuleController`. Couvre les opérations CRUD sur les enregistrements, les métadonnées (menus, layouts, langue, attributs) et les relations.

**Type :** configuration

---

## Ce que ce fichier configure

Groupe de routes sous le préfixe `/v8/modules`, toutes routées vers `ModuleController`.

### Tableau des routes définies

| Route | Verbe | Handler |
|---|---|---|
| `/v8/modules/viewed` | GET | `getModulesMetaViewed` |
| `/v8/modules/favorites` | GET | `getModulesMetaFavorites` |
| `/v8/modules/meta/list` | GET | `getModulesMetaList` |
| `/v8/modules/meta/menu/modules` | GET | `getModulesMetaMenuModules` |
| `/v8/modules/meta/menu/filters` | GET | `getModulesMetaMenuFilters` |
| `/v8/modules/meta/languages` | GET | `getApplicationMetaLanguages` |
| `/v8/modules/{module}` | GET | `getModuleRecords` |
| `/v8/modules/{module}` | POST | `createModuleRecord` |
| `/v8/modules/{module}/viewed` | GET | `getModuleRecordsViewed` |
| `/v8/modules/{module}/favorites` | GET | `getModuleFavorites` |
| `/v8/modules/{module}/meta/language` | GET | `getModuleMetaLanguage` |
| `/v8/modules/{module}/meta/attributes` | GET | `getModuleMetaFields` |
| `/v8/modules/{module}/meta/menu` | GET | `getModuleMetaMenu` |
| `/v8/modules/{module}/meta/view/{view}` | GET | `getModuleMetaLayout` |
| `/v8/modules/{module}/{id}` | GET | `getModuleRecord` |
| `/v8/modules/{module}/{id}` | PATCH | `updateModuleRecord` |
| `/v8/modules/{module}/{id}` | DELETE | `deleteModuleRecord` |
| `/v8/modules/{module}/{id}/relationships/{link}` | GET | `getModuleRelationship` |
| `/v8/modules/{module}/{id}/relationships/{link}` | POST | `createModuleRelationship` |
| `/v8/modules/{module}/{id}/relationships/{link}` | PATCH | `updateModuleRelationship` |
| `/v8/modules/{module}/{id}/relationships/{link}` | DELETE | `deleteModuleRelationship` |

---

## Interactions

- **Consomme :** `ModuleController` (résolu via DI)
- **Inclus par :** INCONNU — bootstrap de l'application API

---

## Notes

- Le fichier opère sur `$app` (instance Slim) disponible dans le contexte d'inclusion via `use ($app)`.
- L'ordre de déclaration des routes est important : `/viewed` et `/favorites` doivent être définis **avant** `/{module}` pour éviter que Slim interprète `viewed` comme un nom de module.
