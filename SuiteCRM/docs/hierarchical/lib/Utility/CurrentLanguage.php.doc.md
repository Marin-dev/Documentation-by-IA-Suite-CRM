# CurrentLanguage.php

**Chemin :** `lib/Utility/CurrentLanguage.php`
**Type :** PHP — Service helper
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Service minimal encapsulant la lecture de la langue courante de la session SuiteCRM (`$current_language`).

## Role technique
Une methode `getCurrentLanguage()` qui retourne le global `$current_language`. Abstraction de la variable globale pour faciliter les tests unitaires.

---

## Dependances cles
- Variable globale `$current_language`

## Exports / Symboles principaux
- `CurrentLanguage` — classe
  - `getCurrentLanguage(): mixed`

- **Consommateurs identifies :**
  - `lib/Utility/ApplicationLanguage.php`
  - `lib/Utility/ModuleLanguage.php`

---

## Points d'attention
- Simple wrapper sur une variable globale — utile pour l'injection de dependances dans les tests.
