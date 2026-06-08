# 📄 Calendar.php

**Chemin :** `modules/Calendar/Calendar.php`
**Type :** PHP — Modèle / Orchestrateur
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Classe centrale du module Calendrier. Elle orchestre l'affichage du calendrier utilisateur en chargeant les activités (Réunions, Appels, Tâches, Événements FP) selon la vue sélectionnée (jour, semaine, mois, vue partagée). Elle gère aussi les préférences utilisateur (heures de début/fin, créneaux à afficher).

## ⚙️ Rôle technique
Instanciée par le contrôleur et le dashlet, elle calcule la plage temporelle selon la vue, récupère les activités via `CalendarActivity::get_activities()`, et construit le tableau `$items` utilisé par `CalendarDisplay` pour le rendu Smarty. Supporte les vues : `agendaDay`, `basicDay`, `agendaWeek`, `basicWeek`, `month`, `sharedMonth`, `sharedWeek`.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `include/utils/activity_utils.php` — utilitaires d'activités
  - `modules/Calendar/CalendarUtils.php` — calculs de date
  - `modules/Calendar/CalendarActivity.php` — requêtes DB activités
- **Variables d'environnement utilisées :** aucune directe
- **Paramètres d'entrée :** `$_REQUEST['day|month|year|week|view|mobile']`, préférences utilisateur SugarConfig

## 📤 Sorties / Exports
- `Calendar` — classe — orchestrateur du calendrier
- `$this->items` — tableau d'activités à afficher (consommé par `CalendarDisplay`)
- **Consommateurs identifiés :**
  - `modules/Calendar/controller.php`
  - `modules/Calendar/Dashlets/CalendarDashlet/CalendarDashlet.php`
  - `modules/iCals/iCal.php` (via CalendarActivity)

## 🔗 Relations clés
- **Appelé par :** `CalendarController`, `CalendarDashlet`, `view.json.php`
- **Appelle :** `CalendarActivity::get_activities()`, `CalendarUtils::get_first_day_of_week()`, `CalendarUtils::get_time_data()`, `BeanFactory::getBean()`
- **Position dans le flux global :** Nœud central entre la requête HTTP et l'affichage du calendrier

---

## 💡 Points d'attention
- La validation d'année est limitée à 1970-2037 (ligne 147) — contrainte timestamp Unix 32 bits.
- Le module `FP_events` est dans `$activityList` avec `showCompleted = true` mais les Tâches utilisent `date_due` comme date de début ET de fin.
- `$this->acts_arr[$user->id]` est rempli séparément par utilisateur pour la vue partagée.
- `SugarConfig` contrôle de nombreux comportements par défaut : `calendar.show_tasks_by_default`, `calendar.enable_repeat`, etc.
