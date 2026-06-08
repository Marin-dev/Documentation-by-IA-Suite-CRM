# 📄 services.php (sous-dossier services)

**Chemin :** `Api/V8/Config/services/services.php`
**Type :** PHP (configuration — conteneur DI)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Enregistre dans le conteneur DI les services métier de l'API V8. Chaque service est instancié avec ses helpers et son `BeanManager`. Ce fichier constitue la couche "service" du pattern MVC de l'API.

**Type :** config

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `Api\V8\BeanDecorator\BeanManager` | Accès aux beans SuiteCRM |
| `Api\V8\Helper\ModuleListProvider` | Liste des modules disponibles |
| `Api\V8\JsonApi\Helper\{Attribute,Pagination,Relationship}ObjectHelper` | Builders de réponses JSON:API |
| `Api\V8\Service` (namespace) | Tous les services V8 |
| `Psr\Container\ContainerInterface` | Accès au conteneur |
| `Api\Core\Loader\CustomLoader` | Fusion avec services personnalisés |

---

## Services enregistrés

| Clé DI | Dépendances injectées |
|---|---|
| `ListViewSearchService::class` | `BeanManager` |
| `UserPreferencesService::class` | `BeanManager` |
| `UserService::class` | `BeanManager`, `AttributeObjectHelper`, `RelationshipObjectHelper` |
| `MetaService::class` | `BeanManager`, `ModuleListProvider` |
| `ListViewService::class` | `BeanManager`, `AttributeObjectHelper`, `RelationshipObjectHelper`, `PaginationObjectHelper` |
| `ModuleService::class` | `BeanManager`, `AttributeObjectHelper`, `RelationshipObjectHelper`, `PaginationObjectHelper` |
| `LogoutService::class` | `BeanManager` |
| `RelationshipService::class` | `BeanManager`, `AttributeObjectHelper`, `PaginationObjectHelper` |

---

## Interactions

- **Appelé par :** `Api/V8/Config/services.php` (via `require`)
- **Consommé par :** `controllers.php` — les contrôleurs résolvent leurs services depuis ce conteneur

---

## Notes

- `RelationshipService` ne reçoit pas `RelationshipObjectHelper` (contrairement à `ModuleService` et `ListViewService`) — cohérent avec son rôle limité aux relations inter-beans sans construction de réponses attributs complètes.
- `CustomLoader::mergeCustomArray` permet de surcharger ou d'ajouter des services métier.
