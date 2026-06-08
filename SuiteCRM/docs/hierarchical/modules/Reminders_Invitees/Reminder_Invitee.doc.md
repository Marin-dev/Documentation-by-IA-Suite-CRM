# Reminder_Invitee.php

**Chemin :** `modules/Reminders_Invitees/Reminder_Invitee.php`
**Type :** PHP - Model
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Bean représentant une relation entre un rappel et un invité (table `reminders_invitees`). Stocke le module et l'ID de l'invité pour chaque rappel.

## Type
model

## Dépendances clés
- `Basic` (classe parente)

## Exports / Symboles principaux
- `Reminder_Invitee` (classe) — étend `Basic`
  - Champs : `$reminder_id`, `$related_invitee_module`, `$related_invitee_module_id`
  - `$disable_row_level_security = true`, `$importable = false`

## Interactions
- **Appelé par :** `Reminder` (gestion des invités)

## Notes
- Table de jointure entre `reminders` et les différents modules d'invités (Users, Contacts, Leads).
