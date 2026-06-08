# field_arrays.php

**Chemin :** `modules/Bugs/field_arrays.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Definit les tableaux de champs utilises par le framework SuiteCRM pour le cache et les requetes de liste/export du module Bugs.

## Type
config

## Dependances cles
- Aucune dependance directe ; alimente la variable globale `$fields_array`

## Exports / Symboles principaux
- `$fields_array['Bug']` avec :
  - `column_fields` : liste des colonnes DB a charger
  - `list_fields` : champs affiches en vue liste
  - `required_fields` : `name` obligatoire

## Interactions
- **Appele par :** framework SuiteCRM (chargement du module, generation des requetes de liste)

## Notes
- Fichier purement declaratif, pas de logique.
