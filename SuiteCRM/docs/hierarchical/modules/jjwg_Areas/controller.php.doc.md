# controller.php (jjwg_Areas)

**Chemin :** `modules/jjwg_Areas/controller.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Controleur MVC du module jjwg_Areas. Gere les actions specifiques d'affichage de carte pour une zone : vue detail et vue edition du polygone.

**Type :** controller

---

## Dependances cles
- `include/utils.php` — fonctions utilitaires SuiteCRM (`get_module_info`, `is_guid`)
- `SugarController` — classe parente du controleur
- `jjwg_Areas` — bean charge via `get_module_info('jjwg_Areas')`

---

## Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `jjwg_AreasController` | Classe | Controleur du module |
| `action_area_edit_map()` | Methode | Charge le bean zone, calcule le polygone et la location, assigne a `$GLOBALS['polygon']` et `$GLOBALS['loc']`, puis route vers la vue `area_edit_map` |
| `action_area_detail_map()` | Methode | Identique mais route vers la vue `area_detail_map` (lecture seule) |

---

## Interactions
- **Appelle :** `get_module_info('jjwg_Areas')`, `jjwg_Areas::retrieve()`, `jjwg_Areas::define_polygon()`, `jjwg_Areas::define_area_loc()`
- **Appele par :** Framework SuiteCRM (dispatcher MVC) via `?module=jjwg_Areas&action=area_edit_map` ou `area_detail_map`
- **Passe des donnees a :** `Jjwg_AreasViewArea_Edit_Map` et `Jjwg_AreasViewArea_Detail_Map` via `$GLOBALS`

---

## Notes
- Utilise `$_REQUEST['id']` pour identifier la zone ; valide avec `is_guid()`.
- Les donnees du polygone et de localisation sont transmises via `$GLOBALS` (couplage fort avec les vues).
