# Fichier : FilterInterpreter.php (container)

**Chemin :** `lib/API/v8/container/FilterInterpreter.php`
**Type :** PHP — configuration (DI factory)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Factory qui instancie `SuiteCRM\API\JsonApi\v1\Filters\Interpreters\FilterInterpreter` et l'enregistre dans le container DI sous la clé `'FilterInterpreter'`. Orchestre la détection et l'interprétation du type de filtre JSON:API (by-id, by-attributes, by-pre-made-name).

**Type :** configuration

---

## Ce que ce fichier configure

| Clé container | Classe instanciée | Services injectés |
|---|---|---|
| `FilterInterpreter` | `SuiteCRM\API\JsonApi\v1\Filters\Interpreters\FilterInterpreter` | `$container` |

---

## Interactions

**Consommé par :** `ModulesLib::getModuleList()` — détection de la stratégie de filtrage
