# Fichier : SuiteBeanResource.php (container)

**Chemin :** `lib/API/v8/container/SuiteBeanResource.php`
**Type :** PHP — configuration (DI factory)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Factory qui instancie `SuiteCRM\API\JsonApi\v1\Resource\SuiteBeanResource` et l'enregistre dans le container DI sous la clé `'SuiteBeanResource'`. C'est le service central de conversion entre `SugarBean` et le format JSON:API.

**Type :** configuration

---

## Ce que ce fichier configure

| Clé container | Classe instanciée | Services injectés |
|---|---|---|
| `SuiteBeanResource` | `SuiteCRM\API\JsonApi\v1\Resource\SuiteBeanResource` | `$container`, `LoggerInterface` |

---

## Interactions

**Consommé par :** `ModuleController` (createModuleRecord, updateModuleRecord, getModuleRecord, createModuleRelationship, updateModuleRelationship), `ModulesLib::generatePaginatedModuleRecords()`
