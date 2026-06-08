# 📄 OperatorValidator.php

**Chemin :** `lib/API/JsonApi/v1/Filters/Validators/OperatorValidator.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Validateur d'opérateurs de filtres JSON API. Censé vérifier qu'une chaîne est un opérateur valide.

## ⚙️ Rôle technique
Implémente `ValidatorInterface`. Le code contient des **bugs** : `value` (sans `$`) en ligne 60 provoque une erreur PHP, et `$operator = new InvalidArgumentException()` (ligne 66) instancie une exception au lieu d'un opérateur — semble être un code non finalisé.

---

## 📤 Sorties / Exports
- `OperatorValidator` — classe (validateur, NON FONCTIONNEL)
  - `isValid($value)` — contient des bugs de développement

---

## 💡 Points d'attention
- **BUG CRITIQUE** : ligne 60 utilise `value` au lieu de `$value` (erreur PHP fatale à l'exécution). Ligne 66, instancie `InvalidArgumentException` à la place d'un opérateur. Cette classe ne fonctionne pas telle quelle.
- Non utilisée dans le code analysé — probablement jamais appelée.
