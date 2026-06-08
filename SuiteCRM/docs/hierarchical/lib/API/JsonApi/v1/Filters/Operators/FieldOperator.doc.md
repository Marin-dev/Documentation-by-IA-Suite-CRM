# 📄 FieldOperator.php

**Chemin :** `lib/API/JsonApi/v1/Filters/Operators/FieldOperator.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Opérateur spécial représentant un identifiant de champ dans la syntaxe filtre JSON API (`[fieldname]` ou `[Module.fieldname]`). Valide et extrait les noms de champs depuis la structure de filtre.

## ⚙️ Rôle technique
Étend `Operator`. Utilise le format tag `[operator]` (simple crochet) et la regex `\[[A-Za-z0-9\_\-\.]+\]`. `isOperator()` délègue à `isValid()`. `totalOperands()` retourne 0 (un champ ne consomme pas d'opérandes).

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `SuiteCRM\API\JsonApi\v1\Filters\Operators\Operator`
  - `SuiteCRM\Exception\InvalidArgumentException`

## 📤 Sorties / Exports
- `FieldOperator` — classe (opérateur)
  - Hérite de `Operator`
  - `isValid(string $operator): bool`
  - `isOperator(string $operator): bool`
  - `totalOperands(): int` (0)
- **Consommateurs identifiés :**
  - `FilterInterpreter`, `FilterParser`, `FieldValidator`

## 🔗 Relations clés
- **Étendu de :** `Operator`
- **Utilisé par :** `FilterInterpreter`, `FilterParser`, `FieldValidator`

---

## 💡 Points d'attention
- Supporte les noms de champs avec `.` (ex: `[Accounts.name]`) — utilisé pour les filtres relationnels.
