# view.quick_radius.php

**Chemin :** `modules/jjwg_Maps/views/view.quick_radius.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Vue de saisie pour la recherche par rayon autour d'une adresse libre. Permet de specifier une adresse, un module CRM cible, une distance et une unite (mi/km).

**Type :** view

---

## Dependances cles
- `SugarView` — classe parente
- `$GLOBALS['jjwg_config']['valid_geocode_modules']` — liste des modules disponibles
- `$GLOBALS['app_list_strings']['map_unit_type_list']` — unite mi/km

---

## Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `Jjwg_MapsViewQuick_Radius` | Classe | Vue formulaire |
| `display()` | Methode | Formulaire GET soumis vers `action=quick_radius_display` |

---

## Interactions
- **Appelee par :** `jjwg_MapsController::action_quick_radius()`
- **Soumet vers :** `action_quick_radius_display` -> iframe `action_map_markers`

---

## Notes
- Les valeurs par defaut de distance et unite sont issues de `$GLOBALS['jjwg_config']`.
