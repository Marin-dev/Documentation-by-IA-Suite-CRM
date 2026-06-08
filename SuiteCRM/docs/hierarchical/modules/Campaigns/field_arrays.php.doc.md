# Fichier : field_arrays.php

**Chemin :** `modules/Campaigns/field_arrays.php`
**Type :** PHP - Configuration (tableaux de champs)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Declare les tableaux de champs utilises par le framework SugarCRM pour le cache et le rendu des vues du module Campaign. Definit les colonnes de la table, les champs de la vue liste, et les champs obligatoires.

## Role technique

Script procedural. Peuple `$fields_array['Campaign']` avec trois sous-tableaux : `column_fields` (tous les champs persistables), `list_fields` (champs de la vue liste), `required_fields` (champs obligatoires).

---

## Dependances cles

- Aucune

## Exports / Symboles principaux

- `$fields_array['Campaign']` — tableau de configuration des champs Campaign
  - `column_fields` : id, name, status, budget, expected_cost, actual_cost, expected_revenue, campaign_type, etc.
  - `list_fields` : id, name, status, campaign_type, assigned_user_id, end_date, refer_url, currency_id
  - `required_fields` : (INCONNU : non lu en entier)

## Consommateurs identifies

- Framework SugarCRM (cache des champs, vues liste)

## Relations cles

- **Complement de :** `vardefs.php` (definition complete du schema)

---

## Points d'attention

- Fichier de configuration statique — a maintenir en coherence avec `vardefs.php` lors de l'ajout de champs.
