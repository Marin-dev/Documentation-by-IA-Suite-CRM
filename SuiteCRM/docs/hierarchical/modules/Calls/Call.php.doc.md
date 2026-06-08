# Fichier : Call.php

**Chemin :** `modules/Calls/Call.php`
**Type :** model
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Classe metier centrale du module Calls (Appels). Represente un appel telephonique planifie, tenu ou non tenu. Gere la planification, les invites (users, contacts, leads), les rappels, la synchronisation vCal/iCal et les notifications par email.

## Role technique
Etend `SugarBean`. Surcharge `save()` pour calculer `date_end`, mettre a jour le cache vCal et sauvegarder les rappels (`Reminder::saveRemindersDataJson`). Surcharge `mark_deleted()` pour corriger les recurrences via `CalendarUtils`. Implemente ACL avec blocage edition des appels recurents non-Sugar. Tres similaire a `Meeting` mais sans integration API externe.

---

## Dependances cles
| Import | Role |
|---|---|
| `SugarBean` | classe parente ORM |
| `vCal` | mise a jour cache iCal |
| `Reminder` | gestion rappels |
| `CalendarUtils` | correction recurrences suppression |
| `SecurityGroup` | ACL groupes |
| `BeanFactory` | beans lies |

## Exports / Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `Call` | classe | bean principal module Calls |

## Tables SQL impliquees
- `calls` (table principale)
- `calls_users` (invites utilisateurs)
- `calls_contacts` (invites contacts)
- `calls_leads` (invites leads)

---

## Relations cles
- **Appele par :** `CallFormBase::handleSave()`, `Save.php`, `Reschedule.php`, logic hooks
- **Appelle :** `vCal::cache_sugar_vcal()`, `Reminder::saveRemindersDataJson()`, `CalendarUtils::correctRecurrences()`

---

## Points d'attention
- Structure et logique quasi-identiques a `Meeting` mais sans `ExternalAPIFactory` (pas d'API webconf pour les appels).
- `create_notification_email()` joint un fichier `.ics` a l'email de notification (lignes 564-593).
- La direction (Inbound/Outbound) est un champ specifique aux Calls absent de Meetings.
