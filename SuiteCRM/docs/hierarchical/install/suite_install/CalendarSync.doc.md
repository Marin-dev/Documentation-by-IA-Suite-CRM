# Fichier : CalendarSync.php

**Chemin :** `install/suite_install/CalendarSync.php`
**Type :** installer (configuration synchronisation calendrier)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Configure la synchronisation du calendrier en enregistrant les logic hooks sur les Meetings pour declencher la synchronisation apres sauvegarde et apres suppression.

## Role technique
Deux fonctions : `install_calendar_sync_hooks()` (facade) et `installCalendarSyncHooks()` (implementation). Enregistre deux hooks sur le module Meetings via `check_logic_hook_file()`.

---

## Dependances cles
- **Imports principaux :** aucun

## Exports / Symboles principaux
| Symbole | Role |
|---|---|
| `install_calendar_sync_hooks()` | Facade appelee par suite_install.php |
| `installCalendarSyncHooks()` | Enregistre les hooks de synchronisation calendrier |

**Hooks configures :**
- `Meetings after_save` order 1 → `MeetingCalendarSyncLogicHook::afterSave`
- `Meetings after_delete` order 1 → `MeetingCalendarSyncLogicHook::afterDelete`

## Interactions
- **Appele par :** `install/suite_install/suite_install.php` (ligne 54)
- **Appelle :**
  - `check_logic_hook_file()`
  - `modules/Meetings/MeetingCalendarSyncLogicHook.php`

---

## Notes
- La separation facade/implementation permet d'appeler `installCalendarSyncHooks()` independamment (ex: lors d'un upgrade).
- Le detail du mecanisme de synchronisation (Google Calendar, iCal, etc.) est dans `MeetingCalendarSyncLogicHook`.
