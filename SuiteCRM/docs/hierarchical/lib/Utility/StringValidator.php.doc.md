# StringValidator.php

**Chemin :** `lib/Utility/StringValidator.php`
**Type :** PHP — Service utilitaire (methodes statiques)
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Validateur de chaines simple fournissant `startsWith()` et `endsWith()`. Utilitaire de bas niveau pour les comparaisons de prefixes/suffixes.

## Role technique
Deux methodes statiques. Valident le type (`is_string`) et lancent `InvalidArgumentException` si les arguments ne sont pas des chaines. Comparaison via `substr()`.

---

## Dependances cles
- PHP natif (`substr`, `strlen`)
- `\InvalidArgumentException`

## Exports / Symboles principaux
- `StringValidator` — classe statique
  - `static startsWith(string $haystack, string $needle): bool`
  - `static endsWith(string $haystack, string $needle): bool`

- **Consommateurs identifies :** INCONNU

---

## Points d'attention
- `endsWith()` retourne `true` si `$needle` est vide (ligne 86 : `$length === 0`).
- PHP 8+ a `str_starts_with()` et `str_ends_with()` nativement — cette classe pourrait devenir obsolete.
