# Fichier : action_file_map.php

**Chemin :** `modules/Campaigns/action_file_map.php`
**Type :** PHP - Configuration (mapping actions)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Declare le mapping entre les noms d'actions non-standard et leurs fichiers PHP correspondants pour le module Campaigns. Permet au framework MVC SugarCRM de charger le bon fichier pour des actions sortant du pattern classique.

## Role technique

Script procedural. Ajoute une entree dans le tableau global `$action_file_map`. Une seule entree : `subpanelviewer` -> `modules/Campaigns/SubPanelViewer.php`.

---

## Dependances cles

- Aucune

## Exports / Symboles principaux

- `$action_file_map['subpanelviewer']` — entree de mapping (l.49)

## Consommateurs identifies

- Framework MVC SugarCRM (charge automatiquement lors du dispatch d'action)

## Relations cles

- **Cible du mapping :** `modules/Campaigns/SubPanelViewer.php`

---

## Points d'attention

- Contenu minimal : une seule entree de mapping. Extension simple et sur-mesure.
