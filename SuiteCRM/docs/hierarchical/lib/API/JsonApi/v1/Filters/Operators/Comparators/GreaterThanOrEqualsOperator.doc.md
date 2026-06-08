# 📄 GreaterThanOrEqualsOperator.php

**Chemin :** `lib/API/JsonApi/v1/Filters/Operators/Comparators/GreaterThanOrEqualsOperator.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Opérateur "supérieur ou égal" pour les filtres JSON API. Mappe `[[gte]]` vers `>=` SQL.

## ⚙️ Rôle technique
Étend `Operator`, implémente `OperatorInterface`. `toFilterOperator()` retourne `[[gte]]`. `toSqlOperator()` retourne `>=`.

---

## 📤 Sorties / Exports
- `GreaterThanOrEqualsOperator` — classe (opérateur)
  - `toFilterOperator(): string` → `'[[gte]]'`
  - `toSqlOperator(): string` → `'>='`

---

## 💡 Points d'attention
- RAS. Voir `Operator.php` pour la logique commune.
