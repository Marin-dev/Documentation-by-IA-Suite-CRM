# 📄 NotEqualsOperator.php

**Chemin :** `lib/API/JsonApi/v1/Filters/Operators/Comparators/NotEqualsOperator.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Opérateur "différent de" pour les filtres JSON API. Mappe `[[ne]]` vers `!=` SQL.

## ⚙️ Rôle technique
Étend `Operator`, implémente `OperatorInterface`. `toFilterOperator()` retourne `[[ne]]`. `toSqlOperator()` retourne `!=`.

---

## 📤 Sorties / Exports
- `NotEqualsOperator` — classe
  - `toFilterOperator(): string` → `'[[ne]]'`
  - `toSqlOperator(): string` → `'!='`

---

## 💡 Points d'attention
- RAS. Voir `Operator.php` pour la logique commune.
