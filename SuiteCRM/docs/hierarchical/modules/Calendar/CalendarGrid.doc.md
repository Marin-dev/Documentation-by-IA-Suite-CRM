# 📄 CalendarGrid.php

**Chemin :** `modules/Calendar/CalendarGrid.php`
**Type :** PHP — Vue / Grille HTML
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Génère la grille HTML du calendrier (colonnes de jours, créneaux horaires) pour chaque vue (jour, semaine, mois, année, mobile, partagée). Produit le HTML des cellules de temps utilisées par le JavaScript FullCalendar côté client.

## ⚙️ Rôle technique
Méthode `display()` dispatch vers `display_<vue>()` par nom dynamique. Chaque méthode construit des `<div>` avec attributs `id`, `time`, `datetime` qui permettent au JavaScript de positionner les événements. La vue mobile génère un affichage liste trié par heure.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `Calendar` (objet passé au constructeur) — fournit `$grid_start_ts`, `$cells_per_day`, `$scroll_slot`
  - `CalendarUtils::get_first_day_of_week()` — calcul premier jour semaine
  - `$GLOBALS['timedate']` — formatage timestamps
- **Paramètres d'entrée :** `Calendar $cal`

## 📤 Sorties / Exports
- `CalendarGrid` — classe — HTML de la grille temporelle
- `display()` — retourne HTML de la grille selon la vue
- **Consommateurs identifiés :** INCONNU (probablement appelé depuis `index.php` ou les vues du module)

## 🔗 Relations clés
- **Appelé par :** `modules/Calendar/index.php` (INCONNU direct — architecture legacy)
- **Appelle :** `CalendarUtils::get_first_day_of_week()`, `BeanFactory::newBean('Users')` (vue partagée)
- **Position dans le flux global :** Rendu de la structure HTML du calendrier, complété par le JS

---

## 💡 Points d'attention
- Dispatch dynamique `$this->$action()` ligne 110 — si vue inconnue, `display_null()` lèverait une erreur.
- La vue mobile utilise `date("Y-m-d", $ts)` sans gestion de fuseau horaire.
- Les IDs de cellules (`t_{timestamp}`, `b_{timestamp}`) sont utilisés par le JavaScript FullCalendar pour positionner les événements — couplage fort avec le frontend.
- `display_year()` génère un tableau HTML brut sans Smarty.
