# 📄 Survey.php (Entry)

**Chemin :** `modules/Surveys/Entry/Survey.php`
**Type :** PHP — Point d'entrée public (vue HTML)
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Page d'affichage public d'un sondage. Accessible sans authentification SuiteCRM via un lien de campagne. Affiche le formulaire du sondage avec toutes ses questions selon leur type (texte, radio, checkbox, dropdown, multiselect, matrice, date, rating, scale).

## ⚙️ Rôle technique
Script procédural (pas de classe). Valide l'ID du sondage via `SuiteValidator`, vérifie que le statut est `Public`, enregistre l'activité de suivi de campagne via `log_campaign_activity()`. Le formulaire pointe vers `entryPoint=surveySubmit`. Chaque type de question a sa propre fonction d'affichage HTML.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `SuiteValidator` — validation UUID
  - `BeanFactory` — chargement survey
  - `Campaigns/utils.php` — `log_campaign_activity()`
  - `Sugar_Smarty` — page "sondage fermé"
  - Bootstrap CSS, rating.min.css, survey.css
- **Paramètres GET :** `id` (survey ID), `contact` (contact ID), `tracker` (tracker ID)

## 📤 Sorties / Exports
- HTML du formulaire de sondage public
- Fonctions : `displaySurvey()`, `displayQuestion()`, `displayRadioField()`, `displayMatrixField()`, `displayRatingField()`, `displayScaleField()`, `displayClosedPage()`

## 🔗 Relations clés
- **Appelé par :** Liens dans les emails de campagne (entryPoint)
- **Appelle :** `Surveys::get_linked_beans('surveys_surveyquestions')`, `SurveyQuestions::get_linked_beans('surveyquestions_surveyquestionoptions')`
- **Position dans le flux global :** Interface publique de soumission de sondage

---

## 💡 Points d'attention
- Pas de `sugarEntry` — fichier inclus via un point d'entrée (entryPoint).
- La désactivation du bouton submit via JS (`disableSubmitButton`) ne remplace pas une protection côté serveur contre les doubles soumissions.
- Status `Closed` affiche une page de fermeture personnalisée via `closeSurvey.tpl`.
