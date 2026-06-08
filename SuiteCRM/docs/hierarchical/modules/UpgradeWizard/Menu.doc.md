# Menu.php

**Chemin :** `modules/UpgradeWizard/Menu.php`
**Type :** PHP - Configuration (menu)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Définit le menu du module UpgradeWizard en réutilisant celui du module Administration. Fusionne les chaînes de traduction Administration avec celles du module courant.

## Type
config

## Dépendances clés
- `modules/Administration/Menu.php` — menu inclus
- `return_module_language()`, `sugarArrayMerge()`

## Exports / Symboles principaux
- `$module_menu` (hérité de `modules/Administration/Menu.php`)

## Interactions
- **Appelé par :** framework SugarCRM (chargement du menu du module)
- **Appelle :** `modules/Administration/Menu.php`

## Notes
- Le menu UpgradeWizard est identique au menu Administration.
