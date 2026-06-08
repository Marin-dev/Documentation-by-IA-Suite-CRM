# 📄 view.savesettings.php

**Chemin :** `modules/Calendar/views/view.savesettings.php`
**Type :** PHP — Vue / Sauvegarde préférences
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Sauvegarde les préférences calendrier de l'utilisateur courant (heures de travail, activités affichées, créneaux, options de partage) puis redirige vers la vue calendrier.

## ⚙️ Rôle technique
Étend `SugarView`. Convertit les heures AM/PM en format 24h via `to_db_time()`, puis appelle `setPreference()` sur `$current_user` pour chaque préférence. Encode `$_POST['activity']` en base64+sérialisation.

---

## 📥 Entrées / Dépendances
- `SugarView` — classe parente
- `$_REQUEST` — `day_start_hours/minutes/meridiem`, `day_end_hours/minutes/meridiem`, `activity`, `display_timeslots`, `show_tasks/calls/completed`, `shared_calendar_separate`
- `$current_user` — objet utilisateur global

## 📤 Sorties / Exports
- `CalendarViewSaveSettings` — vue de sauvegarde préférences
- Redirige vers `index.php?module=Calendar&action=index`

## 🔗 Relations clés
- **Appelé par :** Formulaire de paramètres du calendrier (template `settings.tpl`)
- **Position dans le flux global :** Persistance des préférences utilisateur calendrier

---

## 💡 Points d'attention
- Les activités sont sérialisées en base64 — voir `CalendarDisplay::checkActivity()` pour la désérialisation correspondante.
