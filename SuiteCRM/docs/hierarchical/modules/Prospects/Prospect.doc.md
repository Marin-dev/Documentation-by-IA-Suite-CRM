# Prospect.php

**Chemin :** `modules/Prospects/Prospect.php`
**Type :** PHP - Model
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Bean représentant un prospect (cible de campagne marketing) dans SuiteCRM. Hérite de `Person` et implémente `EmailInterface`. Stocke les données de contact d'un individu non encore qualifié en lead ou contact.

## Type
model

## Dépendances clés
- `include/SugarObjects/templates/person/Person.php` — classe parente `Person`
- `include/EmailInterface.php` — interface `EmailInterface`

## Exports / Symboles principaux
- `Prospect` (classe) — étend `Person`, implémente `EmailInterface`
  - Champs : `$id`, `$name`, `$date_entered`, `$date_modified`, `$assigned_user_id`, `$created_by`, etc.

## Interactions
- **Appelé par :** module Campaigns, ProspectLists, vues Prospects
- **Appelle :** logique `Person`, `SugarBean`

## Notes
- Module aussi appelé "Targets" dans l'UI SuiteCRM.
