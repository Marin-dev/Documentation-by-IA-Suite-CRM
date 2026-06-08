# 📄 controller.php

**Chemin :** `modules/Calendar/controller.php`
**Type :** PHP — Contrôleur MVC
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Contrôleur principal du module Calendar. Traite les actions AJAX du calendrier : sauvegarde d'activité, édition rapide, reprogrammation (drag & drop), redimensionnement, suppression et chargement des activités. Toutes les réponses sont en JSON.

## ⚙️ Rôle technique
Étend `SugarController`. Chaque méthode `action_*` prépare une réponse JSON via `$this->view_object_map['jsonData']` rendue par `CalendarViewJson`. Utilise `BeanFactory::getBean()` pour charger les beans d'activité et vérifie les droits ACL avant chaque opération.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `SugarController` — classe parente MVC
  - `CalendarUtils` — traitement récurrences et données JSON
  - `BeanFactory` — chargement beans
  - `ACLController` — contrôle accès
  - `modules/Calendar/Calendar.php` — pour `action_getActivities`
- **Paramètres d'entrée :** `$_REQUEST['current_module']`, `$_REQUEST['record']`, `$_REQUEST['datetime']`, `$_REQUEST['repeat_*']`

## 📤 Sorties / Exports
- `CalendarController` — étend SugarController
- Actions : `saveactivity`, `quickedit`, `reschedule`, `remove`, `resize`, `getActivities`, `getUser`
- **Consommateurs identifiés :** Appels AJAX JavaScript FullCalendar frontend

## 🔗 Relations clés
- **Appelé par :** Framework MVC SuiteCRM (routing via `index.php`)
- **Appelle :** `CalendarUtils::build_repeat_sequence()`, `CalendarUtils::save_repeat_activities()`, `CalendarUtils::markRepeatDeleted()`, `CalendarUtils::get_sendback_array()`, `Calendar::add_activities()`
- **Position dans le flux global :** Point d'entrée HTTP pour toutes les interactions AJAX du calendrier

---

## 💡 Points d'attention
- `action_saveactivity()` charge dynamiquement `{ObjectName}FormBase.php` — si le fichier est absent, appel à `sugar_cleanup(true)` (arrêt brutal).
- `action_reschedule()` gère le style "basic" (sans créneaux horaires) différemment en conservant l'heure originale.
- La vérification de limite de répétition retourne `limit_error: true` sans créer les récurrences — le client JS doit gérer ce cas.
