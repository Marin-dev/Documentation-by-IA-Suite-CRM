# LabelList.php

**Chemin :** `modules/LabelEditor/LabelList.php`
**Type :** PHP - Vue / Script
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Affiche la liste des libellés de langue d'un module sous forme de tableau HTML. Chaque libellé est un lien cliquable vers la vue d'édition du libellé. Supporte un paramètre `refreshparent` pour recharger la fenêtre parente (popup).

## Type
view

## Dépendances clés
- `return_module_language()` — chargement des chaînes de langue
- `SugarThemeRegistry` — CSS du thème
- `$current_language` (global)

## Exports / Symboles principaux
Aucun (script procédural).

## Interactions
- **Appelé par :** action `LabelList` du LabelEditor
- **Appelle :** vue EditView du LabelEditor (via lien)
