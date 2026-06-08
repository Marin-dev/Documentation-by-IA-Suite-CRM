# Reminder.php

**Chemin :** `modules/Reminders/Reminder.php`
**Type :** PHP - Model
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Bean représentant un rappel dans SuiteCRM (table `reminders`). Associé à un événement (Meeting ou Call), il planifie l'envoi d'un popup ou d'un email de rappel à une date/heure donnée. Peut être lié à plusieurs invités via `Reminders_Invitees`.

## Type
model

## Dépendances clés
- `Basic` (classe parente)

## Exports / Symboles principaux
- `Reminder` (classe) — étend `Basic`
  - Constante `UPGRADE_VERSION = '7.4.3'`
  - Champs : `$date_willexecute`, `$popup`, `$email`, `$email_sent`, `$timer_popup`, `$timer_email`, `$related_event_module`, `$related_event_module_id`
  - `$remindersData` (static array) — cache des rappels en cours de sauvegarde

## Interactions
- **Appelé par :** formulaires Meeting/Call (save), scheduler de rappels
- **Appelle :** logique `Basic`

## Notes
- `$disable_row_level_security = true`, `$tracker_visibility = false`.
- Pattern anti-récursion via `$remindersInSaving`.
