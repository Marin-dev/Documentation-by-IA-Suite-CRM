# CampaignLog.php

**Chemin :** `modules/CampaignLog/CampaignLog.php`
**Type :** PHP - Model
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Bean représentant une entrée du journal de campagne marketing (`campaign_log`). Trace chaque interaction d'une cible avec une campagne : clics sur trackers, ouvertures d'emails, rebonds, désabonnements, etc.

## Type
model

## Dépendances clés
- `SugarBean` (classe parente)

## Exports / Symboles principaux
- `CampaignLog` (classe) — étend `SugarBean`
  - Table : `campaign_log`
  - Champs : `$campaign_id`, `$target_tracker_key`, `$target_id`, `$target_type`, `$activity_type`, `$activity_date`, `$date_modified`

## Interactions
- **Appelé par :** module Campaigns, trackers email, sous-panneaux de Campaigns
- **Appelle :** logique `SugarBean`

## Notes
- `$target_type` peut être Contact, Lead, Prospect, User selon la cible.
