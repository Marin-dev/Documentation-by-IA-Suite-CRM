# view.themeconfigsettings.php

**Chemin :** `modules/Administration/views/view.themeconfigsettings.php`
**Type :** PHP (view MVC SugarCRM)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Vue de configuration detaillee d'un theme specifique (parametres internes du theme). Permet de modifier les options du theme selectionne et sauvegarde dans `config_override.php` sous `theme_settings[nom_theme]`.

## Role technique
Etend `SugarView`. `process()` : valide le theme, lit sa configuration via `SugarThemeRegistry::getThemeConfig()`, normalise true/false, et appelle `Configurator::handleOverride()` avant `sleep(3)` et redirection. `display()` : affiche `templates/themeConfigSettings.tpl`.

---

## Dependances cles
| Element | Role |
|---|---|
| `modules/Configurator/Configurator.php` | Persistance config theme |
| `SugarThemeRegistry` | Lecture config theme |

## Symboles principaux
- `AdministrationViewThemeConfigSettings extends SugarView` — classe view

## Interactions
- **Appele par :** `index.php?module=Administration&action=ThemeConfigSettings&theme={nom}`
- **Template :** `modules/Administration/templates/themeConfigSettings.tpl`

---

## Notes
- `sleep(3)` apres sauvegarde (ligne 97) — probablement pour laisser le temps a la config d'etre ecrite avant la redirection. Pratique discutable.
