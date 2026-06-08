# Fichier : vardefs.php

**Chemin :** `modules/SurveyQuestions/vardefs.php`
**Type :** PHP — configuration (vardefs SugarCRM)
**Derniere mise a jour doc :** 2026-06-02

---

## Ce que ce fichier configure
Definit le schema de la table `surveyquestions` pour le framework SugarCRM. Champs specifiques : `sort_order` (int), `type` (enum des types de questions), `survey_id` (FK vers surveys).

## Parametres cles
| Champ | Type | Effet |
|---|---|---|
| `sort_order` | int | Ordre d'affichage de la question |
| `type` | enum | Type de question (Text, Checkbox, Radio, etc.) |
| `survey_id` | relate | FK vers le sondage parent |

## Impacte par / impacte
- Consomme par `SurveyQuestions.php` via BeanFactory
- Lie a `modules/SurveyQuestions/SurveyQuestions.php`

## Points d'attention
- Table auditee (`audited: true`).
