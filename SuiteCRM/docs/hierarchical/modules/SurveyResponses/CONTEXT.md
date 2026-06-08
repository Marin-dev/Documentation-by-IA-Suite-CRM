# 📁 SurveyResponses

**Chemin :** `modules/SurveyResponses/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module SurveyResponses gère les réponses globales d'un répondant à un sondage. Chaque enregistrement représente la soumission complète d'un sondage par un contact ou prospect, avec l'ensemble de ses réponses aux questions.

## ⚙️ Responsabilité technique
Bean généré par Module Builder. Agrège les `SurveyQuestionResponses` pour une soumission complète.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `Lines/` | Gestion des lignes de réponses | [→ CONTEXT](Lines/CONTEXT.md) |
| `Dashlets/` | Dashlet liste des réponses | [→ CONTEXT](Dashlets/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues | [→ CONTEXT](metadata/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `SurveyResponses.php` | Bean réponse globale à un sondage | [→ fiche](SurveyResponses.doc.md) |
| `vardefs.php` | Schéma de la table | [→ fiche](vardefs.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consommé par :** Module `Surveys` (collecte des réponses), rapports de sondage
- **Contient :** `SurveyQuestionResponses` (réponses par question)

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
