# view.geocoded_counts.php

**Chemin :** `modules/jjwg_Maps/views/view.geocoded_counts.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Vue de tableau de bord du geocodage. Affiche par module le nombre d'enregistrements par statut de geocodage (N/A, OK, ZERO_RESULTS, INVALID_REQUEST, APPROXIMATE, EMPTY), avec liens vers le geocodage et le reset.

**Type :** view

---

## Dependances cles
- `SugarView` — classe parente
- `$this->bean->geocoded_counts`, `geocoded_headings`, `geocoded_module_totals` — donnees preparees par le controleur
- `$GLOBALS['jjwg_config']['valid_geocode_modules']`

---

## Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `Jjwg_MapsViewGeocoded_Counts` | Classe | Vue de statistiques |
| `display()` | Methode | Genere le tableau de comptage + liens cron + liens export |

---

## Interactions
- **Appelee par :** `jjwg_MapsController::action_geocoded_counts()`
- **Affiche :** URL cron (`?entryPoint=jjwg_Maps&cron=1`), liens export CSV par module

---

## Notes
- Lien "Reset" par module appelle `action_reset_geocoding` (admin seulement).
- Lien "Delete Address Cache" appelle `action_delete_all_address_cache` (admin seulement).
