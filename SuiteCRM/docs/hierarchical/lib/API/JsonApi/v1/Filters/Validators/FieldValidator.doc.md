# 📄 FieldValidator.php

**Chemin :** `lib/API/JsonApi/v1/Filters/Validators/FieldValidator.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Validateur de nom de champ dans la syntaxe filtre JSON API. Vérifie qu'un champ a le format `[fieldname]` ou `[Module.field]` valide.

## ⚙️ Rôle technique
Implémente `ValidatorInterface`. `isValid(string $fieldKey)` délègue à `FieldOperator::isValid()`.

---

## 📥 Entrées / Dépendances
- `Psr\Container\ContainerInterface`
- `SuiteCRM\API\JsonApi\v1\Filters\Operators\FieldOperator`
- `SuiteCRM\API\JsonApi\v1\Filters\Interfaces\ValidatorInterface`
- `SuiteCRM\Exception\InvalidArgumentException`

## 📤 Sorties / Exports
- `FieldValidator` — classe (validateur)
  - `isValid(string $fieldKey): bool`
- **Consommateurs identifiés :**
  - `FilterInterpreter`, `FilterParser`

---

## 💡 Points d'attention
- Délègue entièrement à `FieldOperator` — pas de logique propre.
