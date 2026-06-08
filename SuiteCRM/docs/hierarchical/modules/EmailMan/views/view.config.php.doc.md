# view.config.php

**Chemin :** `modules/EmailMan/views/view.config.php`
**Type :** vue

**Dernière mise à jour doc :** 2026-06-02

---

## Rôle

Vue de configuration du Mass Emailer (paramètres SMTP, limite d'emails par run, URL de tracking). Affiche et permet de modifier les réglages globaux de l'envoi de campagnes.

## Type

vue

---

## Dépendances clés

- `SugarView` (classe parente probable)
- `Forms.php` (`modules/EmailMan/Forms.php`) — JavaScript de validation
- `$mod_strings` — libellés

## Exports / Symboles principaux

- Classe de vue (nom probable : `EmailManViewConfig` ou `ViewConfig`)

## Interactions

- **Appelé par :** dispatcher MVC via `action_view_map.php` (action `config`)
- **Appelle :** `Forms.php::get_validate_record_js()`

## Notes

- Vue d'administration réservée aux admins.
