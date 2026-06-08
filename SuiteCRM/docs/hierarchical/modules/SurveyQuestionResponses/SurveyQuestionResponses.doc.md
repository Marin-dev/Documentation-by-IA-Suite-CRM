# 📄 SurveyQuestionResponses.php

**Chemin :** `modules/SurveyQuestionResponses/SurveyQuestionResponses.php`
**Type :** PHP — Modèle (SugarBean)
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Modèle représentant la réponse d'un utilisateur à une question spécifique d'un sondage. Stocke la réponse selon le type : texte libre (`answer`), booléen (`answer_bool`), date/heure (`answer_datetime`), ou option liée (via relation `surveyquestionoptions_surveyquestionresponses`).

## ⚙️ Rôle technique
Étend `Basic`. Bean CRUD minimal. Les relations vers `SurveyQuestionOptions` permettent de lier les réponses de type Radio/Dropdown/Multiselect/Matrix aux options choisies.

---

## 📥 Entrées / Dépendances
- **Table DB :** `surveyquestionresponses`
- **Champs clés :** `surveyresponse_id`, `surveyquestion_id`, `answer`, `answer_bool`, `answer_datetime`

## 📤 Sorties / Exports
- `SurveyQuestionResponses extends Basic` — bean réponse à une question
- **Consommateurs identifiés :**
  - `modules/Surveys/Entry/SurveySubmit.php` — création réponses
  - `modules/SurveyResponses/Lines/Lines.php` — affichage réponses
  - `modules/Surveys/views/view.reports.php` — rapports statistiques

## 🔗 Relations clés
- **Appelé par :** `SurveySubmit::processSurvey()`, `SurveysViewReports`
- **Position dans le flux global :** Feuille de la hiérarchie SurveyResponse → QuestionResponse → Option

---

## 💡 Points d'attention
- `disable_row_level_security = true`, `importable = false`.
