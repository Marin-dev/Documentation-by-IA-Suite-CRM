# Fichier : subpaneldefs.php (Campaigns)

**Chemin :** `modules/Campaigns/metadata/subpaneldefs.php`
**Type :** PHP - Configuration (metadata sous-panels)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Definit les sous-panels affiches dans la vue detail du module Campaigns (listes de prospection, logs, trackers, notes, leads, contacts, etc.).

## Role technique

Script procedural peuplant `$layout_defs['Campaigns']['subpanel_setup']` avec les configurations de chaque sous-panel.

---

## Dependances cles

- Aucune

## Exports / Symboles principaux

- `$layout_defs['Campaigns']['subpanel_setup']` — configuration des sous-panels

## Consommateurs identifies

- Framework SuiteCRM (rendu des sous-panels dans la vue detail)

---

## Points d'attention

- Les sous-panels sont charges en AJAX via `SubPanelViewer.php` (les sous-panels classiques sont desactives dans `view.detail.php`).
