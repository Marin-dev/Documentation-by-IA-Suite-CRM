# 📄 SurveyQuestions.php

**Chemin :** `modules/SurveyQuestions/SurveyQuestions.php`
**Type :** PHP — Modèle (SugarBean)
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Modèle représentant une question d'un sondage. Chaque question a un type (Text, Textbox, Checkbox, Radio, Dropdown, Multiselect, Matrix, Date, DateTime, Rating, Scale), un ordre de tri (`sort_order`) et appartient à un sondage parent.

## ⚙️ Rôle technique
Étend `Basic`. Pas de logique métier additionnelle — simple bean CRUD. Les options de question sont des `SurveyQuestionOptions` liées via la relation `surveyquestions_surveyquestionoptions`.

---

## 📥 Entrées / Dépendances
- **Table DB :** `surveyquestions`
- **Champs clés :** `type` (enum), `sort_order` (int), `survey_id` (relation vers Surveys)

## 📤 Sorties / Exports
- `SurveyQuestions extends Basic` — bean question de sondage
- **Consommateurs identifiés :**
  - `modules/Surveys/Surveys.php` — sauvegarde
  - `modules/Surveys/Entry/Survey.php` — affichage public
  - `modules/Surveys/Entry/SurveySubmit.php` — traitement réponses
  - `modules/Surveys/Lines/Lines.php` — affichage admin

## 🔗 Relations clés
- **Appelé par :** `Surveys::save()`, `Entry/Survey.php`, `Entry/SurveySubmit.php`
- **Appelle :** `Basic::save()`
- **Position dans le flux global :** Nœud intermédiaire Survey → Question → Option

---

## 💡 Points d'attention
- `disable_row_level_security = true` — pas de sécurité par ligne.
- `importable = false`.
