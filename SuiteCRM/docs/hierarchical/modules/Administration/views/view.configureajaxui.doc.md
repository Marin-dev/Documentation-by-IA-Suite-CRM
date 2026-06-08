# view.configureajaxui.php

**Chemin :** `modules/Administration/views/view.configureajaxui.php`
**Type :** PHP (view MVC SugarCRM)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Vue de configuration des modules bannis de l'interface Ajax (modules qui ne supportent pas le chargement Ajax et doivent forcer un rechargement complet de page).

## Role technique
Etend `SugarView`. `display()` : charge `$moduleList`, filtre ceux dans `ajaxBannedModules()` (liste native), et ceux dans `$sugar_config['addAjaxBannedModules']` (liste additionnelle). Encode les listes en JSON et affiche `templates/ConfigureAjaxUI.tpl`.

---

## Symboles principaux
- `ViewConfigureAjaxUI extends SugarView` — classe view

## Interactions
- **Appele par :** `index.php?module=Administration&action=ConfigureAjaxUI` (redirige depuis `AdministrationController::action_UpdateAjaxUI()`)
- **Template :** `modules/Administration/templates/ConfigureAjaxUI.tpl`
- **Sauvegarde via :** `AdministrationController::action_UpdateAjaxUI()`
