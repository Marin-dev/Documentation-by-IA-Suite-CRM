# Menu.php (jjwg_Areas)

**Chemin :** `modules/jjwg_Areas/Menu.php`
**Type :** PHP — configuration
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Definit les entrees du menu de navigation du module jjwg_Areas, avec verification des droits ACL pour chaque action (creation, liste, import).

**Type :** config

---

## Dependances cles
- `ACLController::checkAccess()` — controle des droits

---

## Entrees de menu

| Label | Action | Droit requis |
|---|---|---|
| LNK_NEW_RECORD | EditView | edit |
| LNK_LIST | index (liste) | list |
| LBL_IMPORT | Import Step1 | import |

---

## Notes
- Fichier standard SuiteCRM pour les menus de modules. Pas de logique metier.
