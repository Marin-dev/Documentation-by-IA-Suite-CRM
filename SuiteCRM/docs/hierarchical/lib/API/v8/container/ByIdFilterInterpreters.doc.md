# Fichier : ByIdFilterInterpreters.php (container)

**Chemin :** `lib/API/v8/container/ByIdFilterInterpreters.php`
**Type :** PHP — configuration (DI factory)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Factory qui enregistre dans le container DI sous la clé `'ByIdFilterInterpreter'` un interpréteur de filtre par ID. Utilisé pour filtrer les enregistrements par leur identifiant.

**Type :** configuration

---

## Ce que ce fichier configure

| Clé container | Classe instanciée | Services injectés |
|---|---|---|
| `ByIdFilterInterpreter` | `SuiteCRM\API\JsonApi\v1\Filters\Interpreters\ByIdFilters\ByIdFilter` | `$container` |

---

## Interactions

**Consommé par :** `FilterInterpreter` (indirectement via le container)
