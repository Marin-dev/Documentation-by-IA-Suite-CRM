# Fichier : ResourceIdentifier.php (container)

**Chemin :** `lib/API/v8/container/ResourceIdentifier.php`
**Type :** PHP — configuration (DI factory)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Factory qui instancie `SuiteCRM\API\JsonApi\v1\Resource\ResourceIdentifier` et l'enregistre dans le container DI sous la clé `'ResourceIdentifier'`. Représente un identifiant de ressource JSON:API (`{ id, type }`).

**Type :** configuration

---

## Ce que ce fichier configure

| Clé container | Classe instanciée | Services injectés |
|---|---|---|
| `ResourceIdentifier` | `SuiteCRM\API\JsonApi\v1\Resource\ResourceIdentifier` | `$container`, `LoggerInterface` |

---

## Interactions

**Consommé par :** `ModuleController::createModuleRelationship()`, `updateModuleRelationship()`
