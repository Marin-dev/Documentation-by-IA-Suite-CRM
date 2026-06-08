# view.themesettings.php

**Chemin :** `modules/Administration/views/view.themesettings.php`
**Type :** PHP (view MVC SugarCRM)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Vue de configuration des themes SuiteCRM. Permet de choisir le theme par defaut et d'activer/desactiver les themes disponibles.

## Role technique
Etend `SugarView`. `process()` : en POST, sauvegarde le theme par defaut et les themes desactives via `Configurator::handleOverride()`. `display()` : construit les listes enabled/disabled depuis `SugarThemeRegistry`, encode en JSON et affiche `templates/themeSettings.tpl`.

---

## Dependances cles
| Element | Role |
|---|---|
| `modules/Configurator/Configurator.php` | Persistance themes dans config_override |
| `SugarThemeRegistry` | Registre des themes disponibles |

## Symboles principaux
- `AdministrationViewThemesettings extends SugarView` — classe view

## Interactions
- **Appele par :** `index.php?module=Administration&action=ThemeSettings`
- **Template :** `modules/Administration/templates/themeSettings.tpl`

---

## Notes
- Validation : le theme par defaut est verifie dans `SugarThemeRegistry::allThemes()` (ligne 76) — `sugar_die()` si invalide.
