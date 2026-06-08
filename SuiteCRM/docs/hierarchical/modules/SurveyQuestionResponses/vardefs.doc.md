# Fichier : vardefs.php

**Chemin :** `modules/SurveyQuestionResponses/vardefs.php`
**Type :** PHP — configuration (vardefs SugarCRM)
**Derniere mise a jour doc :** 2026-06-02

---

## Ce que ce fichier configure
Definit le schema de la table `surveyquestionresponses` pour SugarCRM. Champs specifiques : `surveyresponse_id`, `surveyquestion_id`, `answer` (texte/numero), `answer_bool` (boolean), `answer_datetime` (date/heure).

## Parametres cles
| Champ | Type | Effet |
|---|---|---|
| `answer` | varchar | Reponse texte libre, numerique ou scale |
| `answer_bool` | bool | Reponse case a cocher |
| `answer_datetime` | datetime | Reponse date/heure |
| `surveyresponse_id` | relate | FK vers SurveyResponse parent |
| `surveyquestion_id` | relate | FK vers la question |

## Impacte par / impacte
- Consomme par `SurveyQuestionResponses.php`
- Relation `surveyquestionoptions_surveyquestionresponses` vers SurveyQuestionOptions

## Points d'attention
- Pas de champ `answer_option_id` direct — les options choisies sont stockees via la relation `surveyquestionoptions_surveyquestionresponses`.
