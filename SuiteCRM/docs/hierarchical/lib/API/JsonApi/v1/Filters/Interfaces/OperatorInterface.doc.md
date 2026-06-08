# 📄 OperatorInterface.php

**Chemin :** `lib/API/JsonApi/v1/Filters/Interfaces/OperatorInterface.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Contrat central pour tous les opérateurs de filtres JSON API. Définit comment un opérateur se représente en format filtre API, en SQL, comment il s'identifie et comment il construit ses opérandes SQL.

## ⚙️ Rôle technique
Interface avec quatre méthodes :
- `toFilterOperator(): string` — représentation dans la syntaxe filtre API (`[[eq]]`, `[[gt]]`, etc.)
- `toSqlOperator(): string` — représentation SQL (`=`, `>`, `LIKE`, etc.)
- `isOperator(string $operator): bool` — vérifie si la chaîne correspond à cet opérateur
- `toSqlOperands(array $operands): string` — construit la clause des opérandes SQL

---

## 📤 Sorties / Exports
- `OperatorInterface` — interface
- **Consommateurs identifiés :**
  - `lib/API/JsonApi/v1/Filters/Operators/Operator.php` (implémentation de base)
  - Tous les opérateurs Comparators et Strings
  - `lib/API/JsonApi/v1/Filters/Interpreters/FilterInterpreter.php`

## 🔗 Relations clés
- **Implémenté par :** `Operator` et ses sous-classes (`EqualsOperator`, `GreaterThanOperator`, `LikeOperator`, etc.)

---

## 💡 Points d'attention
- RAS.
