# 📄 view.quickedit.php

**Chemin :** `modules/Calendar/views/view.quickedit.php`
**Type :** PHP — Vue / Edition rapide AJAX
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Génère le formulaire d'édition rapide d'une activité calendrier (Meeting, Call, Task) et le retourne en JSON avec le HTML du formulaire, les données de groupe de ressources (GR) et les informations de répétition.

## ⚙️ Rôle technique
Étend `SugarView`. Utilise `EditView` pour rendre le formulaire via `quickcreatedefs.php` (ou `editviewdefs.php` en fallback). Charge les reminders si l'activité existe déjà. Encode le résultat en JSON avec le HTML embarqué.

---

## 📥 Entrées / Dépendances
- `EditView` (`include/EditView/EditView2.php`) — formulaire d'édition
- `CalendarUtils::get_sendback_repeat_data()` — données de récurrence
- `Reminder::loadRemindersData()` — données rappels
- `json_config` — données GR (Group Relations)
- `view_object_map['currentBean']` et `['currentModule']` — injectés par CalendarController

## 📤 Sorties / Exports
- `CalendarViewQuickEdit` — vue édition rapide
- Sortie JSON : `{access, module_name, record, edit, html, gr, repeat}`

## 🔗 Relations clés
- **Appelé par :** `CalendarController::action_quickedit()`
- **Position dans le flux global :** Rendu du formulaire inline pour édition depuis le calendrier

---

## 💡 Points d'attention
- Fallback de métadonnées : `quickcreatedefs` > `editviewdefs` (custom puis standard).
- Référence au fix #9781 pour les reminders — les données de reminders sont chargées séparément.
