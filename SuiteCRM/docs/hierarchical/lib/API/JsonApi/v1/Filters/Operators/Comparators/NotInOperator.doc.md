# 📄 NotInOperator.php

**Chemin :** `lib/API/JsonApi/v1/Filters/Operators/Comparators/NotInOperator.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Opérateur "NOT IN" pour les filtres JSON API. Mappe `[[nin]]` vers `NOT IN (...)` SQL.

## ⚙️ Rôle technique
Étend `Operator`, implémente `OperatorInterface`. Override `toSqlOperands()` pour encapsuler dans des parenthèses : `NOT IN ("v1","v2",...)`.

---

## 📤 Sorties / Exports
- `NotInOperator` — classe
  - `toFilterOperator(): string` → `'[[nin]]'`
  - `toSqlOperator(): string` → `'NOT IN'`
  - `toSqlOperands(array): string` → `'("v1","v2",...)'`

---

## 💡 Points d'attention
- RAS. Voir `Operator.php` pour la logique commune et la limite d'opérandes.
