# view.modulelistmenu.php

**Chemin :** `modules/Home/views/view.modulelistmenu.php`
**Type :** PHP - Vue
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Vue du menu liste des modules pour le module Home. Enrichit la vue parente `ViewModulelistmenu` en ajoutant l'historique des enregistrements récemment consultés par l'utilisateur, avec leurs icônes de module et un résumé tronqué.

## Type
view

## Dépendances clés
- `ViewModulelistmenu` — classe parente
- `BeanFactory::newBean('Trackers')` — accès à l'historique de navigation
- `SugarThemeRegistry::current()->getImage()` — icônes de module
- `getTrackerSubstring()` — troncature du résumé

## Exports / Symboles principaux
- `HomeViewModulelistmenu` (classe, étend `ViewModulelistmenu`)
  - `display()` — assigne `LAST_VIEWED` à Smarty et affiche `modulelistmenu.tpl`

## Interactions
- **Appelé par :** framework SuiteCRM lors du rendu du menu de navigation supérieur
- **Appelle :** `Tracker::get_recently_viewed()`, `SugarThemeRegistry`, template `include/MVC/View/tpls/modulelistmenu.tpl`

## Notes
- `getTrackerSubstring()` tronque le nom de l'enregistrement pour l'affichage dans le menu.
