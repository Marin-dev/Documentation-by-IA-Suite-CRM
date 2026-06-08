# Fichier : vardefs.php

**Chemin :** `modules/Calls/vardefs.php`
**Type :** config (definition du schema)
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure
Definition complete du schema du bean `Call` dans `$dictionary['Call']`. Declare tous les champs, relations et index de la table `calls`. Structure analogue a `modules/Meetings/vardefs.php`.

## Parametres cles
| Parametre | Valeur | Effet |
|---|---|---|
| `table` | `calls` | table SQL principale |
| `unified_search` | `true` | appels dans recherche globale |
| `full_text_search` | `true` | indexation texte integral |
| `status` | enum `call_status_dom` | Planned / Held / Not Held |
| `direction` | enum `call_direction_dom` | Inbound / Outbound (specifique Calls) |
| `duration_hours / duration_minutes` | int | duree de l'appel |
| `repeat_*` | champs recurrence | support appels recurrents |
| `reminder_time / email_reminder_time` | int (seconde) | rappels avant debut (-1 = aucun) |

## Relations declarees (principales)
- `calls_contacts`, `calls_users`, `calls_leads` (many-to-many via tables de liaison)
- `calls_assigned_user`, `calls_modified_user`, `calls_created_by` (one-to-many Users)

---

## Points d'attention
- Champ `direction` (Inbound/Outbound) distingue les Calls des Meetings.
- `VardefManager::createVardef('Calls', 'Call', ['default', 'assignable', 'security_groups'])`.
