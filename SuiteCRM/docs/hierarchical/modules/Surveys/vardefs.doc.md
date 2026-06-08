# ⚙️ vardefs.php (Surveys)

**Chemin :** `modules/Surveys/vardefs.php`
**Configure :** Schéma de la table `surveys`
**Dernière mise à jour doc :** 2026-05-31

## 🎯 Ce que ce fichier configure
Définit les champs du module Surveys : `status` (Pending/Public/Closed), `submit_text`, `satisfied_text`, `neither_text`, `dissatisfied_text`, et les relations vers les questions et réponses.

## 🔑 Paramètres clés
| Paramètre | Valeur | Effet |
|---|---|---|
| `status` | enum | Contrôle l'accès public au sondage |
| `submit_text` | varchar | Texte personnalisé du bouton submit |
| Relations | `surveys_surveyquestions`, `surveys_surveyresponses` | Liens vers questions et réponses |

## 💡 Points d'attention
- Fichier non lu intégralement — détails INCONNU.
