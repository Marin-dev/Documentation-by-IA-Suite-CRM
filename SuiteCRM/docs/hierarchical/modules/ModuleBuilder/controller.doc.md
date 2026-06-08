# controller.php

**Chemin :** `modules/ModuleBuilder/controller.php`
**Type :** `PHP` — controller
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Contrôleur principal du module ModuleBuilder/Studio. Il orchestre toutes les actions admin disponibles : gestion des packages, modules, champs, relations, layouts, labels, dropdowns. Il est le point d'entrée de toutes les requêtes HTTP vers `module=ModuleBuilder`.

## Rôle technique
Étend `SugarController`. Vérifie les droits d'accès admin/developer dans `process()`, puis dispatche vers des méthodes `action_*` selon l'action demandée. Chaque `action_*` instancie les parsers ou modèles nécessaires et définit `$this->view` pour le rendu.

---

## Dépendances clés
- `modules/ModuleBuilder/MB/ModuleBuilder.php` — classe `ModuleBuilder`, gestionnaire de packages MB
- `modules/ModuleBuilder/parsers/ParserFactory.php` — fabrique de parsers de vues
- `modules/ModuleBuilder/Module/StudioModuleFactory.php` — fabrique de modules Studio
- `modules/ModuleBuilder/parsers/constants.php` — constantes MB_*
- `modules/DynamicFields/FieldCases.php` — `get_widget()` pour créer des objets champs
- `modules/DynamicFields/DynamicField.php` — gestion des champs personnalisés déployés
- `ModuleInstall/PackageManager/PackageManager.php` — déploiement de packages
- `modules/Administration/QuickRepairAndRebuild.php` — reconstruire les extensions après modifications

## Exports / Symboles principaux
- `ModuleBuilderController` — classe (extends SugarController) — contrôleur principal

## Actions principales

| Méthode | Rôle |
|---|---|
| `process()` | Vérifie accès admin/developer avant dispatch |
| `action_editLayout()` | Détermine le type de vue et redirige vers la bonne vue layout |
| `action_ViewTree()` | Renvoie le JSON du tree (panneaux ouest) via AjaxCompose |
| `action_SavePackage()` | Sauvegarde/renomme/duplique un package MB |
| `action_BuildPackage()` | Construit le ZIP d'un package |
| `action_DeployPackage()` | Déploie un package MB via PackageManager |
| `action_ExportPackage()` | Exporte un package MB en ZIP |
| `action_DeletePackage()` | Supprime un package |
| `action_SaveModule()` | Sauvegarde/renomme/duplique un module MB |
| `action_DeleteModule()` | Supprime un module MB |
| `action_saveLabels()` | Sauvegarde les labels via ParserLabel |
| `action_SaveLabel()` | Sauvegarde un label unique (inline) |
| `action_SaveField()` | Crée/modifie un champ dynamique (studio ou MB) |
| `action_saveSugarField()` | Sauvegarde un champ standard (StandardField) |
| `action_DeleteField()` | Supprime un champ et le retire des layouts |
| `action_SaveRelationship()` | Crée/modifie une relation (deployed ou undeployed) |
| `action_DeleteRelationship()` | Supprime une relation |
| `action_SaveDropDown()` | Sauvegarde une liste déroulante via ParserDropDown |
| `action_saveLayout()` | Sauvegarde le layout en fichier working |
| `action_saveAndPublishLayout()` | Sauvegarde et publie le layout (custom) |
| `action_listViewSave()` | Sauvegarde le layout de liste |
| `action_dashletSave()` | Sauvegarde le layout dashlet |
| `action_popupSave()` | Sauvegarde le layout popup |
| `action_searchViewSave()` | Sauvegarde la vue de recherche |
| `getModuleTitle()` | (statique) Retourne le titre de section selon `$_REQUEST['type']` |

## Interactions
- **Appelé par :** framework SugarCRM (dispatcher) via `index.php?module=ModuleBuilder&action=...`
- **Appelle :** `ModuleBuilder`, `MBPackage`, `MBModule`, `ParserFactory`, `ParserLabel`, `ParserDropDown`, `DeployedRelationships`, `UndeployedRelationships`, `DynamicField`, `StandardField`, `PackageManager`, `RepairAndClear`

## Notes
- `action_DeployPackage()` vide les caches JS, ACL, menu, unified search après déploiement (lignes 209-261).
- `action_SaveField()` gère deux chemins distincts : champ déployé (Studio) vs champ non-déployé (MB). Le mapping `Employees` → `Users` est appliqué systématiquement (ligne 389).
- `action_savetablesort()` persiste les préférences de tri du tableau de champs en session utilisateur.
