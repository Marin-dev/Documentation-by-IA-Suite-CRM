# 📄 SurveySubmit.php (Entry)

**Chemin :** `modules/Surveys/Entry/SurveySubmit.php`
**Type :** PHP — Point d'entrée (traitement soumission)
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Traite la soumission d'un sondage public. Crée un `SurveyResponse` et tous les `SurveyQuestionResponse` correspondant aux réponses soumises. Redirige vers la page de remerciements.

## ⚙️ Rôle technique
Script procédural. `processSurvey()` itère sur les questions liées, crée un `SurveyQuestionResponse` par question selon le type (Checkbox, Radio, Dropdown, Multiselect, Matrix, DateTime, Date, Text/Rating/Scale/Textbox). Pour Matrix, calcule le score `happiness` (0 si insatisfait). Enregistre l'activité campagne.

---

## 📥 Entrées / Dépendances
- `$_REQUEST['id']` — ID du sondage
- `$_REQUEST['question'][]` — réponses par question ID
- `$_REQUEST['contact']`, `$_REQUEST['tracker']`
- `BeanFactory` — création SurveyResponses, SurveyQuestionResponses
- `modules/Campaigns/utils.php` — `log_campaign_activity()`

## 📤 Sorties / Exports
- Crée : `SurveyResponses` + N × `SurveyQuestionResponses`
- Redirige vers `entryPoint=surveyThanks`

## 🔗 Relations clés
- **Appelé par :** Formulaire POST de `Entry/Survey.php` (entryPoint=surveySubmit)
- **Appelle :** `BeanFactory::newBean('SurveyResponses/SurveyQuestionResponses')`, `SurveyResponses::save()`
- **Position dans le flux global :** Persistance des réponses d'un sondage

---

## 💡 Points d'attention
- Aucune validation CSRF ni protection anti-double-soumission côté serveur.
- `happiness` : -1 = non évalué, 0 = insatisfait (Textbox rempli ou réponse Dissatisfied en Matrix) — calcul simplifié.
- TODO ligne 122 : conversion du format de date utilisateur non implémentée.
- Pas de `sugarEntry` — fichier inclus via entryPoint.
