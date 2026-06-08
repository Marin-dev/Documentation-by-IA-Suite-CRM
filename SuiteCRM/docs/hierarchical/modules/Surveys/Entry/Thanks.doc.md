# 📄 Thanks.php (Entry)

**Chemin :** `modules/Surveys/Entry/Thanks.php`
**Type :** PHP — Point d'entrée public (page de remerciements)
**Dernière mise à jour doc :** 2026-05-31

---

## 🎯 Rôle fonctionnel
Affiche la page de remerciements après la soumission d'un sondage. Page HTML minimale accessible publiquement via l'entryPoint `surveyThanks`.

## ⚙️ Rôle technique
Script procédural. Récupère le nom du sondage depuis `$_REQUEST['name']`, traduit le message de remerciement via `translate('LBL_SURVEY_THANKS', 'Surveys')`. Rendu HTML Bootstrap autonome.

---

## 📥 Entrées / Dépendances
- `$_REQUEST['name']` — nom du sondage (facultatif, défaut "Survey")
- `translate()` — traduction du message

## 📤 Sorties / Exports
- Page HTML de remerciements

## 🔗 Relations clés
- **Appelé par :** Redirection depuis `Entry/SurveySubmit.php`
- **Position dans le flux global :** Dernière étape du parcours de soumission de sondage

---

## 💡 Points d'attention
- RAS — page de remerciements simple.
