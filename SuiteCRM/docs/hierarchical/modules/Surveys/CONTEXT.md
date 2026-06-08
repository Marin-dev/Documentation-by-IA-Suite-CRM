# 📁 Surveys

**Chemin :** `modules/Surveys/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module Surveys gère les sondages dans SuiteCRM. Permet de créer des questionnaires avec des questions multiples (`SurveyQuestions`), de les envoyer à des destinataires via un lien externe, et de collecter et analyser les réponses.

## ⚙️ Responsabilité technique
Bean `Surveys` (Module Builder). Architecture avec sous-dossiers `Entry/` (formulaire public), `Lines/` (gestion des lignes), `Utils/` et `views/`. Point d'entrée public pour les répondants.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `Entry/` | Point d'entrée public et soumission du sondage | [→ CONTEXT](Entry/CONTEXT.md) |
| `Lines/` | Gestion des lignes de questions | [→ CONTEXT](Lines/CONTEXT.md) |
| `views/` | Vue des rapports de sondage | [→ CONTEXT](views/CONTEXT.md) |
| `Utils/` | Utilitaires du module | [→ CONTEXT](Utils/CONTEXT.md) |
| `Dashlets/` | Dashlet liste des sondages | [→ CONTEXT](Dashlets/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues | [→ CONTEXT](metadata/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `Surveys.php` | Bean principal des sondages | [→ fiche](Surveys.doc.md) |
| `controller.php` | Contrôleur MVC | [→ fiche](controller.doc.md) |
| `vardefs.php` | Schéma de la table des sondages | [→ fiche](vardefs.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `SurveyQuestions`, `SurveyQuestionOptions`, `SurveyResponses`, `SurveyQuestionResponses`
- **Consommé par :** Campaigns (envoi des sondages via emails)
- **Flux typique :** Création sondage → questions ajoutées → envoi lien → réponse via `Entry/` → rapports dans `views/`

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
