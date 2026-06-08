# Fichier : vardefs.php

**Chemin :** `modules/SurveyQuestionOptions/vardefs.php`
**Type :** PHP — configuration (vardefs SugarCRM)
**Derniere mise a jour doc :** 2026-06-02

---

## Ce que ce fichier configure
Definit le schema de la table `surveyquestionoptions` pour SugarCRM. Champs specifiques : `name` (nom de l'option), `sort_order` (ordre d'affichage), `survey_question_id` (FK vers la question parente).

## Parametres cles
| Champ | Type | Effet |
|---|---|---|
| `sort_order` | int | Ordre d'affichage de l'option |
| `survey_question_id` | relate | Lien vers la question parente |

## Impacte par / impacte
- Consomme par `SurveyQuestionOptions.php`, BeanFactory
- Relation `surveyquestions_surveyquestionoptions` vers SurveyQuestions

## Points d'attention
- Fichier config standard.
