# 📄 Operator.php

**Chemin :** `lib/API/JsonApi/v1/Filters/Operators/Operator.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Classe de base pour tous les opérateurs de filtres JSON API. Gère le format tag `[[operator]]` et la construction des opérandes SQL avec échappement.

## ⚙️ Rôle technique
Implémente la logique commune : conversion en tag filtre (`[[eq]]`, `[[gt]]`...), extraction du nom depuis un tag, détection d'opérateur par regex, construction des opérandes SQL via `DBManager::quote()`. La limite d'opérandes est de 1 par défaut (`totalOperands(): int`). Les sous-classes surchargent `toFilterOperator()` et `toSqlOperator()`.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `Psr\Container\ContainerInterface`
  - `SuiteCRM\API\v8\Exception\BadRequestException`
  - `SuiteCRM\Exception\InvalidArgumentException`
  - `DatabaseManager` (depuis container) — pour l'échappement SQL

## 📤 Sorties / Exports
- `Operator` — classe (base)
  - `toFilterTag(string $operator): string`
  - `stripFilterTag(string $operator): string`
  - `isValid(string $operator): bool`
  - `isOperator(string $operator): bool`
  - `hasOperator(string $filter): bool`
  - `totalOperands(): int` (retourne 1)
  - `toSqlOperands(array $operands): string`
- **Consommateurs identifiés :**
  - Toutes les classes `*Operator` du dossier `Comparators/` et `Strings/`
  - `FilterInterpreter`, `FilterParser`

## 🔗 Relations clés
- **Étendu par :** `EqualsOperator`, `GreaterThanOperator`, `GreaterThanOrEqualsOperator`, `InOperator`, `LessThanOperator`, `LessThanOrEqualsOperator`, `NotEqualsOperator`, `NotInOperator`, `LikeOperator`, `NotLikeOperator`, `FieldOperator`, `SpecialOperator`

---

## 💡 Points d'attention
- `toSqlOperands()` appelle `$db->checkConnection()` à chaque exécution — attention aux performances sous haute charge.
- `toFilterOperator()` n'est pas définie dans cette classe de base (retourne INCONNU si appelée directement) — méthode abstraite manquante.
