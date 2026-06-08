# MainTree.php

**Chemin :** `modules/ModuleBuilder/Module/MainTree.php`
**Type :** PHP (helper / UI)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Arbre principal vide pour ModuleBuilder. Hérite de `MBPackageTree` mais initialise un arbre sans noeuds (tableau vide). Utilise `StudioBrowser` comme contexte mais ne peuple pas l'arbre.

## Type
helper

## Dépendances clés
- `MBPackageTree` (`MB/MBPackageTree.php`) — classe parente
- `StudioBrowser` (`Module/StudioBrowser.php`) — chargé mais non utilisé pour les noeuds

## Exports/Symboles principaux
- `MainTree` — classe (hérite de `MBPackageTree`)

## Interactions
- **Appelé par :** INCONNU (classe peu documentée dans le code source — probablement reliquat ou utilisation interne)
- **Appelle :** `StudioBrowser` (instancié mais `getNodes()` non appelé), `MBPackageTree::populateTree(array(), ...)`

## Notes
Classe vestige — l'arbre est peuplé avec un tableau vide. Usage actuel INCONNU.
