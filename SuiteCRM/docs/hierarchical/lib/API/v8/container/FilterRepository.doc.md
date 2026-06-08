# Fichier : FilterRepository.php (container)

**Chemin :** `lib/API/v8/container/FilterRepository.php`
**Type :** PHP — configuration (DI factory)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Factory qui instancie `SuiteCRM\API\JsonApi\v1\Repositories\FilterRepository` et l'enregistre dans le container DI sous la clé `'FilterRepository'`. Extrait la structure de filtre depuis les paramètres de la requête HTTP.

**Type :** configuration

---

## Ce que ce fichier configure

| Clé container | Classe instanciée | Services injectés |
|---|---|---|
| `FilterRepository` | `SuiteCRM\API\JsonApi\v1\Repositories\FilterRepository` | `$container` |

---

## Interactions

**Consommé par :** `ModulesLib::getModuleList()` — extraction du filtre de la requête
