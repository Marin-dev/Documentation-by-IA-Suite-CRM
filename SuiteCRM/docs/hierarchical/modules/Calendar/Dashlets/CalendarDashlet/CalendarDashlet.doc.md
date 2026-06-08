# 📄 CalendarDashlet.php

**Chemin :** `modules/Calendar/Dashlets/CalendarDashlet/CalendarDashlet.php`
**Type :** PHP — Dashlet
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Intègre le calendrier comme widget dashlet sur la page d'accueil SuiteCRM. Affiche une vue jour ou semaine du calendrier de l'utilisateur directement dans le tableau de bord.

## ⚙️ Rôle technique
Étend `Dashlet`. Instancie `Calendar`, `CalendarDisplay` et rend l'en-tête + la vue principale. Limite l'affichage à un seul dashlet calendrier (retourne un message d'erreur si `$GLOBALS['cal_strings']` est déjà défini). Configurable via vue jour ou semaine.

---

## 📥 Entrées / Dépendances
- `Calendar`, `CalendarDisplay` — modules Calendar
- `Dashlet` (`include/Dashlets/Dashlet.php`) — classe parente
- `ACLController::checkAccess('Calendar', 'list')` — contrôle accès
- `$def['view']` — vue configurée (day/week)

## 📤 Sorties / Exports
- `CalendarDashlet` — étend Dashlet
- `display()` — HTML du dashlet calendrier
- `displayOptions()` — formulaire de configuration
- `saveOptions()` — sauvegarde titre et vue

## 🔗 Relations clés
- **Appelé par :** Framework Dashlet SuiteCRM (page d'accueil)
- **Appelle :** `Calendar`, `CalendarDisplay::display_calendar_header()`, `CalendarDisplay::display()`
- **Position dans le flux global :** Intégration calendrier dans le tableau de bord

---

## 💡 Points d'attention
- Un seul dashlet calendrier autorisé par tableau de bord (vérification via `$GLOBALS['cal_strings']`).
- `displayScript()` retourne une chaîne vide — le script est probablement chargé via `hasScript = true` par le framework.
