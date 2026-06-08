# 📄 Surveys.php

**Chemin :** `modules/Surveys/Surveys.php`
**Type :** PHP — Modèle (SugarBean)
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Modèle principal du module Surveys (Sondages). Représente un sondage avec son statut (Pending/Public/Closed), son texte de soumission personnalisé et ses options de matrice (satisfied/neither/dissatisfied). Orchestre la sauvegarde des questions et options associées.

## ⚙️ Rôle technique
Étend `Basic`. Surcharge `save()` pour créer/mettre à jour les `SurveyQuestions` et `SurveyQuestionOptions` associées à partir des données POST (`survey_questions_*`). `getMatrixOptions()` retourne les libellés de la matrice. Status `Public` nécessaire pour l'accès public au sondage (voir `Entry/Survey.php`).

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `Basic` — classe parente SugarBean
  - `BeanFactory` — instanciation SurveyQuestions/SurveyQuestionOptions
- **Table DB :** `surveys`
- **Paramètres POST :** `survey_questions_supplied`, `survey_questions_names[]`, `survey_questions_types[]`, `survey_questions_ids[]`, `survey_questions_options[]`, etc.

## 📤 Sorties / Exports
- `Surveys` — classe modèle
- `save(): string` — sauvegarde le sondage + questions + options
- `getMatrixOptions(): array` — options de la matrice (satisfied/neither/dissatisfied)
- `getSubmitText(): string` — texte du bouton submit (défaut "Submit")
- **Consommateurs identifiés :**
  - `modules/Surveys/Entry/Survey.php` — affichage public
  - `modules/Surveys/Entry/SurveySubmit.php` — soumission des réponses

## 🔗 Relations clés
- **Appelé par :** Interface d'administration Surveys, `Entry/Survey.php`
- **Appelle :** `BeanFactory::getBean('SurveyQuestions')`, `BeanFactory::newBean('SurveyQuestionOptions')`
- **Position dans le flux global :** Modèle racine de la hiérarchie Survey → Questions → Options

---

## 💡 Points d'attention
- La sauvegarde des questions n'est déclenchée que si `$_REQUEST['survey_questions_supplied']` est non vide — un save programmatique sans cette clé POST ne sauvegardera pas les questions.
- `disable_row_level_security = true` — pas de sécurité par lignes.
- `importable = false` — les sondages ne peuvent pas être importés.
