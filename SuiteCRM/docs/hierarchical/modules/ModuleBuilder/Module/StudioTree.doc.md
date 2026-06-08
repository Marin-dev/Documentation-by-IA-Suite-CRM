# StudioTree.php

**Chemin :** `modules/ModuleBuilder/Module/StudioTree.php`
**Type :** PHP (helper / UI)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Arbre de navigation AJAX pour Studio. Hérite de `MBPackageTree` mais utilise `StudioBrowser` comme source de données à la place de `ModuleBuilder`.

## Type
helper

## Dépendances clés
- `MBPackageTree` (`MB/MBPackageTree.php`) — classe parente
- `StudioBrowser` (`Module/StudioBrowser.php`) — source des noeuds
- `include/ytree/Tree.php` — arbre YUI

## Exports/Symboles principaux
- `StudioTree` — classe (hérite de `MBPackageTree`)
  - `getName()` — retourne la traduction de `LBL_SECTION_MODULES`

## Interactions
- **Appelé par :** `ModuleBuilderController::action_ViewTree()` (quand `$_REQUEST['tree'] == 'Studio'`)
- **Appelle :** `StudioBrowser::getNodes()`, héritage `MBPackageTree::populateTree()`

## Notes
Classe très légère — toute la logique est dans `MBPackageTree` et `StudioBrowser`.
