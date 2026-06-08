# Fichier : Relationship.php (container)

**Chemin :** `lib/API/v8/container/Relationship.php`
**Type :** PHP — configuration (DI factory)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Factory qui instancie `SuiteCRM\API\JsonApi\v1\Resource\Relationship` et l'enregistre dans le container DI sous la clé `'Relationship'`. Représente une relation JSON:API avec son nom, type, et ressources identifiants associées.

**Type :** configuration

---

## Ce que ce fichier configure

| Clé container | Classe instanciée | Services injectés |
|---|---|---|
| `Relationship` | `SuiteCRM\API\JsonApi\v1\Resource\Relationship` | `$container`, `LoggerInterface` |

---

## Interactions

**Consommé par :** `ModuleController::createModuleRelationship()`, `updateModuleRelationship()`, `deleteModuleRelationship()`
