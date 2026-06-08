# Fichier : JSGroupings.php

**Chemin :** `jssource/JSGroupings.php`
**Type :** configuration (build JS)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Definit la carte de regroupement des fichiers JavaScript de SuiteCRM : quels fichiers sources doivent etre concatenes ensemble et dans quel fichier de sortie. Ce fichier pilote la construction des bundles JS mis en cache pour optimiser les performances.

## Role technique
Expose un tableau PHP `$js_groupings` compose de plusieurs sous-tableaux nommes (groupes). Chaque entree mappe `source.js => fichier_concatene.js`. Les groupes existants sont :
- `$sugar_grp1` — scripts charges en premiere page (alertes, AJAX UI, menus, calendrier...)
- `$sugar_grp_jquery` — jQuery, Bootstrap, jQuery UI et plugins
- `$sugar_field_grp` — champs SugarFields
- `$sugar_grp1_yui` — bibliotheque YUI (yahoo, dom, event, autocomplete...)
- `$sugar_grp_yui_widgets` — widgets YUI (datatable, treeview, button...)
- `$sugar_grp_yui_widgets_css` — CSS des widgets YUI
- `$sugar_grp_yui2` — complement YUI2 (dragdrop, container)
- `$sugar_grp_emails` — module Emails complet
- `$sugar_grp_quick_compose` — composition rapide d'emails
- `$sugar_grp_jsolait` — scheduler Meetings
- `$sugar_grp_project` — scheduler Projects
- `$sugar_grp_project_template` — scheduler AM_ProjectTemplates

Supporte les extensions via `custom/application/Ext/JSGroupings/jsgroups.ext.php` (ligne 219).

---

## Dependances cles
- **Imports principaux :**
  - `custom/application/Ext/JSGroupings/jsgroups.ext.php` — extensions personnalisees (optionnel)
- **Variables d'environnement :** aucune
- **Arguments :** aucun

## Exports / Symboles principaux
- `$js_groupings` — tableau — carte source->destination pour la concatenation JS
- `$sugar_grp1`, `$sugar_grp_jquery`, `$sugar_grp1_yui`, etc. — sous-tableaux individuels accessibles apres include

## Interactions
- **Appele par :**
  - `jssource/minify.php` (ligne 29, 32)
  - `jssource/minify_utils.php` (ligne 95)
  - `install/welcome.php` (ligne 70)
  - `install/old_php.php` (ligne 58)
- **Appelle :** rien

---

## Notes
- Les fichiers sources CSS sont egalement inclus dans `$sugar_grp_yui_widgets_css`.
- Pour eviter les doublons de cle dans le tableau, ajouter un `.` apres `.js` (commentaire ligne 48).
- Le repertoire `jssource/src_files/` contient les sources non-minifiees de certains fichiers.
