# InvadersDashlet.php

**Chemin :** `modules/Home/Dashlets/InvadersDashlet/InvadersDashlet.php`
**Type :** PHP - Dashlet
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Dashlet ludique "Space Invaders" intégré dans le tableau de bord. Non configurable (`isConfigurable = false`). Affiche un jeu via template Smarty et script JS associé.

## Type
view / dashlet

## Dépendances clés
- `include/Dashlets/Dashlet.php`
- `Sugar_Smarty`

## Exports / Symboles principaux
- `InvadersDashlet` (classe) — étend `Dashlet`
  - `display()` — rendu HTML
  - `displayScript()` — rendu JS du jeu

## Interactions
- **Appelé par :** `modules/Home/index.php`

## Notes
- Dashlet purement cosmétique / fun feature, sans logique métier.
