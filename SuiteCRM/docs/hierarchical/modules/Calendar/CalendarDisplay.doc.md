# 📄 CalendarDisplay.php

**Chemin :** `modules/Calendar/CalendarDisplay.php`
**Type :** PHP — Vue / Affichage
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Gère le rendu HTML du calendrier. Produit l'en-tête, le pied de page, le titre, la zone de vue partagée et la vue principale via des templates Smarty. Définit aussi les couleurs des activités par type de module.

## ⚙️ Rôle technique
Utilise `Sugar_Smarty` pour rendre les templates `.tpl` du dossier `modules/Calendar/tpls/`. Assigne les variables de configuration (format date, créneaux, couleurs, JSON des activités) aux templates. Contient `convertPHPToMomentFormat()` pour convertir les formats PHP en format Moment.js.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `Calendar` (objet passé au constructeur)
  - `Sugar_Smarty` — moteur de templates
  - `SugarConfig` — configuration globale
  - `SugarThemeRegistry` — images de navigation
  - `json_config` / `include/json_config.php` — configuration JSON
- **Paramètres d'entrée :** `Calendar $cal`, `$dashlet_id`, `$views`

## 📤 Sorties / Exports
- `CalendarDisplay` — classe — rendu HTML/Smarty du calendrier
- `display()` — rendu principal du calendrier
- `display_calendar_header()` / `display_calendar_footer()` — en-tête et pied de page
- `display_title()` — titre du module
- `display_shared_html()` — interface vue partagée
- **Consommateurs identifiés :**
  - `modules/Calendar/Dashlets/CalendarDashlet/CalendarDashlet.php`

## 🔗 Relations clés
- **Appelé par :** `index.php` du module Calendar, `CalendarDashlet`
- **Appelle :** `Sugar_Smarty`, `CalendarUtils::get_first_day_of_week()`, `get_custom_file_if_exists()`
- **Position dans le flux global :** Couche de présentation finale après chargement des activités

---

## 💡 Points d'attention
- La méthode `checkActivity()` fait une désérialisation `base64_decode + unserialize` des préférences utilisateur `CalendarActivities` — risque si données corrompues (mitigation : `['allowed_classes' => false]`).
- `convertPHPToMomentFormat()` ne couvre pas tous les codes PHP (plusieurs retournent `''`).
- Les couleurs peuvent être surchargées via `$sugar_config['CalendarColors']`.
