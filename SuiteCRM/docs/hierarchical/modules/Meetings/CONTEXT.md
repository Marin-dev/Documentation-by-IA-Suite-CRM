# 📁 Meetings

**Chemin :** `modules/Meetings/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module Meetings gère les réunions planifiées dans SuiteCRM. Supporte les réunions internes (type "Sugar") et les API externes (GoToMeeting, WebEx). Gère les invités (utilisateurs, contacts, leads), les statuts d'acceptation, les notifications par email avec pièce jointe ICS, et la synchronisation calendrier via vCal.

## ⚙️ Responsabilité technique
Bean `Meeting` (hérite de `SugarBean`). Calcule `date_end` depuis `date_start + duration`. Synchronise vCal, envoie des notifications ICS, gère les rappels JSON. Supporte les réunions récurrentes (éditables uniquement depuis Outlook si type non-Sugar). Tables : `meetings`, `meetings_users`, `meetings_contacts`, `meetings_leads`.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `views/` | Vues édition, liste, liste par type | [→ CONTEXT](views/CONTEXT.md) |
| `Dashlets/` | Dashlet "Mes réunions" | [→ CONTEXT](Dashlets/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues | [→ CONTEXT](metadata/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `Meeting.php` | Bean principal des réunions | [→ fiche](Meeting.php.doc.md) |
| `MeetingFormBase.php` | Logique de base du formulaire | [→ fiche](MeetingFormBase.php.doc.md) |
| `Save.php` | Action de sauvegarde | [→ fiche](Save.php.doc.md) |
| `MeetingCalendarSyncLogicHook.php` | Hook de synchronisation calendrier | [→ fiche](MeetingCalendarSyncLogicHook.php.doc.md) |
| `MeetingsJjwg_MapsLogicHook.php` | Hook de géolocalisation | [→ fiche](MeetingsJjwg_MapsLogicHook.php.doc.md) |
| `JoinExternalMeeting.php` | Rejoindre une réunion externe | [→ fiche](JoinExternalMeeting.php.doc.md) |
| `SubPanelViewInvitees.php` | Vue sous-panneau des invités | [→ fiche](SubPanelViewInvitees.php.doc.md) |
| `vardefs.php` | Schéma des tables de réunions | [→ fiche](vardefs.php.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.php.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `vCal`, `Reminder`, `ExternalAPIFactory`, `CalendarUtils`, `BeanFactory`, `SecurityGroup`, `ACLController`
- **Consommé par :** Module Calendar (affichage), Accounts/Contacts/Leads (relations), `MyMeetingsDashlet`
- **Flux typique :** Création réunion → invitation participants → `save()` calcule `date_end` → notifications ICS envoyées → synchronisation vCal

---

## ⚠️ Zones INCONNU
- Réunions récurrentes non-Sugar : lecture seule depuis le CRM
- Flag statique `$remindersInSaving` : problème potentiel en cas d'appel imbriqué
