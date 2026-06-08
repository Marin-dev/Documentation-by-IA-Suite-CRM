# 📄 LessThanOperator.php

**Chemin :** `lib/API/JsonApi/v1/Filters/Operators/Comparators/LessThanOperator.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Opérateur "inférieur à" pour les filtres JSON API. Mappe `[[lt]]` vers `<` SQL.

## ⚙️ Rôle technique
Étend `Operator`, implémente `OperatorInterface`. `toFilterOperator()` retourne `[[lt]]`. `toSqlOperator()` retourne `<`.

---

## 📤 Sorties / Exports
- `LessThanOperator` — classe
  - `toFilterOperator(): string` → `'[[lt]]'`
  - `toSqlOperator(): string` → `'<'`

---

## 💡 Points d'attention
- RAS. Voir `Operator.php` pour la logique commune.
