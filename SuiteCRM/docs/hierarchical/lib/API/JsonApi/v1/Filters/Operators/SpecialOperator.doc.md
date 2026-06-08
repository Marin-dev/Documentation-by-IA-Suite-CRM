# 📄 SpecialOperator.php

**Chemin :** `lib/API/JsonApi/v1/Filters/Operators/SpecialOperator.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Représente les opérateurs spéciaux à triple crochet (`[[[operator]]]`) dans la syntaxe filtre JSON API. Ces opérateurs encodent des comportements particuliers (ex: opérations sur null, EXISTS) distincts des comparateurs standards.

## ⚙️ Rôle technique
Étend `Operator`. Overrides le tag (`[[[operator]]]`), la regex (`\[\[\[[A-Za-z\_\-]+\]\]\]`), `isOperator()` (utilise regex triple crochet en plus de `isValid()`), et `totalOperands()` (retourne 0).

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `SuiteCRM\API\JsonApi\v1\Filters\Operators\Operator`
  - `SuiteCRM\Exception\InvalidArgumentException`

## 📤 Sorties / Exports
- `SpecialOperator` — classe (opérateur)
  - Hérite de `Operator`
  - `isValid(string): bool`
  - `isOperator(string): bool`
  - `totalOperands(): int` (0)
- **Consommateurs identifiés :**
  - `FilterInterpreter`, `FilterParser`, `SpecialOperatorValidator`

---

## 💡 Points d'attention
- Aucune implémentation concrète de `SpecialOperator` trouvée dans le périmètre analysé — semble être une extension point pour des opérateurs futurs ou personnalisés.
