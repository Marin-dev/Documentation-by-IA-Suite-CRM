# 📄 CalendarActivity.php

**Chemin :** `modules/Calendar/CalendarActivity.php`
**Type :** PHP — Helper / Requêtes DB
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Encapsule une activité individuelle du calendrier (Meeting, Call, Task, FP_event) avec ses dates de début/fin. Fournit aussi les méthodes statiques pour requêter les activités en base de données sur une plage de dates, en tenant compte des droits ACL.

## ⚙️ Rôle technique
Construit des clauses SQL WHERE (`within` ou `until`) pour filtrer les activités par plage temporelle. La méthode `get_activities()` itère sur `$activityList`, interroge chaque module via `build_related_list_by_user_id()` et retourne un tableau de `CalendarActivity`. Supporte aussi les créneaux free/busy via le format vCal.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `include/utils/activity_utils.php` — `build_related_list_by_user_id()`
  - `DBManagerFactory` — conversion dates SQL
  - `BeanFactory` — instanciation beans
  - `ACLController` — vérification accès liste
  - `vCal` — pour `get_freebusy_activities()`
- **Paramètres d'entrée :** `$activities` (liste modules), `$user_id`, `$show_tasks`, `$view_start_time`, `$view_end_time`, `$view`, `$show_calls`, `$show_completed`

## 📤 Sorties / Exports
- `CalendarActivity` — classe — activité calendrier avec `$sugar_bean`, `$start_time`, `$end_time`
- `get_activities()` — statique — tableau de `CalendarActivity[]`
- `get_freebusy_activities()` — statique — tableau de créneaux occupés
- `get_occurs_within_where_clause()` / `get_occurs_until_where_clause()` — clauses SQL
- **Consommateurs identifiés :**
  - `modules/Calendar/Calendar.php`
  - `modules/iCals/iCal.php`
  - `modules/vCals/vCal.php`

## 🔗 Relations clés
- **Appelé par :** `Calendar::add_activities()`, `iCal::createSugarIcal()`, `vCal::create_sugar_freebusy()`
- **Appelle :** `BeanFactory::newBean()`, `ACLController::checkAccess()`, `DBManagerFactory::getInstance()`
- **Position dans le flux global :** Couche d'accès aux données activités du calendrier

---

## 💡 Points d'attention
- La méthode `until` (Meetings/Calls) capture aussi les événements commencés avant la plage mais se terminant dedans — logique différente de `within` (Tasks/Events).
- Le filtrage `accept_status != 'decline'` sur les tables de relation évite d'afficher les activités déclinées.
- Un commentaire TODO indique que la vérification SecurityGroup est désactivée pour des raisons de performance (ligne 277).
