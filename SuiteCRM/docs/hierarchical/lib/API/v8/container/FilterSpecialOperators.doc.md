# Fichier : FilterSpecialOperators.php (container)

**Chemin :** `lib/API/v8/container/FilterSpecialOperators.php`
**Type :** PHP — configuration (DI factory)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Factory qui enregistre dans le container DI sous la clé `'FilterSpecialOperators'` un tableau contenant l'opérateur spécial (`SpecialOperator`). Gère les cas de filtrage non couverts par les opérateurs standard.

**Type :** configuration

---

## Ce que ce fichier configure

| Clé container | Type | Contenu |
|---|---|---|
| `FilterSpecialOperators` | `OperatorInterface[]` | `[SpecialOperator]` |

---

## Interactions

**Consommé par :** `FilterInterpreter` (indirectement via le container)
