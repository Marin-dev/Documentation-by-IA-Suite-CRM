# DropDownTree.php

**Chemin :** `modules/ModuleBuilder/Module/DropDownTree.php`
**Type :** PHP (helper / UI)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Arbre de navigation AJAX pour l'éditeur de dropdowns. Hérite de `MBPackageTree` et utilise `DropDownBrowser` comme source de données.

## Type
helper

## Dépendances clés
- `MBPackageTree` (`MB/MBPackageTree.php`) — classe parente
- `DropDownBrowser` (`Module/DropDownBrowser.php`) — source des noeuds

## Exports/Symboles principaux
- `DropDownTree` — classe (hérite de `MBPackageTree`)
  - `getName()` — retourne la traduction de `LBL_SECTION_PACKAGES`

## Interactions
- **Appelé par :** INCONNU (probablement `ModuleBuilderController::action_ViewTree()` pour le type 'dropdowns')
- **Appelle :** `DropDownBrowser::getNodes()`

## Notes
Classe très légère — toute la logique est dans `MBPackageTree` et `DropDownBrowser`.
