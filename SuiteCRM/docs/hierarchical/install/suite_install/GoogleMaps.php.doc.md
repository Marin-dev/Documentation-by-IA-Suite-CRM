# GoogleMaps.php

**Chemin :** `install/suite_install/GoogleMaps.php`
**Type :** `PHP (installeur — initialisation module Google Maps)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Initialise le module Google Maps (jjwg_Maps) lors de l'installation. Installe les champs personnalisés de géocodage et enregistre les logic hooks de mise à jour des coordonnées GPS pour les modules Prospects, Leads, Contacts, Accounts et Meetings.

**Type :** installer

---

## Dépendances clés
- `ModuleInstall/ModuleInstaller.php` — `ModuleInstaller::install_custom_fields()`
- `check_logic_hook_file()` — enregistrement de hooks
- `getCustomFields()` — INCONNU (fonction non lue en totalité)

## Exports / Symboles principaux
- `install_gmaps()` — installe les champs custom et appelle `installJJWHooks()`
- `installJJWHooks()` — enregistre des hooks `before_save` et `after_save` sur Prospects, Leads, Contacts, Accounts pour `updateGeocodeInfo` et `updateRelatedMeetingsGeocodeInfo`

## Interactions
- **Appelé par :** `install/suite_install/suite_install.php` (ligne 50-51)
- **Appelle :** `ModuleInstaller::install_custom_fields()`, `check_logic_hook_file()`
- **Position dans le flux global :** installation du module de cartographie

---

## Notes
- Ordre des hooks : 77 (priorité basse dans la chaîne de hooks).
- Les hooks de géocodage s'exécutent sur `before_save` (mise à jour coordonnées) et `after_save` (mise à jour réunions liées).
- Modules couverts (partiels lus) : Prospects, Leads — Contacts, Accounts et Meetings probables (fichier tronqué).
