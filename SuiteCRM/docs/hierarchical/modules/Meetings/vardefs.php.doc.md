# Fichier : vardefs.php

**Chemin :** `modules/Meetings/vardefs.php`
**Type :** config (definition du schema)
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure
Definition complete du schema du bean `Meeting` dans le dictionnaire global `$dictionary['Meeting']`. Declare tous les champs, relations et index de la table `meetings`. Sert de source de verite pour l'ORM, Studio, les exports et les formulaires.

## Parametres cles
| Parametre | Valeur | Effet |
|---|---|---|
| `table` | `meetings` | table SQL principale |
| `unified_search` | `true` | reunions incluses dans la recherche globale |
| `full_text_search` | `true` | indexation texte integral |
| `optimistic_locking` | `true` | protection contre les editions concurrentes |
| `status` | enum `meeting_status_dom`, default `Planned` | statuts : Planned, Held, Not Held |
| `type` | enum via `getMeetingsExternalApiDropDown`, default `Sugar` | type reunion (Sugar, WebEx, etc.) |
| `repeat_type/interval/dow/until/count` | champs recurrence | gestion reunions recurrentes |
| `gsync_id / gsync_lastsync` | varchar/int | synchronisation Google Calendar |
| `outlook_id` | varchar 255 | synchronisation Outlook |
| `reminder_time / email_reminder_time` | enum (int en DB) | delai rappel en secondes avant debut (-1 = aucun) |

## Dependances
- `VardefManager::createVardef('Meetings', 'Meeting', ['default', 'assignable', 'security_groups'])` — ajoute les champs standard (id, dates, description, etc.)
- `getMeetingsExternalApiDropDown()` (definie dans `Meeting.php`) utilisee comme `function` du champ `type`

## Relations declarees
| Relation | Type | Description |
|---|---|---|
| `meetings_assigned_user` | one-to-many | utilisateur assigne |
| `meetings_modified_user` | one-to-many | utilisateur modificateur |
| `meetings_created_by` | one-to-many | createur |
| `meetings_notes` | one-to-many | notes rattachees a la reunion |
| `meetings_contacts` (via link) | many-to-many | contacts invites |
| `meetings_users` (via link) | many-to-many | users invites |
| `meetings_leads` (via link) | many-to-many | leads invites |

---

## Points d'attention
- Le champ `direction` est `non-db` (source = non-db) et existe uniquement pour compatibilite formulaire rapide (bug 24170).
- Les champs de recurrence (`repeat_*`) et `gsync_*` sont `studio: false`, non reportables ni importables.
