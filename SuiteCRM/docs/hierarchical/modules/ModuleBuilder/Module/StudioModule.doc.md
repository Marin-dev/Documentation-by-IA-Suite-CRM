# StudioModule.php

**Chemin :** `modules/ModuleBuilder/Module/StudioModule.php`
**Type :** PHP (model)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Représente un module déployé dans Studio. Fournit l'accès à la structure de navigation UI (champs, labels, relations, layouts, subpanels), aux métadonnées de vues, et à la suppression de champs depuis tous les layouts.

## Type
model

## Dépendances clés
- `BeanFactory` (`data/BeanFactory.php`) — chargement du bean
- `DeployedRelationships` (`parsers/relationships/DeployedRelationships.php`)
- `constants.php` (`parsers/constants.php`) — constantes MB_*
- `IconRepository` (local) — noms d'icônes
- `SubPanel` / `SubPanelDefinitions` (`include/SubPanel/`) — liste des subpanels
- `SearchViewMetaDataParser` — vérification des vues de recherche

## Exports/Symboles principaux
- `StudioModule` — classe
  - `getModuleName()` — nom du module (avec gestion du cas Bugs)
  - `getType()` — détecte le type SugarObject (company, person, issue, file, basic, sale)
  - `getFields()` — retourne `field_defs` du bean
  - `getNodes()` — arbre de navigation complet pour le panneau Studio
  - `getModule()` — sections Labels, Fields, Relationships, Layouts, Subpanels
  - `getLayouts()` — vues edit/detail/list/quickcreate/dashlet/popup/search
  - `getSubpanels()` — subpanels utilisés par ce module
  - `getProvidedSubpanels()` — subpanels fournis par ce module à d'autres
  - `getRelationships()` — retourne `DeployedRelationships`
  - `removeFieldFromLayouts($fieldName)` — retire un champ de toutes les vues et subpanels
  - `getViewMetadataSources()` — liste des types de vues disponibles
  - `isValidDashletModule($moduleName)` — vérifie l'existence d'un dashlet

## Interactions
- **Appelé par :** `StudioModuleFactory`, `StudioBrowser`, `ModuleBuilderController`, `ParserFactory`
- **Appelle :** `BeanFactory`, `DeployedRelationships`, `SubPanel`, `ParserFactory`

## Notes
- `sources` (ligne 83) mappe les fichiers de métadonnées (editviewdefs.php, etc.) aux types de vue MB. Peut être surchargé par des modules custom qui créent leur propre `{Module}StudioModule.php`.
- `getType()` utilise une boucle sur la hiérarchie de classes pour remonter jusqu'au template SugarObject. Ligne 161.
- La liste `$hideQuickCreateForModules` dans `getLayouts()` exclut kbdocuments, projecttask, campaigns du formulaire QuickCreate. Ligne 293.
