# Fichier : editviewdefs.php (Campaigns)

**Chemin :** `modules/Campaigns/metadata/editviewdefs.php`
**Type :** PHP - Configuration (metadata vue edition)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Definit la disposition et les champs du formulaire d'edition du module Campaigns. En pratique, la creation passe par le wizard (`WizardHome`) — ce fichier est utilise pour les editions directes (rarement).

## Role technique

Script procedural peuplant `$viewdefs['Campaigns']['EditView']`.

---

## Dependances cles

- Aucune

## Exports / Symboles principaux

- `$viewdefs['Campaigns']['EditView']` — configuration du formulaire d'edition

## Consommateurs identifies

- Framework SuiteCRM (vue EditView si bypass du wizard)

---

## Points d'attention

- Le wizard (`WizardHome`) est le parcours principal de creation/edition — ce fichier est secondaire.
- Personnalisations a placer dans `custom/modules/Campaigns/metadata/editviewdefs.php`.
