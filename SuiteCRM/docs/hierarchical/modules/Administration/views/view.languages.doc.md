# view.languages.php

**Chemin :** `modules/Administration/views/view.languages.php`
**Type :** PHP (view MVC SugarCRM)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Vue de gestion des langues disponibles dans SuiteCRM. Permet d'activer ou desactiver les packs de langue installes.

## Role technique
Etend `SugarView`. `display()` lit `$sugar_config['languages']` et `$sugar_config['disabled_languages']`, construit deux listes (enabled/disabled) en JSON, et affiche `templates/Languages.tpl`. La langue par defaut systeme est toujours dans "enabled" et marquee `disabled: true` (non deplacable).

---

## Symboles principaux
- `ViewLanguages extends SugarView` — classe view

## Interactions
- **Appele par :** `index.php?module=Administration&action=Languages`
- **Template :** `modules/Administration/templates/Languages.tpl`
- **Sauvegarde via :** `AdministrationController::action_savelanguages()`
