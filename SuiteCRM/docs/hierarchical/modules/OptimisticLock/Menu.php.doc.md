# Menu.php (OptimisticLock)

**Chemin :** `modules/OptimisticLock/Menu.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role
Definit le menu de navigation du module OptimisticLock. Le menu est vide — ce module n'expose aucune action utilisateur directe dans la navigation.

**Type :** config (menu module)

---

## Dependances cles
- Aucune

## Exports / Symboles principaux
- `$module_menu` — tableau vide

## Interactions
- **Appele par :** framework SuiteCRM pour construire la navigation du module
- **Appelle :** rien

## Notes
- Menu intentionnellement vide : OptimisticLock est un module technique interne, accessible uniquement via redirect depuis les logiques de conflit de sauvegarde.
