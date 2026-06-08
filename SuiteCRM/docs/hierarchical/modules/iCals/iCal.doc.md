# 📄 iCal.php

**Chemin :** `modules/iCals/iCal.php`
**Type :** PHP — Modèle / Générateur iCal
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Génère un fichier iCalendar (.ics) complet pour un utilisateur SuiteCRM, incluant ses Réunions, Appels, Tâches (VTODO) et Tâches Projet. Le fichier peut être consommé par des clients calendrier externes (Outlook, Google Calendar, Apple Calendar).

## ⚙️ Rôle technique
Étend `vCal`. Surcharge et ajoute des méthodes spécifiques au format iCal v2 : gestion des fuseaux horaires (VTIMEZONE avec DST), support VTODO pour les tâches, propriétés ATTENDEE avec statuts de participation. `getVcalIcal()` est le point d'entrée principal qui assemble VCALENDAR complet.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `vCal` — classe parente (méthodes de formatage iCal)
  - `Calendar` — pour `CalendarActivity::get_activities()`
  - `CalendarActivity` — requêtes activités
  - `BeanFactory` — ProjectTask, Tasks
  - `SugarDateTime` — manipulation dates
  - `TimeDate` — gestion fuseaux horaires
- **Variables d'env :** `$sugar_config['vcal_time']` (fenêtre temporelle, défaut 2 mois), `$sugar_config['site_url']`

## 📤 Sorties / Exports
- `iCal extends vCal` — générateur iCal
- `getVcalIcal(User $user, int $num_months): string` — fichier .ics complet
- Constante `UTC_FORMAT = 'Ymd\THi00\Z'`
- **Consommateurs identifiés :**
  - `modules/iCals/Server.php` — serveur WebDAV iCal
  - `modules/iCals/HTTP_WebDAV_Server_iCal.php`

## 🔗 Relations clés
- **Appelé par :** Serveur WebDAV iCal
- **Appelle :** `CalendarActivity::get_activities()`, `BeanFactory::newBean('ProjectTask')`, `vCal::create_ical_string_from_array()`
- **Position dans le flux global :** Génération du flux .ics pour abonnement calendrier externe

---

## 💡 Points d'attention
- `createSugarIcal()` inclut les ProjectTasks séparément des Tasks normales — deux requêtes DB.
- Le support VTIMEZONE inclut le calcul DST (heure d'été) via `getDSTRange()`.
- `getVcalIcal()` encode en ISO-8859-1 (ligne 552) — peut causer des problèmes avec les caractères UTF-8.
- Le paramètre `show_tasks_as_events=1` bascule les tâches de VTODO vers VEVENT.
