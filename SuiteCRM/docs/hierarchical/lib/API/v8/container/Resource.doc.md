# Fichier : Resource.php (container)

**Chemin :** `lib/API/v8/container/Resource.php`
**Type :** PHP — configuration (DI factory)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Factory qui instancie `SuiteCRM\API\JsonApi\v1\Resource\Resource` et l'enregistre dans le container DI sous la clé `'Resource'`. Représente une ressource JSON:API générique (lecture/transformation depuis un payload request).

**Type :** configuration

---

## Ce que ce fichier configure

| Clé container | Classe instanciée | Services injectés |
|---|---|---|
| `Resource` | `SuiteCRM\API\JsonApi\v1\Resource\Resource` | `$container`, `LoggerInterface` |

---

## Interactions

**Consommé par :** `ModuleController::updateModuleRecord()`, `getModuleRelationship()`
