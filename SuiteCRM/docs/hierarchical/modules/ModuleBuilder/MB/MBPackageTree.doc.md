# MBPackageTree.php

**Chemin :** `modules/ModuleBuilder/MB/MBPackageTree.php`
**Type :** PHP (helper / UI)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Construit l'arbre de navigation AJAX (YUI Tree) pour le panneau latéral du Module Builder. Peuple un arbre `Tree` avec les noeuds de packages et modules issus de `ModuleBuilder::getNodes()`.

## Type
helper

## Dépendances clés
- `include/ytree/Tree.php` — classe `Tree` (arbre YUI)
- `include/ytree/Node.php` — classe `Node`
- `ModuleBuilder` (`MB/ModuleBuilder.php`) — source des noeuds

## Exports/Symboles principaux
- `MBPackageTree` — classe
  - `getName()` — retourne `'Packages'`
  - `populateTree($nodes, $parent)` — remplit récursivement l'arbre
  - `fetch()` — génère le JS de l'arbre (tableau de noeuds)
  - `fetchNodes()` — retourne les noeuds bruts (format JSON)

## Interactions
- **Appelé par :** `ModuleBuilderController::action_ViewTree()` (quand `$_REQUEST['tree'] == 'ModuleBuilder'`)
- **Appelle :** `ModuleBuilder::getNodes()`, `Tree`, `Node`

## Notes
- Héritée par `StudioTree` et `DropDownTree` qui remplacent la source de données (`StudioBrowser` et `DropDownBrowser` respectivement).
- `populateTree()` est récursive — gère l'arborescence package > module > layouts > sous-vues.
