# 📄 view.reports.php

**Chemin :** `modules/Surveys/views/view.reports.php`
**Type :** PHP — Vue / Rapports statistiques
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Vue de rapports statistiques d'un sondage. Affiche les taux de réponse, statistiques par question (comptages, données graphiques) et compare avec les envois de campagne.

## ⚙️ Rôle technique
Étend `SugarView`. `generateSkeletonData()` crée une structure de données vide par question selon son type. La méthode `display()` la remplit avec les réponses réelles. `getSurveyStats()` requête les tables campaigns/campaign_log pour comptabiliser les envois. Les données sont passées au template `reports.tpl` via Smarty.

---

## 📥 Entrées / Dépendances
- `SugarView`, `DetailView2` — classes parentes
- `DBManagerFactory` — requête statistiques campagne
- `$this->bean` — objet Surveys courant
- `$app_list_strings['surveys_matrix_options']` — libellés matrice
- Template : `modules/Surveys/tpls/reports.tpl`

## 📤 Sorties / Exports
- `SurveysViewReports extends SugarView` — vue rapports
- Données : `responsesCount`, `surveysSent`, `surveysSentDistinct`, `data` (par question)

## 🔗 Relations clés
- **Appelé par :** `SurveysController::action_Reports()` (action "Reports" du module)
- **Appelle :** `get_linked_beans('surveys_surveyresponses')`, `get_linked_beans('surveyresponses_surveyquestionresponses')`
- **Position dans le flux global :** Tableau de bord analytique d'un sondage

---

## 💡 Points d'attention
- `getSurveyStats()` joint via `campaigns.survey_id` — INCONNU si ce champ existe dans le schéma campaigns standard (à vérifier).
- Pas de pagination sur les réponses — peut être lent avec de nombreuses réponses.
- La relation utilisée est `surveys_surveyresponses` — ordre par `date_created` (pas `date_entered`).
