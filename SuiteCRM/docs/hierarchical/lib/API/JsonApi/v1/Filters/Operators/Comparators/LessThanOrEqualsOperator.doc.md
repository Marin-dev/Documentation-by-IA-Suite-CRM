# 📄 LessThanOrEqualsOperator.php

**Chemin :** `lib/API/JsonApi/v1/Filters/Operators/Comparators/LessThanOrEqualsOperator.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Opérateur "inférieur ou égal" pour les filtres JSON API. Mappe `[[lte]]` vers `<=` SQL.

## ⚙️ Rôle technique
Étend `Operator`, implémente `OperatorInterface`. `toFilterOperator()` retourne `[[lte]]`. `toSqlOperator()` retourne `<=`.

---

## 📤 Sorties / Exports
- `LessThanOrEqualsOperator` — classe
  - `toFilterOperator(): string` → `'[[lte]]'`
  - `toSqlOperator(): string` → `'<='`

---

## 💡 Points d'attention
- RAS. Voir `Operator.php` pour la logique commune.
