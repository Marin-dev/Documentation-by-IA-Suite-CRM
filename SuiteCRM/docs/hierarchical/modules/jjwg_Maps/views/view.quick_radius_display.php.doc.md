# view.quick_radius_display.php

**Chemin :** `modules/jjwg_Maps/views/view.quick_radius_display.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Vue de resultat de la recherche par rayon. Affiche l'adresse recherchee comme titre puis charge la carte des marqueurs dans une iframe.

**Type :** view

---

## Dependances cles
- `SugarView` — classe parente
- `$_REQUEST` — parametres de la recherche (quick_address, distance, unit_type, display_module)

---

## Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `Jjwg_MapsViewQuick_Radius_Display` | Classe | Vue resultat |
| `display()` | Methode | Genere l'iframe vers `action=map_markers` avec les parametres filtres |

---

## Interactions
- **Appelee par :** `jjwg_MapsController::action_quick_radius_display()`
- **Charge dans iframe :** `action=map_markers`

---

## Notes
- Parametres exclus de l'URL iframe : action, module, entryPoint, record, relate_id.
