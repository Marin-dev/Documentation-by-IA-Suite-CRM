# MBPackage.php

**Chemin :** `modules/ModuleBuilder/MB/MBPackage.php`
**Type :** PHP (model)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Représente un package ModuleBuilder (ensemble de modules non-deployés). Gère le cycle de vie complet : chargement, sauvegarde, build (ZIP), export, déploiement, suppression. Gère également l'export des personnalisations Studio (champs, layouts, relations).

## Type
model

## Dépendances clés
- `MBModule` (`MB/MBModule.php`) — module dans le package
- `DBManagerFactory` — requêtes DB pour `fields_meta_data` (export custom fields)
- `StudioModule` (`Module/StudioModule.php`) — pour lire les relations déployées
- `BeanFactory` — introspection des beans
- `php_zip_utils` — création ZIP

## Exports/Symboles principaux
- `MBPackage` — classe
  - `load()` — charge depuis `manifest.php`
  - `save()` — écrit `manifest.php` dans `custom/modulebuilder/packages/{name}/`
  - `build($export, $clean)` — construit le ZIP du package dans `custom/modulebuilder/builds/`
  - `exportCustom($modules, $export, $clean)` — exporte les personnalisations Studio en ZIP
  - `exportProject($package, $export, $clean)` — exporte le projet MB complet
  - `getManifest()` — génère le contenu PHP du manifest
  - `buildInstall($path)` — génère `$installdefs` pour le manifest
  - `getModule($name)` — retourne (ou crée) un `MBModule`
  - `delete()` — supprime récursivement le répertoire du package
  - `rename($new_name)` / `copy($new_name)` — renommage/copie du package
  - `getRelationshipsForModule($moduleName)` — retourne les relations d'un module du package
  - `filterExportedRelationshipFile($fn, $module, $includeRelationships)` — filtre les fichiers de relations pour l'export

## Interactions
- **Appelé par :** `ModuleBuilder`, `ModuleBuilderController`
- **Appelle :** `MBModule`, `StudioModule`, `DBManagerFactory`

## Notes
- `build()` change le répertoire courant (`chdir`) temporairement pour créer le ZIP — risque si une exception est levée entre `chdir` et la restauration. Ligne 329.
- `exportCustom()` copie `custom/modules/{module}` et supprime le dossier `Ext` pour ne pas inclure les extensions compilées. Ligne 666.
- `copyCustomDropdownValuesForModules()` itère sur les fichiers de `custom/include/language` pour extraire uniquement les dropdowns utilisés par les modules exportés.
- Les fichiers de langue sont convertis en format Extension lors de l'export (`convertLangFilesToExtensions`).
