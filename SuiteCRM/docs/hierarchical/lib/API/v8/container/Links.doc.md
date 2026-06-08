# Fichier : Links.php (container)

**Chemin :** `lib/API/v8/container/Links.php`
**Type :** PHP — configuration (DI factory)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Factory qui instancie `SuiteCRM\API\JsonApi\v1\Links` et l'enregistre dans le container DI sous la clé `'Links'`. Cet objet construit les objets `links` (self, first, last, prev, next) dans les réponses JSON:API.

**Type :** configuration

---

## Ce que ce fichier configure

| Clé container | Classe instanciée | Services injectés |
|---|---|---|
| `Links` | `SuiteCRM\API\JsonApi\v1\Links` | `LoggerInterface` |

---

## Interactions

**Consommé par :** `ModuleController::createModuleRecord()`
