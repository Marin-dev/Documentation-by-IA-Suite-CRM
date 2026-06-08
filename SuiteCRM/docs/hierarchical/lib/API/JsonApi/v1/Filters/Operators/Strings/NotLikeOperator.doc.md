# 📄 NotLikeOperator.php

**Chemin :** `lib/API/JsonApi/v1/Filters/Operators/Strings/NotLikeOperator.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Opérateur "NOT LIKE" pour les filtres JSON API. Mappe `[[nli]]` vers `NOT LIKE` SQL. Utilisé pour exclure les enregistrements dont un champ texte correspond à un motif.

## ⚙️ Rôle technique
Étend `Operator`, implémente `OperatorInterface`. `toFilterOperator()` retourne `[[nli]]`. `toSqlOperator()` retourne `NOT LIKE`.

---

## 📤 Sorties / Exports
- `NotLikeOperator` — classe
  - `toFilterOperator(): string` → `'[[nli]]'`
  - `toSqlOperator(): string` → `'NOT LIKE'`

---

## 💡 Points d'attention
- Même remarque que `LikeOperator` : les jokers doivent être inclus par le client.
