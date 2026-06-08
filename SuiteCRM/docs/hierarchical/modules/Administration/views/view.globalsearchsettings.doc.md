# view.globalsearchsettings.php

**Chemin :** `modules/Administration/views/view.globalsearchsettings.php`
**Type :** PHP (view MVC SugarCRM)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Vue de configuration des modules inclus dans la recherche globale (barre de recherche principale). Permet d'activer/desactiver les modules pour la recherche unifiee.

## Role technique
Etend `SugarView`. `display()` instancie `UnifiedSearchAdvanced`, appelle `retrieveEnabledAndDisabledModules()`, encode les listes en JSON et affiche le template (avec support override dans `custom/`).

---

## Dependances cles
| Element | Role |
|---|---|
| `modules/Home/UnifiedSearchAdvanced.php` | Service recherche unifiee |

## Symboles principaux
- `AdministrationViewGlobalsearchsettings extends SugarView` — classe view (nom non standard)

## Interactions
- **Appele par :** `index.php?module=Administration&action=GlobalSearchSettings`
- **Template :** `modules/Administration/templates/GlobalSearchSettings.tpl` (ou `custom/` override)
- **Sauvegarde via :** `AdministrationController::action_saveglobalsearchsettings()`
