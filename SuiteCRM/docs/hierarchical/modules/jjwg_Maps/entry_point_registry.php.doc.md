# entry_point_registry.php (jjwg_Maps)

**Chemin :** `modules/jjwg_Maps/entry_point_registry.php`
**Type :** PHP — configuration
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Enregistre le point d'entree HTTP `jjwg_Maps` dans le registre SuiteCRM, pointant vers `jjwg_Maps_Router.php`.

**Type :** config

---

## Parametre

| Cle | Valeur |
|---|---|
| file | modules/jjwg_Maps/jjwg_Maps_Router.php |
| auth | false |

---

## Notes
- `auth => false` signifie que le point d'entree peut etre appele sans session authentifiee. A surveiller d'un point de vue securite.
