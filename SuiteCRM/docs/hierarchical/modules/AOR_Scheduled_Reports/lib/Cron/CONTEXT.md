# 📁 Cron

**Chemin :** `modules/AOR_Scheduled_Reports/lib/Cron/`
**Profondeur :** 6
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Librairie tierce d'analyse et de calcul des expressions cron. Permet de parser des expressions cron et de déterminer la prochaine date d'exécution d'un rapport planifié.

## ⚙️ Responsabilité technique
Librairie PHP dans le namespace `Cron`. Architecture avec classe principale `CronExpression`, interface `FieldInterface`, factory `FieldFactory` et classes de champs individuels (Minutes, Hours, DayOfMonth, DayOfWeek, Month, Year).

---

## 📂 Contenu

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `CronExpression.php` | Classe principale : parsing et calcul de prochaine exécution | [→ fiche](CronExpression.php.doc.md) |
| `FieldFactory.php` | Factory des champs de l'expression cron | [→ fiche](FieldFactory.php.doc.md) |
| `FieldInterface.php` | Interface des champs cron | [→ fiche](FieldInterface.php.doc.md) |
| `AbstractField.php` | Classe abstraite de base pour les champs | [→ fiche](AbstractField.php.doc.md) |
| `MinutesField.php` | Champ minutes de l'expression cron | [→ fiche](MinutesField.php.doc.md) |
| `HoursField.php` | Champ heures | [→ fiche](HoursField.php.doc.md) |
| `DayOfMonthField.php` | Champ jour du mois | [→ fiche](DayOfMonthField.php.doc.md) |
| `DayOfWeekField.php` | Champ jour de la semaine | [→ fiche](DayOfWeekField.php.doc.md) |
| `MonthField.php` | Champ mois | [→ fiche](MonthField.php.doc.md) |
| `YearField.php` | Champ année | [→ fiche](YearField.php.doc.md) |
| `includeCron.php` | Point d'entrée d'inclusion de la librairie | [→ fiche](includeCron.php.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consommé par :** `AOR_Scheduled_Reports::shouldRun()` via `Cron\CronExpression`
- **Expose :** `Cron\CronExpression::factory()`, `isDue()`, `getNextRunDate()`

---

## ⚠️ Zones INCONNU
- Librairie tierce — ne pas modifier
