# 📄 params.php

**Chemin :** `Api/V8/Config/services/params.php`
**Type :** PHP (configuration — conteneur DI)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Enregistre dans le conteneur DI toutes les classes de paramètres (`Param\*`) utilisées comme middlewares de validation pour chaque route de l'API V8. Chaque classe `Param` reçoit un `ValidatorFactory` et un `BeanManager`.

**Type :** config

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `Api\V8\BeanDecorator\BeanManager` | Validation des noms de modules et attributs |
| `Api\V8\Factory\ValidatorFactory` | Création des closures de validation Symfony |
| `Api\V8\Param` (namespace) | Toutes les classes `*Params` |
| `Psr\Container\ContainerInterface` | Accès au conteneur |
| `Api\Core\Loader\CustomLoader` | Fusion avec params personnalisés |

---

## Params enregistrés

| Clé DI | Route associée |
|---|---|
| `ListViewSearchParams::class` | `GET /V8/search-defs/module/{moduleName}` |
| `GetUserPreferencesParams::class` | `GET /V8/user-preferences/{id}` |
| `ListViewColumnsParams::class` | `GET /V8/listview/columns/{moduleName}` |
| `GetModuleParams::class` | `GET /V8/module/{moduleName}/{id}` |
| `GetModulesParams::class` | `GET /V8/module/{moduleName}` |
| `CreateModuleParams::class` | `POST /V8/module` |
| `UpdateModuleParams::class` | `PATCH /V8/module` |
| `DeleteModuleParams::class` | `DELETE /V8/module/{moduleName}/{id}` |
| `GetRelationshipParams::class` | `GET /V8/module/{moduleName}/{id}/relationships/{linkFieldName}` |
| `CreateRelationshipParams::class` | `POST /V8/module/{moduleName}/{id}/relationships` |
| `CreateRelationshipByLinkParams::class` | `POST /V8/module/{moduleName}/{id}/relationships/{linkFieldName}` |
| `DeleteRelationshipParams::class` | `DELETE /V8/module/{moduleName}/{id}/relationships/{linkFieldName}/{relatedBeanId}` |
| `GetFieldListParams::class` | `GET /V8/meta/fields/{moduleName}` |

---

## Interactions

- **Appelé par :** `Api/V8/Config/services.php` (via `require`)
- **Consommé par :** `ParamsMiddlewareFactory::bind()` dans `routes.php` — résout la classe `Param` depuis le conteneur et l'attache comme middleware à la route

---

## Notes

- Toutes les instances `Param\*` reçoivent les mêmes deux dépendances : `ValidatorFactory` et `BeanManager`.
- C'est `CustomLoader::mergeCustomArray` qui permet d'ajouter des params pour des routes personnalisées.
