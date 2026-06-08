# Fichier : field_arrays.php (Contacts)

**Chemin :** `modules/Contacts/field_arrays.php`
**Type :** PHP - Configuration (tableaux de champs)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Declare les tableaux de champs utilises par le framework SugarCRM pour le module Contacts. Definit les colonnes de table, les champs de vue liste et les champs obligatoires.

## Role technique

Script procedural. Peuple `$fields_array['Contact']` avec `column_fields`, `list_fields`, et `required_fields`.

---

## Dependances cles

- Aucune

## Exports / Symboles principaux

- `$fields_array['Contact']` — tableaux de configuration des champs

## Consommateurs identifies

- Framework SuiteCRM (cache des champs, vues)

---

## Points d'attention

- A maintenir en coherence avec `vardefs.php`.
