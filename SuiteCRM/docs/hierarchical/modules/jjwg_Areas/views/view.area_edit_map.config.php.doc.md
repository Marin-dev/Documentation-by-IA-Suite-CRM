# view.area_edit_map.config.php

**Chemin :** `modules/jjwg_Areas/views/view.area_edit_map.config.php`
**Type :** PHP — configuration de vue
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Configure la vue `area_edit_map` : desactive l'affichage de tous les elements standard de la vue via `show_all => false`.

**Type :** config

---

## Parametres

| Parametre | Valeur | Effet |
|---|---|---|
| `$view_config['actions']['area_edit_map']['show_all']` | `false` | Masque les elements standard de la vue SugarView |

---

## Notes
- Analogue a `view.area_detail_map.config.php`. Permet l'utilisation en iframe.
