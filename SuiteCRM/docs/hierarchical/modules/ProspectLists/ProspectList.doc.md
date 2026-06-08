# ProspectList.php

**Chemin :** `modules/ProspectLists/ProspectList.php`
**Type :** PHP - Model
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Bean représentant une liste de prospects/cibles utilisée dans les campagnes marketing. Gère les listes de type "test", "exemption", "default", etc. Permet de regrouper des contacts, leads, prospects et utilisateurs dans une liste ciblée.

## Type
model

## Dépendances clés
- `SugarBean` (classe parente)

## Exports / Symboles principaux
- `ProspectList` (classe) — étend `SugarBean`
  - `$field_name_map` — mapping des champs
  - Autres champs (INCONNU — lecture partielle)

## Interactions
- **Appelé par :** module Campaigns, vues ProspectLists
- **Appelle :** logique `SugarBean`

## Notes
- Aussi appelée "Target List" dans l'UI.
