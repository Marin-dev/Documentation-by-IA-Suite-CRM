# 📁 SurveyQuestions

**Chemin :** `modules/SurveyQuestions/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module SurveyQuestions gère les questions individuelles des sondages. Chaque question est associée à un sondage et peut avoir des options (`SurveyQuestionOptions`).

## ⚙️ Responsabilité technique
Bean `SurveyQuestions` (Module Builder). Module simple généré automatiquement.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `Dashlets/` | Dashlet liste des questions | [→ CONTEXT](Dashlets/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues | [→ CONTEXT](metadata/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `SurveyQuestions.php` | Bean question de sondage | [→ fiche](SurveyQuestions.doc.md) |
| `vardefs.php` | Schéma de la table des questions | [→ fiche](vardefs.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consommé par :** Module `Surveys` (questions liées), `SurveyQuestionResponses`

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
