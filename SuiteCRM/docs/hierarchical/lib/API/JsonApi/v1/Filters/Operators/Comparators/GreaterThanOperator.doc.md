# 📄 GreaterThanOperator.php

**Chemin :** `lib/API/JsonApi/v1/Filters/Operators/Comparators/GreaterThanOperator.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Opérateur "supérieur à" pour les filtres JSON API. Mappe `[[gt]]` vers `>` SQL.

## ⚙️ Rôle technique
Étend `Operator`, implémente `OperatorInterface`. `toFilterOperator()` retourne `[[gt]]`. `toSqlOperator()` retourne `>`.

---

## 📤 Sorties / Exports
- `GreaterThanOperator` — classe (opérateur)
  - `toFilterOperator(): string` → `'[[gt]]'`
  - `toSqlOperator(): string` → `'>'`

---

## 💡 Points d'attention
- RAS. Voir `Operator.php` pour la logique commune.
