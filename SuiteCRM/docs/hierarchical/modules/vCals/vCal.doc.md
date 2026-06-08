# 📄 vCal.php

**Chemin :** `modules/vCals/vCal.php`
**Type :** PHP — Modèle / Base vCal + Utilitaires iCal
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Classe de base pour la génération et la manipulation des données vCalendar/iCalendar. Gère le cache des données Free/Busy en base de données (table `vcals`), la génération du VFREEBUSY pour les réunions/appels, et fournit des utilitaires statiques de formatage RFC 5545 (folding, escape/unescape des caractères spéciaux).

## ⚙️ Rôle technique
Étend `SugarBean` avec la table `vcals`. Méthodes statiques pour encoder/décoder le format iCal (folding 75 caractères, escape backslash/newline/semicolon/comma). `cache_sugar_vcal()` met à jour le cache VFREEBUSY en base après chaque modification d'activité. `get_ical_event()` génère un VEVENT pour les invitations par email.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `SugarBean` — classe parente
  - `CalendarActivity` (via `Calendar.php`) — requêtes activités pour FREEBUSY
  - `BeanFactory` — instanciation
- **Table DB :** `vcals` (colonnes : `id`, `user_id`, `content`, `type`, `source`, `date_modified`, `deleted`)
- **Variables d'env :** `$sugar_config['vcal_time']` — fenêtre temporelle (défaut 2 mois)

## 📤 Sorties / Exports
- `vCal extends SugarBean` — modèle vCal
- `get_vcal_freebusy(User): string` — chaîne VCALENDAR avec VFREEBUSY
- `cache_sugar_vcal(User): void` — met à jour le cache DB
- `get_ical_event(SugarBean, User, ?User): string` — VEVENT pour invitation email
- `fold_ical_lines(string, string): string` — folding RFC 5545
- `create_ical_string_from_array(array, bool): string` — tableau → chaîne iCal
- `create_ical_array_from_string(string): array` — chaîne iCal → tableau
- `escape_ical_chars(string): string` / `unescape_ical_chars(string): string`
- Constantes : `UTC_FORMAT`, `EOL`, `TAB`, `CHARSPERLINE`
- **Consommateurs identifiés :**
  - `modules/iCals/iCal.php`
  - `modules/Calendar/CalendarActivity.php` (get_freebusy_activities)
  - `modules/Calendar/CalendarUtils.php` (cache après récurrences)
  - `modules/vCals/HTTP_WebDAV_Server_vCal.php`

## 🔗 Relations clés
- **Appelé par :** `iCal`, `CalendarActivity`, `CalendarUtils`, serveurs WebDAV
- **Appelle :** `CalendarActivity::get_activities()`, `BeanFactory::newBean('vCals')`
- **Position dans le flux global :** Infrastructure de base pour tout le sous-système iCal/vCal

---

## 💡 Points d'attention
- La section FREEBUSY en cache (lignes 203-215) est commentée/TODO — le cache VFREEBUSY est généré à la volée à chaque appel.
- `get_ical_event()` est utilisé pour les invitations par email (notifications de réunions).
- `cache_sugar_vcal_freebusy()` peut être lent si l'utilisateur a beaucoup d'activités.
