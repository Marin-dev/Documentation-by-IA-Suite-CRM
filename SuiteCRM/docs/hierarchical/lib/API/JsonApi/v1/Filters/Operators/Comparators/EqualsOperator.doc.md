# 📄 EqualsOperator.php

**Chemin :** `lib/API/JsonApi/v1/Filters/Operators/Comparators/EqualsOperator.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Opérateur d'égalité pour les filtres JSON API. Mappe `[[eq]]` (syntaxe filtre API) vers `=` (SQL).

## ⚙️ Rôle technique
Étend `Operator`, implémente `OperatorInterface`. `toFilterOperator()` retourne `[[eq]]`. `toSqlOperator()` retourne `=`.

---

## 📤 Sorties / Exports
- `EqualsOperator` — classe (opérateur)
  - `toFilterOperator(): string` → `'[[eq]]'`
  - `toSqlOperator(): string` → `'='`
- **Consommateurs identifiés :** enregistré dans le container `FilterOperators`

---

## 💡 Points d'attention
- RAS.
