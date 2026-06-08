# 📄 LikeOperator.php

**Chemin :** `lib/API/JsonApi/v1/Filters/Operators/Strings/LikeOperator.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Opérateur "LIKE" pour les filtres JSON API sur les chaînes de caractères. Mappe `[[li]]` vers `LIKE` SQL. Utilisé pour les recherches partielles de texte.

## ⚙️ Rôle technique
Étend `Operator`, implémente `OperatorInterface`. `toFilterOperator()` retourne `[[li]]`. `toSqlOperator()` retourne `LIKE`.

---

## 📤 Sorties / Exports
- `LikeOperator` — classe
  - `toFilterOperator(): string` → `'[[li]]'`
  - `toSqlOperator(): string` → `'LIKE'`

---

## 💡 Points d'attention
- Les jokers SQL (`%`, `_`) doivent être fournis dans la valeur de l'opérande par le client — non ajoutés automatiquement.
