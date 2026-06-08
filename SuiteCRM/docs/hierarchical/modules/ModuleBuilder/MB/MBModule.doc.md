# MBModule.php

**Chemin :** `modules/ModuleBuilder/MB/MBModule.php`
**Type :** PHP (model)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Représente un module non-déployé dans un package ModuleBuilder. Gère la configuration du module, ses champs (via `MBVardefs`), ses fichiers de langue (via `MBLanguage`), ses relations (via `UndeployedRelationships`), la copie de templates, et la génération des fichiers PHP du module lors du build.

## Type
model

## Dépendances clés
- `MBVardefs` (`MB/MBVardefs.php`) — gestion des vardefs du module
- `MBLanguage` (`MB/MBLanguage.php`) — gestion des fichiers de langue
- `UndeployedRelationships` (`parsers/relationships/UndeployedRelationships.php`) — gestion des relations
- `ParserFactory` (`parsers/ParserFactory.php`) — pour `removeFieldFromLayouts`
- `Sugar_Smarty` — génération de classes PHP et menus via templates Smarty
- Constantes `MB_TEMPLATES` (`include/SugarObjects/templates`) et `MB_IMPLEMENTS`

## Exports/Symboles principaux
- `MBModule` — classe
  - `load()` / `save()` — chargement/sauvegarde du module (config + vardefs + langue + relations)
  - `build($basepath)` — génère les fichiers PHP du module dans le dossier de build
  - `createClasses($path)` — génère la classe PHP du bean et `vardefs.php` via Smarty
  - `createMenu($path)` — génère `Menu.php` via Smarty
  - `addField($vardef)` / `deleteField($name)` / `getField($name)` — CRUD champs
  - `setLabel()` / `getLabel()` / `deleteLabel()` — gestion labels
  - `setDropDown()` / `deleteDropDown()` — gestion dropdowns
  - `removeFieldFromLayouts($fieldName)` — supprime un champ de tous les layouts
  - `getNodes()` — arbre de navigation UI (champs, labels, relations, layouts)
  - `rename($new_name)` / `copy($new_name)` — renommage/copie
  - `createIcon()` — copie les icônes depuis le template SugarObject
  - `getDBName($name)` — normalise le nom (remplace les caractères non-alphanum par `_`)

## Interactions
- **Appelé par :** `MBPackage`, `ModuleBuilderController`
- **Appelle :** `MBVardefs`, `MBLanguage`, `UndeployedRelationships`, `ParserFactory`, `Sugar_Smarty`

## Notes
- `createClasses()` utilise `modules/ModuleBuilder/tpls/MBModule/Class.tpl` et `vardef.tpl` — les templates Smarty utilisent `{{` / `}}` comme délimiteurs. Ligne 487.
- `renameMetaData()` applique des regex sur le contenu de chaque fichier du répertoire pour remplacer les variables `$module_name`, `$object_name` etc. Ligne 669.
- `removeFieldFromLayouts()` itère sur une liste hardcodée de vues (editview, detailview, listview, basic_search, advanced_search, dashlet, popuplist). Ligne 842.
- `iTemplate` = `['assignable', 'security_groups']` — toujours implémentés.
