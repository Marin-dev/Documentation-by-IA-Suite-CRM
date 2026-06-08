# 📄 CalendarUtils.php

**Chemin :** `modules/Calendar/CalendarUtils.php`
**Type :** PHP — Helper / Utilitaires statiques
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Bibliothèque de fonctions utilitaires statiques pour le calendrier. Gère : calcul premier jour de semaine, extraction des champs temporels d'un bean, construction de séquences de récurrence, sauvegarde et suppression d'activités récurrentes.

## ⚙️ Rôle technique
Toutes les méthodes sont statiques. `build_repeat_sequence()` implémente l'algorithme de génération de dates selon les types Daily/Weekly/Monthly/Yearly. `save_repeat_activities()` utilise des insertions SQL en masse pour les relations invités (users, contacts, leads) pour des raisons de performance. `markRepeatDeleted()` supprime directement en SQL sans appeler `mark_deleted()`.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `DBManagerFactory` — requêtes SQL directes
  - `SugarDateTime` — manipulation des dates
  - `BeanFactory` — instanciation beans
  - `vCal::cache_sugar_vcal()` — mise à jour cache vCal après modification
- **Paramètres d'entrée :** `SugarDateTime $date`, `SugarBean $bean`, `array $params` (type/interval/count/until/dow)

## 📤 Sorties / Exports
- `CalendarUtils` — classe utilitaire statique
- `get_first_day_of_week(SugarDateTime)` — retourne SugarDateTime
- `get_fields()` — liste des champs à extraire par module
- `get_time_data(SugarBean)` — tableau timestamp/offset/ts_start/ts_end/days
- `get_sendback_array(SugarBean)` — données JSON à renvoyer au client
- `build_repeat_sequence(string, array)` — tableau de dates de récurrence
- `save_repeat_activities(SugarBean, array)` — sauvegarde récurrences
- `markRepeatDeleted(SugarBean)` — suppression récurrences
- `correctRecurrences(SugarBean, string)` — correction après suppression parent
- **Consommateurs identifiés :**
  - `modules/Calendar/Calendar.php`
  - `modules/Calendar/controller.php`
  - `modules/Calendar/views/view.quickedit.php`

## 🔗 Relations clés
- **Appelé par :** `Calendar`, `CalendarController`, `CalendarViewQuickEdit`
- **Appelle :** `DBManagerFactory`, `vCal::cache_sugar_vcal()`
- **Position dans le flux global :** Couche utilitaire transverse du module Calendar

---

## 💡 Points d'attention
- `save_repeat_activities()` utilise `$clone = $bean` (pas de `clone` PHP) — mutation de l'objet original possible.
- La limite de récurrences est configurable via `calendar.max_repeat_count` (défaut 1000) — une limite +100 est ajoutée en sécurité.
- `markRepeatDeleted()` contient des logs `fatal()` pour debug (ligne 152-153) — dette technique.
- `correctRecurrences()` a un bug SQL potentiel ligne 538 : `SET repeat_parent_id = '' AND recurring_source = ''` (devrait être une virgule, pas AND).
