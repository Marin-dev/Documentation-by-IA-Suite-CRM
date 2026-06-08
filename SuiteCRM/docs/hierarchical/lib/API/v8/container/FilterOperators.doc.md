# Fichier : FilterOperators.php (container)

**Chemin :** `lib/API/v8/container/FilterOperators.php`
**Type :** PHP — configuration (DI factory)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Factory qui enregistre dans le container DI sous la clé `'FilterOperators'` un tableau d'opérateurs de comparaison pour les filtres JSON:API. Ces opérateurs sont utilisés lors du filtrage par attributs.

**Type :** configuration

---

## Ce que ce fichier configure

| Clé container | Type | Opérateurs inclus |
|---|---|---|
| `FilterOperators` | `OperatorInterface[]` | EQ, NEQ, GTE, GT, LTE, LT, IN, NOT IN, LIKE, NOT LIKE |

### Opérateurs enregistrés

| Classe | Opération |
|---|---|
| `EqualsOperator` | `=` |
| `NotEqualsOperator` | `!=` |
| `GreaterThanOrEqualsOperator` | `>=` |
| `GreaterThanOperator` | `>` |
| `LessThanOrEqualsOperator` | `<=` |
| `LessThanOperator` | `<` |
| `InOperator` | `IN (...)` |
| `NotInOperator` | `NOT IN (...)` |
| `LikeOperator` | `LIKE` |
| `NotLikeOperator` | `NOT LIKE` |

---

## Interactions

**Consommé par :** `FilterInterpreter` (indirectement via le container)
