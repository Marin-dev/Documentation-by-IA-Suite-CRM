# 📄 InOperator.php

**Chemin :** `lib/API/JsonApi/v1/Filters/Operators/Comparators/InOperator.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Opérateur "IN" pour les filtres JSON API. Mappe `[[in]]` vers `IN (...)` SQL. Supporte jusqu'à 255 opérandes.

## ⚙️ Rôle technique
Étend `Operator`, implémente `OperatorInterface`. Override `totalOperands()` (retourne 255). Override `toSqlOperands()` pour encapsuler les valeurs dans des parenthèses : `IN ("v1","v2",...)`.

---

## 📤 Sorties / Exports
- `InOperator` — classe (opérateur)
  - `toFilterOperator(): string` → `'[[in]]'`
  - `toSqlOperator(): string` → `'IN'`
  - `totalOperands(): int` → `255`
  - `toSqlOperands(array): string` → `'("v1","v2",...)'`

---

## 💡 Points d'attention
- Limite arbitraire de 255 opérandes — peut causer des erreurs SQL si dépassée sur certains moteurs DB.
