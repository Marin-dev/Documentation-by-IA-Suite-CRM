# 📄 view.json.php

**Chemin :** `modules/Calendar/views/view.json.php`
**Type :** PHP — Vue JSON
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Vue de réponse JSON pour toutes les actions AJAX du calendrier. Encode et retourne les données préparées par le contrôleur.

## ⚙️ Rôle technique
Étend `SugarView`. Récupère `$this->view_object_map['jsonData']`, nettoie le buffer de sortie (`ob_clean()`) et encode en JSON. Si `jsonData` est absent, arrêt fatal.

---

## 📥 Entrées / Dépendances
- `SugarView` — classe parente
- `view_object_map['jsonData']` — données à encoder (injecté par CalendarController)

## 📤 Sorties / Exports
- `CalendarViewJson` — vue JSON
- **Consommateurs identifiés :** `CalendarController` (toutes actions AJAX)

## 🔗 Relations clés
- **Appelé par :** Framework MVC via `CalendarController` (`$this->view = 'json'`)
- **Position dans le flux global :** Dernière étape de la chaîne AJAX Calendar

---

## 💡 Points d'attention
- RAS
