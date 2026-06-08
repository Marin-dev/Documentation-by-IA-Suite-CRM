# ApplicationLanguage.php

**Chemin :** `lib/Utility/ApplicationLanguage.php`
**Type :** PHP — Service helper
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Service utilitaire pour charger les chaines de traduction de l'application (labels generaux + listes de valeurs) dans la langue courante de l'utilisateur.

## Role technique
Une methode `getApplicationLanguageStrings()`. Fusionne les resultats de `return_application_language()` et `return_app_list_strings_language()` via `array_merge()`.

---

## Dependances cles
- `SuiteCRM\Utility\CurrentLanguage`
- `return_application_language()` (fonction globale SuiteCRM)
- `return_app_list_strings_language()` (fonction globale SuiteCRM)

## Exports / Symboles principaux
- `ApplicationLanguage` — classe helper
  - `getApplicationLanguageStrings(CurrentLanguage $currentLanguage): array`

- **Consommateurs identifies :** INCONNU

---

## Points d'attention
- Dependances sur des fonctions globales SuiteCRM — necessite l'initialisation complete de l'application.
