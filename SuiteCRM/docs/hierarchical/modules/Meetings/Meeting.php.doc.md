# Fichier : Meeting.php

**Chemin :** `modules/Meetings/Meeting.php`
**Type :** PHP - Modele (Model)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Classe metier centrale du module Meetings. Represente une reunion planifiee ou tenue dans le CRM. Gere le cycle de vie complet : creation, modification, suppression logique, notifications aux invites, et synchronisation calendrier. Supporte les reunions internes (type "Sugar") et les reunions via API externes (GoToMeeting, WebEx, etc.).

## Role technique

Herite de `SugarBean`. Surcharge `save()` pour calculer `date_end` a partir de `date_start + duration`, synchroniser vCal, envoyer des notifications et sauvegarder les donnees de rappels JSON. Surcharge `mark_deleted()` pour corriger les recurrences et mettre a jour vCal. Fournit des methodes de gestion des invites (users, contacts, leads), du statut d'acceptation, et des emails de notification avec piece jointe ICS.

---

## Dependances principales

| Import / Classe | Role |
|---|---|
| `SugarBean` | Classe de base ORM SuiteCRM |
| `vCal` (`modules/vCals/vCal.php`) | Synchronisation calendrier iCal |
| `Reminder` | Sauvegarde des donnees de rappel |
| `ExternalAPIFactory` (`include/externalAPI/`) | Integration APIs externes (WebMeeting) |
| `CalendarUtils` (`modules/Calendar/CalendarUtils.php`) | Correction des recurrences a la suppression |
| `BeanFactory` | Instanciation des beans lies (Users, Contacts, Leads) |
| `SecurityGroup` (`modules/SecurityGroups/SecurityGroup.php`) | Controle d'acces par groupe |
| `ACLController` | Controle ACL par module/vue |
| `SugarConfig` | Lecture de la configuration (upload_dir, etc.) |

## Variables d'environnement / Config
- `$sugar_config['email_calendar_invite_type']` : type d'invite calendrier ('rsvp_ics' ou 'rsvp_links'), ligne 719
- `$sugar_config['disable_notify_current_user']` : supprime l'utilisateur courant des destinataires

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `Meeting` | Classe | Modele metier de la reunion |
| `Meeting::save()` | Methode | Sauvegarde avec calcul date_end, notifications, vCal, rappels |
| `Meeting::set_accept_status()` | Methode | Mise a jour du statut acceptation (User/Contact/Lead) |
| `Meeting::get_meeting_users()` | Methode | Liste des utilisateurs invites avec leur statut |
| `Meeting::get_notification_recipients()` | Methode | Liste complete des destinataires de notification |
| `Meeting::create_notification_email()` | Methode | Email de notification avec piece jointe .ics |
| `Meeting::removeUnInvitedFromReminders()` | Methode | Filtre les invites supprimes des rappels |
| `Meeting::ACLAccess()` | Methode | Bloque edition/suppression si recurrence non-Sugar |
| `getMeetingsExternalApiDropDown()` | Fonction globale | Construit la liste deroulante des APIs externes |
| `getMeetingTypeOptions()` | Fonction globale | Retourne les options de type de reunion |

**Tables DB :** `meetings`, `meetings_users`, `meetings_contacts`, `meetings_leads`

---

## Relations cles

- **Appele par :** `modules/Meetings/Save.php` (via `MeetingFormBase`), Calendar, vues edit/list, API SOAP
- **Appelle :** `vCal`, `Reminder`, `ExternalAPIFactory`, `CalendarUtils`, `BeanFactory`, `SecurityGroup`
- **Position dans le flux :** Coeur du module Meetings, instancie par `BeanFactory::newBean('Meetings')`

---

## Points d'attention

- Si `$this->type != 'Sugar'`, une API externe est chargee pour planifier la reunion (ligne 239). Si l'API echoue, le save continue avec un log WARN sans erreur utilisateur (ligne 263).
- La prevention des doublons de rappels utilise un flag statique `$remindersInSaving` (ligne 119) — potentiel probleme en cas d'appel imbrique.
- `save_relationship_changes()` exclut `contact_id`, `user_id`, `assigned_user_id` (ligne 966) — la logique est geree par `MeetingFormBase`.
- Les reunions recurrentes dont la source n'est pas "Sugar" sont en lecture seule depuis le CRM (edition uniquement depuis Outlook).
- La piece jointe ICS est creee dans `upload_dir/{meeting_id}` et supprimee apres envoi (ligne 750).
