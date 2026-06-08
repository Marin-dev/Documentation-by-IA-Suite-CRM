# 📄 Lines.php (Surveys)

**Chemin :** `modules/Surveys/Lines/Lines.php`
**Type :** PHP — Helper / Affichage questions
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Fournit les fonctions d'affichage des questions de sondage dans les vues Edit et Detail du back-office SuiteCRM. Rend le HTML des questions via des templates Smarty selon que le sondage a déjà des réponses ou non.

## ⚙️ Rôle technique
Fonctions PHP globales (pas de classe). `survey_questions_display()` bascule entre mode édition (si pas de réponses) et mode lecture seule. En mode édition, charge les questions avec leurs options pour le template `editsurveyquestions.tpl`. En mode détail, utilise `detailsurveyquestions.tpl`.

---

## 📥 Entrées / Dépendances
- `Surveys $focus` — objet sondage
- `Sugar_Smarty` — rendu templates
- `get_custom_file_if_exists()` — fichiers template
- `get_select_options_with_id()` — liste des types de questions

## 📤 Sorties / Exports
- `survey_questions_display(Surveys, field, value, view): string` — HTML des questions
- `survey_questions_display_edit()` — mode édition
- `survey_questions_display_detail()` — mode lecture

## 🔗 Relations clés
- **Appelé par :** Métadonnées de la vue Edit/Detail (via champ custom `survey_questions`)
- **Position dans le flux global :** Rendu du panneau questions dans les vues admin du sondage

---

## 💡 Points d'attention
- Un sondage ayant des réponses devient en lecture seule dans EditView — protège l'intégrité des données.
- `isDuplicate` en session permet de bypasser la protection en cas de duplication.
