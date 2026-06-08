# Tracker.php

**Chemin :** `modules/Trackers/Tracker.php`
**Type :** PHP - Model
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Bean SuiteCRM représentant un enregistrement de tracking dans la table `tracker`. Enregistre chaque visite/action d'un utilisateur sur un module : user_id, module_name, monitor_id, date_modified, etc.

## Type
model

## Dépendances clés
- `data/SugarBean.php` — classe parente `SugarBean`

## Exports / Symboles principaux
- `Tracker` (classe) — étend `SugarBean`
  - Table : `tracker`
  - Champs : `id`, `monitor_id`, `user_id`, `module_name`, et autres
  - `$disable_var_defs = true`, `$disable_custom_fields = true`

## Interactions
- **Appelé par :** `TrackerManager`, monitors de tracking
- **Appelle :** `SugarBean`

## Notes
- Défini avec garde `if (!class_exists('Tracker'))` pour éviter les re-déclarations.
- Champs personnalisés désactivés (`disable_custom_fields = true`).
