# view.map_display.php

**Chemin :** `modules/jjwg_Maps/views/view.map_display.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Vue d'affichage principale de la carte. Encapsule la vue `map_markers` dans une iframe avec redimensionnement automatique via jQuery. Sert de conteneur dans le contexte du Detail View de SuiteCRM.

**Type :** view

---

## Dependances cles
- `SugarView` — classe parente
- `modules/jjwg_Maps/javascript/jquery.iframe-auto-height.plugin.1.9.3.min.js`
- `$_REQUEST` — parametres passes a l'URL de l'iframe

---

## Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `Jjwg_MapsViewMap_Display` | Classe | Vue conteneur iframe |
| `display()` | Methode | Construit l'URL de l'iframe (action=map_markers) avec les parametres filtrés, et injecte le plugin d'auto-redimensionnement |

---

## Interactions
- **Appelee par :** `jjwg_MapsController::action_map_display()`
- **Charge dans iframe :** `action=map_markers` (vue `Jjwg_MapsViewMap_Markers`)

---

## Notes
- Les parametres autorises dans l'URL iframe sont filtres (whitelist ligne 21) pour eviter les URL trop longues.
- Le parametre `current_post` (recherche avancee) est stocke en `$_SESSION` pour eviter les depassements de taille d'URL (ligne 621-623 du controleur).
