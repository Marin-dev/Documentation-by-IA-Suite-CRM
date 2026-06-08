# controller.php (jjwg_Markers)

**Chemin :** `modules/jjwg_Markers/controller.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Controleur MVC du module jjwg_Markers. Gere les actions d'affichage de carte pour un marqueur : vue detail (lecture seule) et vue edition (marqueur draggable).

**Type :** controller

---

## Dependances cles
- `include/utils.php`
- `SugarController`
- `jjwg_Markers` — charge via `get_module_info('jjwg_Markers')`

---

## Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `jjwg_MarkersController` | Classe | Controleur du module |
| `action_marker_edit_map()` | Methode | Charge le bean, calcule `define_loc()`, route vers `marker_edit_map` |
| `action_marker_detail_map()` | Methode | Idem mais route vers `marker_detail_map` (lecture seule) |

---

## Interactions
- **Appelle :** `get_module_info('jjwg_Markers')`, `jjwg_Markers::retrieve()`, `jjwg_Markers::define_loc()`
- **Passe a la vue via :** `$GLOBALS['loc']`

---

## Notes
- Analogue a `jjwg_AreasController` mais sans calcul de polygone.
