# SugarFeed.php

**Chemin :** `modules/SugarFeed/SugarFeed.php`
**Type :** PHP - Model
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Bean représentant une entrée de fil d'actualité interne SuiteCRM (SugarFeed / Activity Stream). Stocke les posts d'activité : description, auteur, module lié. Non importable. Fournit des méthodes statiques pour activer/désactiver les feeds par module.

## Type
model

## Dépendances clés
- `Basic` (classe parente SugarCRM)

## Exports / Symboles principaux
- `SugarFeed` (classe) — étend `Basic`
  - Table : `sugarfeed`
  - Champs : `$id`, `$name`, `$description`, `$assigned_user_id`, `$created_by`, etc.
  - `activateModuleFeed($module, $updateDB)` — (static) active le feed pour un module

## Interactions
- **Appelé par :** `SugarFeedDashlet`, hooks de modules (save actions)

## Notes
- `$importable = false` — ne peut pas être importé via CSV.
