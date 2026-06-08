# view.area_detail_map.config.php

**Chemin :** `modules/jjwg_Areas/views/view.area_detail_map.config.php`
**Type :** PHP — configuration de vue
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Configure la vue `area_detail_map` : desactive l'affichage de tous les elements standard de la vue (navigation, header, etc.) via `show_all => false`.

**Type :** config

---

## Parametres

| Parametre | Valeur | Effet |
|---|---|---|
| `$view_config['actions']['area_detail_map']['show_all']` | `false` | Masque les elements standard de la vue SugarView |

---

## Notes
- Fichier minimal ; permet d'afficher uniquement le contenu brut de la vue (utile pour les iframes).
