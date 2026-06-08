# Fichier : MeetingCalendarSyncLogicHook.php

**Chemin :** `modules/Meetings/MeetingCalendarSyncLogicHook.php`
**Type :** helper (logic hook)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Logic hook declenche apres la sauvegarde et apres la suppression d'une reunion. Synchronise la reunion avec les comptes calendrier externes (Google Calendar ou autre) via le service `CalendarSync`.

## Role technique
Classe simple avec deux methodes (`afterSave`, `afterDelete`) qui appellent toutes deux `CalendarSync::getInstance()->syncMeeting($bean)`. Depend de `include/CalendarSync/CalendarSync.php`.

---

## Dependances cles
- `CalendarSync` (`include/CalendarSync/CalendarSync.php`) — singleton de synchronisation calendrier

## Exports / Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `MeetingCalendarSyncLogicHook` | classe | logic hook calendar sync |
| `afterSave()` | methode | synchro apres sauvegarde |
| `afterDelete()` | methode | synchro apres suppression |

---

## Relations cles
- **Appele par :** framework logic hooks SuiteCRM (after_save, after_delete sur Meetings)
- **Appelle :** `CalendarSync::getInstance()->syncMeeting()`
- **Position dans le flux :** post-sauvegarde/suppression, apres la persistance bean

---

## Points d'attention
- Enregistrement du hook INCONNU dans ce fichier — doit etre declare dans `logic_hooks.php` (non visible ici).
