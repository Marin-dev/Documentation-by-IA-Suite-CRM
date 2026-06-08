# Menu.php

**Chemin :** `modules/Import/Menu.php`
**Type :** PHP - Configuration (menu)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Fichier de menu du module Import. Initialise `$module_menu` à un tableau vide — le menu est géré via la méthode `getMenu()` de la vue (override dans `ImportView`).

## Type
config

## Dépendances clés
Aucune.

## Exports / Symboles principaux
- `$module_menu` (tableau vide)

## Interactions
- **Appelé par :** framework SugarCRM (chargement du menu du module)
- **Appelle :** rien

## Notes
- Volontairement vide : le menu réel est délégué à la vue ImportView via `getMenu()`.
