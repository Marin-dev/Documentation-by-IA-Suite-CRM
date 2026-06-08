# Fichier : detailviewdefs.php (Campaigns)

**Chemin :** `modules/Campaigns/metadata/detailviewdefs.php`
**Type :** PHP - Configuration (metadata vue detail)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Definit la disposition et les champs de la vue Detail du module Campaigns. Specifie les panels, colonnes et champs affiches lors de la consultation d'une campagne.

## Role technique

Script procedural peuplant `$viewdefs['Campaigns']['DetailView']`. Structure standard des metadata de vue SugarCRM.

---

## Dependances cles

- Aucune

## Exports / Symboles principaux

- `$viewdefs['Campaigns']['DetailView']` — configuration de la vue detail

## Consommateurs identifies

- Framework SuiteCRM (rendu de la vue detail Campaigns)
- `CampaignsViewDetail` (via le moteur de rendu)

---

## Points d'attention

- Personnalisations a placer dans `custom/modules/Campaigns/metadata/detailviewdefs.php`.
