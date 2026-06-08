# view.tour.php

**Chemin :** `modules/Home/views/view.tour.php`
**Type :** PHP - Vue
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Vue d'accueil de bienvenue / tour de démarrage de SuiteCRM. Détecte si l'instance a été mise à jour (via `UpgradeHistory`) pour afficher ou non un message de configuration du calendrier. Rendu via le template `modules/Home/tour.tpl`.

## Type
view

## Dépendances clés
- `include/MVC/View/SugarView.php` — classe parente
- `UpgradeHistory` — détection d'une mise à jour
- `Sugar_Smarty` (via `$this->ss`) — moteur de templates
- `$sugar_flavor`, `$current_user` (globaux)

## Exports / Symboles principaux
- `HomeViewTour` (classe, étend `SugarView`)
  - `display()` — détecte la mise à jour, assigne les variables Smarty, affiche `tour.tpl`

## Interactions
- **Appelé par :** dispatcher SugarCRM via `action_view_map['tour']` (défini dans `action_view_map.php`)
- **Appelle :** `UpgradeHistory::getAll()`, template `modules/Home/tour.tpl`

## Notes
- Le lien vers la configuration du calendrier est affiché uniquement si l'instance a un historique de mise à jour (`count($uh->getAll()) > 0`).
