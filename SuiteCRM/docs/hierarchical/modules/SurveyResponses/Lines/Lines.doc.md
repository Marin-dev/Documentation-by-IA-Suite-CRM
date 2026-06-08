# 📄 Lines.php (SurveyResponses)

**Chemin :** `modules/SurveyResponses/Lines/Lines.php`
**Type :** PHP — Helper / Affichage réponses
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Fournit les fonctions d'affichage des réponses à un sondage dans la vue DetailView d'une SurveyResponse. Formate chaque réponse selon le type de question (texte, booléen, date, choix, matrice, rating, scale).

## ⚙️ Rôle technique
Fonctions PHP globales. `question_responses_display()` charge toutes les `SurveyQuestionResponses` liées et les groupe par question. `convertQuestionResponseForDisplay()` traduit les données brutes en HTML selon le type. Rendu via template Smarty `detailquestionresponses.tpl`.

---

## 📥 Entrées / Dépendances
- `SurveyResponses $focus` — réponse au sondage
- `Sugar_Smarty` — rendu template
- `BeanFactory` — chargement SurveyQuestions, SurveyQuestionOptions
- `$timedate` — formatage dates
- `$app_list_strings['surveys_matrix_options']` — libellés matrice

## 📤 Sorties / Exports
- `question_responses_display()` — HTML des réponses formatées
- `convertQuestionResponseForDisplay()` — conversion réponse → HTML

## 🔗 Relations clés
- **Appelé par :** Vue DetailView de SurveyResponses (via métadonnées)
- **Position dans le flux global :** Affichage des réponses d'un participant dans l'interface admin

---

## 💡 Points d'attention
- Le mode EditView retourne une chaîne vide — les réponses ne sont pas éditables.
- Le rating affiche des étoiles en HTML (`<img>`).
