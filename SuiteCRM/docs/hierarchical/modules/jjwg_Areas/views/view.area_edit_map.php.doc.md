# view.area_edit_map.php

**Chemin :** `modules/jjwg_Areas/views/view.area_edit_map.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Vue d'edition cartographique d'une zone. Permet a l'utilisateur de dessiner ou modifier un polygone sur Google Maps et de recuperer les coordonnees resultantes pour les inserer dans le champ `coordinates` du formulaire parent.

**Type :** view

---

## Dependances cles
- `SugarView` — classe parente
- Google Maps API JS avec librairie `drawing` (CDN)
- jQuery (via `include/javascript/jquery/jquery-min.js`)
- `$GLOBALS['polygon']` — polygone existant (optionnel, injecte par le controleur)
- `$GLOBALS['loc']` — point central initial
- `$GLOBALS['jjwg_config']` — cle API et coordonnees par defaut

---

## Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `Jjwg_AreasViewArea_Edit_Map` | Classe | Vue SugarView |
| `display()` | Methode | Genere la page HTML avec Google Maps DrawingManager |

---

## Interactions
- **Appelee par :** `jjwg_AreasController::action_area_edit_map()`
- **Ecrit dans :** `parent.document.getElementById('coordinates').value` — champ du formulaire parent (l'iframe communique avec la fenetre parente)
- **Utilise :** boutons "Reset" et "Use Area Coordinates" (jQuery)

---

## Notes
- Fonctionne dans une iframe integree a la vue edit du module.
- Le clic droit sur un sommet le supprime (listener `rightclick`, ligne 178).
- Les coordonnees sont exportees au format `lng,lat,0` separes par espaces (precision 8 decimales, zeros finaux supprimes).
- Si plusieurs polygones sont dessines, "Use Area Coordinates" les concatene tous.
