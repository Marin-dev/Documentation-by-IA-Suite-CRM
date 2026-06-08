# Fichier : FilterFieldOperators.php (container)

**Chemin :** `lib/API/v8/container/FilterFieldOperators.php`
**Type :** PHP — configuration (DI factory)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Factory qui enregistre dans le container DI sous la clé `'FilterFieldOperators'` un tableau contenant l'opérateur de champ (`FieldOperator`). Utilisé pour le filtrage par champs dans les filtres JSON:API.

**Type :** configuration

---

## Ce que ce fichier configure

| Clé container | Type | Contenu |
|---|---|---|
| `FilterFieldOperators` | `OperatorInterface[]` | `[FieldOperator]` |

---

## Interactions

**Consommé par :** `FilterInterpreter` (indirectement via le container)
