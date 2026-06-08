# CalendarSync.php

**Chemin :** `install/suite_install/CalendarSync.php`
**Type :** `PHP (installeur — initialisation synchronisation calendrier)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Enregistre les logic hooks de synchronisation de calendrier pour le module Meetings lors de l'installation. Permet la synchronisation automatique après sauvegarde et après suppression d'une réunion.

**Type :** installer

---

## Dépendances clés
- `check_logic_hook_file()` — enregistrement de hooks

## Exports / Symboles principaux
- `install_calendar_sync_hooks()` — appelle `installCalendarSyncHooks()`
- `installCalendarSyncHooks()` — enregistre 2 hooks sur le module `Meetings` :
  - `after_save` → `MeetingCalendarSyncLogicHook::afterSave()`
  - `after_delete` → `MeetingCalendarSyncLogicHook::afterDelete()`

## Interactions
- **Appelé par :** `install/suite_install/suite_install.php` (ligne 54)
- **Appelle :** `check_logic_hook_file()`
- **Position dans le flux global :** enregistrement des hooks de synchronisation calendrier

---

## Notes
- `MeetingCalendarSyncLogicHook` est dans `modules/Meetings/MeetingCalendarSyncLogicHook.php`.
- Ordre des hooks : 1 (priorité haute).
