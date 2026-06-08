# 📄 helpers.php

**Chemin :** `Api/V8/Config/services/helpers.php`
**Type :** PHP (configuration — conteneur DI)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Enregistre les helpers utilitaires de l'API V8 dans le conteneur DI. Ces helpers sont des services transversaux utilisés pour construire les réponses JSON:API (attributs, relations, pagination) ainsi que pour introspection des VarDefs et liste des modules.

**Type :** config

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `Api\V8\BeanDecorator\BeanManager` | Résolution des beans (requis par `AttributeObjectHelper`) |
| `Api\V8\Helper` (namespace) | `VarDefHelper`, `ModuleListProvider` |
| `Api\V8\JsonApi\Helper` (namespace) | `AttributeObjectHelper`, `RelationshipObjectHelper`, `PaginationObjectHelper` |
| `Psr\Container\ContainerInterface` | Accès au conteneur |
| `Api\Core\Loader\CustomLoader` | Fusion avec helpers personnalisés |

---

## Helpers enregistrés

| Clé DI | Dépendances | Rôle |
|---|---|---|
| `VarDefHelper::class` | aucune | Introspection des définitions de champs (vardefs) |
| `AttributeObjectHelper::class` | `BeanManager` | Construction des `attributes` dans les réponses JSON:API |
| `RelationshipObjectHelper::class` | `VarDefHelper` | Construction des `relationships` dans les réponses JSON:API |
| `PaginationObjectHelper::class` | aucune | Construction des métadonnées de pagination |
| `ModuleListProvider::class` | aucune | Fournit la liste des modules disponibles |

---

## Interactions

- **Appelé par :** `Api/V8/Config/services.php` (via `require`)
- **`AttributeObjectHelper`** : consommé par `UserService`, `ModuleService`, `RelationshipService`, `ListViewService`
- **`RelationshipObjectHelper`** : consommé par `UserService`, `ModuleService`, `ListViewService`
- **`PaginationObjectHelper`** : consommé par `ModuleService`, `RelationshipService`, `ListViewService`
- **`ModuleListProvider`** : consommé par `MetaService`

---

## Notes

- `PaginationObjectHelper` n'a pas de dépendance injectée à la construction — ses méthodes reçoivent probablement les données en paramètre.
- `RelationshipObjectHelper` dépend de `VarDefHelper` plutôt que de `BeanManager` directement — il travaille sur les métadonnées de champs, pas les beans eux-mêmes.
