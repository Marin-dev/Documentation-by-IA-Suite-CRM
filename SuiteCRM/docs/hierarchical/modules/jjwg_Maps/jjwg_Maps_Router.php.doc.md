# jjwg_Maps_Router.php

**Chemin :** `modules/jjwg_Maps/jjwg_Maps_Router.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Point d'entree HTTP enregistre (`entryPoint=jjwg_Maps`). Sert deux objectifs : (1) execution du geocodage par cron (`?cron=1`), (2) redirection POST de la vue liste vers `action=map_display` (transmission des parametres de recherche via formulaire JS auto-soumis).

**Type :** helper (entry point / routeur)

---

## Dependances cles
- `include/utils.php`, `include/export_utils.php`
- `modules/jjwg_Maps/jjwg_Maps.php` (mode cron seulement)
- `modules/jjwg_Maps/controller.php` (mode cron seulement)
- `entry_point_registry.php` — enregistrement du point d'entree

---

## Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| Mode `?cron=1` | Bloc PHP | Instancie `jjwg_MapsController` et appelle `action_geocode_addresses()` |
| Mode normal | Bloc PHP | Genere un formulaire HTML avec auto-soumission JS pour transmettre `$_REQUEST` en POST vers `action=map_display` |

---

## Interactions
- **Enregistre dans :** `entry_point_registry.php` avec `auth => false` (accessible sans authentification ?)
- **Appelle :** `jjwg_MapsController::action_geocode_addresses()` (mode cron)
- **Redirige vers :** `index.php?module=jjwg_Maps&action=map_display` (mode normal)

---

## Notes
- `auth => false` dans le registre : le point d'entree est accessible sans authentification SuiteCRM. Attention si l'instance est exposee publiquement.
- URL cron : `index.php?module=jjwg_Maps&entryPoint=jjwg_Maps&cron=1&limit=2500`
- Le formulaire JS exclu les parametres `action`, `module`, `entryPoint`, `display_module`, `quick_address` pour eviter les conflits.
