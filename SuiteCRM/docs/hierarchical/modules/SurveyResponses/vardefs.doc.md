# Fichier : vardefs.php

**Chemin :** `modules/SurveyResponses/vardefs.php`
**Type :** PHP — configuration (vardefs SugarCRM)
**Derniere mise a jour doc :** 2026-06-02

---

## Ce que ce fichier configure
Definit le schema de la table `surveyresponses` pour SugarCRM. Champs specifiques : `survey_id` (FK vers le sondage), `contact_id`, `campaign_id`, `happiness` (score satisfaction), `happiness_text` (texte libre), `email_response_sent` (bool).

## Parametres cles
| Champ | Type | Effet |
|---|---|---|
| `happiness` | int | Score de satisfaction (-1 = neutre, 0 = negatif, N = positif) |
| `happiness_text` | text | Detail textuel des reponses negatives |
| `email_response_sent` | bool | Flag anti-double-envoi d'email |
| `survey_id` | relate | FK vers le sondage |
| `contact_id` | relate | Contact ayant repondu |

## Impacte par / impacte
- Consomme par `SurveyResponses.php`
- Relation `surveys_surveyresponses` vers Surveys
- Relation `surveyresponses_surveyquestionresponses` vers SurveyQuestionResponses

## Points d'attention
- `happiness == -1` = valeur par defaut (aucune reponse matrice enregistree).
