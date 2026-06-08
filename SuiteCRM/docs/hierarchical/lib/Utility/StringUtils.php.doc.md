# StringUtils.php

**Chemin :** `lib/Utility/StringUtils.php`
**Type :** PHP — Service utilitaire (methodes statiques)
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Boite a outils de manipulation de chaines. Permet de convertir des noms en camelCase vers snake_case ou vers des libelles traduits pour l'UI.

## Role technique
Trois methodes statiques. `explodeCamelCase()` extrait les composants d'un nom camelCase via regex. `camelToUnderscoreCase()` les joint avec `_`. `camelToTranslation()` essaie de trouver un label `LBL_CAMEL_TO_UPPER` via `translate()`, sinon retourne les mots en ucwords.

---

## Dependances cles
- `translate()` — fonction globale SuiteCRM
- PHP natif (regex, string functions)

## Exports / Symboles principaux
- `StringUtils` — classe statique
  - `static camelToUnderscoreCase(string $input, bool $uppercase = true): string`
  - `static camelToTranslation(string $input): string`
  - `static explodeCamelCase(string $input): array`

- **Consommateurs identifies :**
  - `lib/Search/UI/SearchFormView.php` (ligne 72)

---

## Points d'attention
- `camelToTranslation()` necessite l'initialisation des traductions SuiteCRM (`translate()` doit etre disponible).
