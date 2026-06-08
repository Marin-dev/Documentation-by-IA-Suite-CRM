# 📁 SurveyQuestionResponses

**Chemin :** `modules/SurveyQuestionResponses/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module SurveyQuestionResponses stocke les réponses individuelles à chaque question d'un sondage. Lie une réponse globale (`SurveyResponses`) à une question spécifique et sa valeur.

## ⚙️ Responsabilité technique
Bean généré par Module Builder. Module de liaison entre `SurveyResponses` et `SurveyQuestions`.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `Dashlets/` | Dashlet des réponses aux questions | [→ CONTEXT](Dashlets/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues | [→ CONTEXT](metadata/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `SurveyQuestionResponses.php` | Bean réponse à une question | [→ fiche](SurveyQuestionResponses.doc.md) |
| `vardefs.php` | Schéma de la table | [→ fiche](vardefs.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consommé par :** `SurveyResponses` (réponses liées aux questions)

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
