# 📄 SurveyQuestionOptions.php

**Chemin :** `modules/SurveyQuestionOptions/SurveyQuestionOptions.php`
**Type :** PHP — Modèle (SugarBean)
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Modèle représentant une option de réponse pour une question de sondage (item d'une liste Radio, Dropdown, Multiselect ou ligne d'une matrice). Chaque option a un nom et un `sort_order`.

## ⚙️ Rôle technique
Étend `Basic`. Bean CRUD minimal sans logique additionnelle. Liée à `SurveyQuestions` via `surveyquestions_surveyquestionoptions` et aux réponses via `surveyquestionoptions_surveyquestionresponses`.

---

## 📥 Entrées / Dépendances
- **Table DB :** `surveyquestionoptions`
- **Champs clés :** `name`, `sort_order`, `survey_question_id`

## 📤 Sorties / Exports
- `SurveyQuestionOptions extends Basic` — bean option de question
- **Consommateurs identifiés :**
  - `modules/Surveys/Surveys.php` — sauvegarde options
  - `modules/Surveys/Entry/Survey.php` — affichage public
  - `modules/SurveyResponses/Lines/Lines.php` — affichage réponses

## 🔗 Relations clés
- **Appelé par :** `Surveys::saveOptions()`, `Entry/Survey.php`, `Lines/Lines.php`
- **Position dans le flux global :** Feuille de la hiérarchie Survey → Question → Option

---

## 💡 Points d'attention
- `disable_row_level_security = true`, `importable = false` — standard pour les sous-modules sondage.
