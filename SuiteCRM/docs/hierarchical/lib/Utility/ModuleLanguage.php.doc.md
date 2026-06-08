# ModuleLanguage.php

**Chemin :** `lib/Utility/ModuleLanguage.php`
**Type :** PHP — Service helper
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Service utilitaire pour charger les chaines de traduction d'un module specifique dans la langue courante de l'utilisateur.

## Role technique
Une methode `getModuleLanguageStrings()`. Appelle `return_module_language($lang, $moduleName)` (fonction globale SuiteCRM).

---

## Dependances cles
- `SuiteCRM\Utility\CurrentLanguage`
- `return_module_language()` (fonction globale SuiteCRM)

## Exports / Symboles principaux
- `ModuleLanguage` — classe helper
  - `getModuleLanguageStrings(CurrentLanguage $currentLanguage, string $moduleName): array`

---

## Points d'attention
- Complement de `ApplicationLanguage` : celui-ci est specifique a un module.
