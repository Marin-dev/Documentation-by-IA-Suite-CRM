# Menu.php

**Chemin :** `modules/ProspectLists/Menu.php`
**Type :** PHP - Configuration (menu)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Définit le menu du module ProspectLists avec vérifications ACL : Créer et Liste.

## Type
config

## Dépendances clés
- `ACLController::checkAccess()`, `$mod_strings`

## Exports / Symboles principaux
- `$module_menu` — 2 entrées ACL conditionnelles

## Interactions
- **Appelé par :** framework SugarCRM
- **Appelle :** `ACLController::checkAccess()`
