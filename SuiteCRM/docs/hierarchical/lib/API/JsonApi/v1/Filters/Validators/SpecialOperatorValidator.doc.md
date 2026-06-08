# 📄 SpecialOperatorValidator.php

**Chemin :** `lib/API/JsonApi/v1/Filters/Validators/SpecialOperatorValidator.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Validateur pour les opérateurs spéciaux à triple crochet `[[[...]]]`.

## ⚙️ Rôle technique
Implémente `ValidatorInterface`. Contient également un **bug** : `value` (sans `$`) en ligne 62 et `$operator = new SpecialOperator()` sans passer le `ContainerInterface` requis par son constructeur — non fonctionnel tel quel.

---

## 📤 Sorties / Exports
- `SpecialOperatorValidator` — classe (validateur, NON FONCTIONNEL)
  - `isValid($value)` — contient des bugs

---

## 💡 Points d'attention
- **BUG** : même problème que `OperatorValidator` — `value` sans `$` en ligne 62. De plus, `SpecialOperator` requiert un `ContainerInterface` en constructeur mais est instancié sans argument (ligne 68).
- Import incorrect ligne 44 : `use SuiteCRM\API\JsonApi\v1\Filters\Operators\InvalidArgumentException` (classe inexistante à ce chemin).
