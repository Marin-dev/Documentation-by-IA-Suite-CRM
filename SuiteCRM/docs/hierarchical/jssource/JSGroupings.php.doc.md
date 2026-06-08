# JSGroupings.php

**Chemin :** `jssource/JSGroupings.php`
**Type :** `PHP (configuration build JS)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Déclare le tableau `$js_groupings` qui définit comment les fichiers JavaScript individuels doivent être concaténés en bundles. Chaque entrée mappe un fichier source vers un fichier bundle cible. Ce fichier est la source de vérité pour l'organisation des assets JS de SuiteCRM.

**Type :** build / config

---

## Dépendances clés
- `custom/application/Ext/JSGroupings/jsgroups.ext.php` — surcharge personnalisée optionnelle (ligne 218-220)

## Exports / Symboles principaux
- `$js_groupings` — tableau PHP des groupes de concaténation
- `$sugar_grp1` — bundle principal (alerts, sugar_3, ajaxUI, cookie, menu, calendar, quickCompose, yuiloader, phpjs, Panels)
- `$sugar_grp_jquery` — bundle jQuery (jquery, jquery-migrate, bootstrap, html5shiv, respond, footable, jquery-ui, plugins divers, message-box, EmailsComposeViewModal)
- `$sugar_field_grp` — bundle champs Sugar (SugarFieldCollection, Datetimecombo)
- `$sugar_grp1_yui` — bundle YUI (yahoo, dom, event, logger, animation, connection, dragdrop, container, element, tabview, selector, quicksearch, etc.)
- `$sugar_grp_yui_widgets` — bundle widgets YUI (datatable, treeview, button, calendar, SugarYUIWidgets, overrides)
- `$sugar_grp_yui_widgets_css` — bundle CSS YUI
- `$sugar_grp_yui2` — bundle YUI2 (dragdrop, container)
- `$sugar_grp_emails` — bundle module Emails
- `$sugar_grp_quick_compose` — bundle Quick Compose
- `$sugar_grp_jsolait` — bundle Meetings scheduler
- `$sugar_grp_project` — bundle Project scheduler
- `$sugar_grp_project_template` — bundle AM_ProjectTemplates scheduler

## Interactions
- **Appelé par :**
  - `jssource/minify.php` (ligne 32, 35)
  - `jssource/minify_utils.php` (ligne 95, 98)
  - `install/old_php.php` (ligne 58)
- **Appelle :** rien (fichier de données pur)
- **Position dans le flux global :** lu par le pipeline de build JS pour produire les bundles dans `cache/include/javascript/`

---

## Notes
- Les bundles de sortie sont placés dans `cache/include/javascript/` (via `sugar_cached()`).
- La convention de nommage `sugar_grp1_jquery.js`, `sugar_grp1_yui.js` etc. est référencée directement dans les vues HTML de l'installeur.
- Les fichiers sources non minifiés sont dans `jssource/src_files/`.
- Extension custom possible via `custom/application/Ext/JSGroupings/jsgroups.ext.php`.
