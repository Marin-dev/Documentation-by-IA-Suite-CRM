# actiondefs.php

**Chemin :** `modules/ACLActions/actiondefs.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Definit les constantes de niveaux d'acces ACL et le tableau global `$ACLActions` qui decrit les actions possibles par type (module, field) avec leurs valeurs par defaut et niveaux acceptes. Reference centrale du systeme ACL.

## Type
config / definitions

## Exports / Symboles principaux
- Constantes : `ACL_ALLOW_ADMIN_DEV=100`, `ACL_ALLOW_ADMIN=99`, `ACL_ALLOW_ALL=90`, `ACL_ALLOW_ENABLED=89`, `ACL_ALLOW_OWNER=75`, `ACL_ALLOW_NORMAL=1`, `ACL_ALLOW_DEFAULT=0`, `ACL_ALLOW_DISABLED=-98`, `ACL_ALLOW_NONE=-99`, `ACL_ALLOW_DEV=95`
- `$GLOBALS['ACLActionAccessLevels']` — descriptions de rendu (couleur, label) par niveau
- `$GLOBALS['ACLActions']` — actions par type : actions `list`, `view`, `edit`, `delete`, `export`, `import`, `access` (module) ; actions field (INCONNU — non lu entierement)

## Interactions
- **Appele par :** `ACLAction.php` (require au chargement), `ACLController.php`

## Notes
- Peut etre surcharge par `actiondefs.override.php` (cree par SecurityGroups).
