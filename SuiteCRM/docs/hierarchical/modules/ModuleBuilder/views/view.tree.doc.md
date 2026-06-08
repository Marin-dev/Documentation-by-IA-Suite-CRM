# view.tree.php

**Chemin :** `modules/ModuleBuilder/views/view.tree.php`
**Type :** PHP (view)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Vue qui renvoie les noeuds de l'arbre de navigation pour le panneau latéral AJAX. Produit du JSON pur (pas de HTML) pour alimenter l'arbre YUI côté client.

## Type
view

## Dépendances clés
- `SugarView` (parente)
- `MBPackageTree` / `StudioTree` selon contexte

## Exports/Symboles principaux
- `ViewTree` (ou similaire) — classe

## Interactions
- **Rendue par :** `action_view_map.php` -> `'tree'` (INCONNU — probablement via action_ViewTree du contrôleur)
