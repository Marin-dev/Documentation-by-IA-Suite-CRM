# TrackerManager.php

**Chemin :** `modules/Trackers/TrackerManager.php`
**Type :** PHP - Service (singleton)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Singleton gérant l'ensemble des monitors de tracking de l'activité utilisateur. Charge la configuration depuis `modules/Trackers/config.php`, instancie les monitors actifs, et fournit les méthodes pour enregistrer les visites de modules, mettre en pause/reprendre le tracking.

## Type
service / singleton

## Dépendances clés
- `modules/Trackers/monitor/Monitor.php` — classe `Monitor`
- `modules/Trackers/config.php` — configuration `$tracker_config`
- `BeanFactory` (Administration) — lecture des paramètres admin

## Exports / Symboles principaux
- `TrackerManager` (classe singleton)
  - `getInstance()` — (static) retourne l'instance unique
  - `pause()` — suspend le tracking (ex. pendant import)
  - `unPause()` — reprend le tracking
  - `$paused` (static) — état de pause

## Interactions
- **Appelé par :** `Importer` (pause), framework SuiteCRM (tracking navigation)
- **Appelle :** monitors actifs (`Monitor` et sous-classes)

## Notes
- Pattern Singleton : constructeur privé.
- Désactivation par monitor possible via paramètres admin (`tracker_*`).
