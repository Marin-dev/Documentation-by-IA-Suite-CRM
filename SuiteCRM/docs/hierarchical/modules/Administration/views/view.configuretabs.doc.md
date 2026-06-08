# view.configuretabs.php

**Chemin :** `modules/Administration/views/view.configuretabs.php`
**Type :** PHP (view MVC SugarCRM)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Vue de configuration des onglets de la barre de navigation de SuiteCRM. Permet d'activer/desactiver les modules dans la barre d'onglets et dans les sous-panneaux.

## Role technique
Etend `SugarView`. `display()` charge les onglets via `TabController::get_tabs_system()` (retourne enabled/disabled), les sous-panneaux via `SubPanelDefinitions`, encode tout en JSON et affiche `templates/ConfigureTabs.tpl`.

---

## Dependances cles
| Element | Role |
|---|---|
| `modules/Administration/Forms.php` | Helper JS |
| `include/SubPanel/SubPanelDefinitions.php` | Definition sous-panneaux |
| `modules/MySettings/TabController.php` | Gestion onglets |

## Symboles principaux
- `ViewConfiguretabs extends SugarView` — classe view

## Interactions
- **Appele par :** `index.php?module=Administration&action=ConfigureTabs`
- **Template :** `modules/Administration/templates/ConfigureTabs.tpl`
- **Sauvegarde via :** `AdministrationController::action_savetabs()`
