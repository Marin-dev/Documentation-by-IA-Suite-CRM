# 📁 iCals

**Chemin :** `modules/iCals/`
**Profondeur :** 2
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module iCals génère des flux de calendrier au format iCalendar (RFC 5545) pour les utilisateurs de SuiteCRM. Il permet à des clients calendrier externes (Outlook, Google Calendar, Apple Calendar) de s'abonner aux événements CRM (réunions, appels, tâches) via un flux iCal. Il supporte également le protocole WebDAV pour la synchronisation.

## ⚙️ Responsabilité technique
La classe `iCal` étend `vCal` (modules/vCals) et surcharge la génération d'entrées calendrier pour produire des blocs `VCALENDAR`, `VEVENT`, `VTODO` et `VTIMEZONE` conformes à la norme iCalendar. Elle gère les fuseaux horaires et l'heure d'été (DST) via `DateTimeZone`. La classe `HTTP_WebDAV_Server_iCal` implémente le serveur WebDAV pour la synchronisation. Le point d'entrée HTTP est `Server.php`.

---

## 📂 Contenu

### Sous-dossiers
_Aucun sous-dossier._

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `iCal.php` | Classe principale de génération du flux iCalendar (étend vCal) | Pas de fiche |
| `Server.php` | Point d'entrée HTTP pour la diffusion du flux iCal | Pas de fiche |
| `HTTP_WebDAV_Server_iCal.php` | Serveur WebDAV pour synchronisation calendrier | Pas de fiche |

### Fichiers non documentés (volontairement)
_Tous les fichiers sont documentés ci-dessus._

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `modules/vCals/vCal.php` (classe parente), `modules/Calendar/Calendar.php` (récupération des activités via `CalendarActivity::get_activities()`), `modules/ProjectTask/ProjectTask.php`, `modules/Tasks/Task.php`, `include/TimeDate.php`.
- **Expose :** URL de flux iCal accessible par des clients externes via `Server.php`. Méthode publique `getVcalIcal($user_focus, $num_months)`.
- **Flux typique :** Client calendrier externe → `Server.php` → `iCal::getVcalIcal()` → requête `CalendarActivity::get_activities()` → génération des blocs VEVENT/VTODO → retour du flux `.ics`.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre la génération du flux iCalendar | [`iCal.php`](iCal.php) |
| Trouver le point d'entrée HTTP du flux | [`Server.php`](Server.php) |
| Comprendre la synchronisation WebDAV | [`HTTP_WebDAV_Server_iCal.php`](HTTP_WebDAV_Server_iCal.php) |

---

## ⚠️ Zones INCONNU
- Contenu exact de `Server.php` et son mécanisme d'authentification : non lu intégralement.
- Différence fonctionnelle précise entre iCals et vCals (modules/vCals) : INCONNU sans comparaison approfondie.
