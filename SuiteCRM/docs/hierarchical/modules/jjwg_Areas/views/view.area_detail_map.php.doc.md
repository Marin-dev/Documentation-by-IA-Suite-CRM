# view.area_detail_map.php

**Chemin :** `modules/jjwg_Areas/views/view.area_detail_map.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Vue de detail cartographique d'une zone. Affiche le polygone de la zone sur une carte Google Maps en mode lecture seule (affichage uniquement, sans controles d'edition).

**Type :** view

---

## Dependances cles
- `SugarView` — classe parente
- Google Maps API JS (chargee depuis CDN, cle dans `$GLOBALS['jjwg_config']['google_maps_api_key']`)
- `$GLOBALS['polygon']` — tableau de points du polygone (injecte par le controleur)
- `$GLOBALS['loc']` — localisation centrale (lat/lng, injectee par le controleur)
- `$GLOBALS['jjwg_config']` / `$GLOBALS['jjwg_config_defaults']` — configuration carte

---

## Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `Jjwg_AreasViewArea_Detail_Map` | Classe | Vue SugarView |
| `display()` | Methode | Genere la page HTML complete avec carte Google Maps et le polygone de la zone |

---

## Interactions
- **Appelee par :** `jjwg_AreasController::action_area_detail_map()`
- **Recoit :** donnees via `$GLOBALS['polygon']` et `$GLOBALS['loc']`
- **Sortie :** page HTML autonome (document complet, pas un fragment)

---

## Notes
- Affiche un polygone bleu (`#000099`) avec `fillOpacity: 0.15` et utilise `map.fitBounds(bounds)` pour centrer automatiquement.
- Aucune interaction utilisateur (pas de drawing controls).
- La cle Google Maps est injectee directement dans l'URL du script JS (ligne 55).
