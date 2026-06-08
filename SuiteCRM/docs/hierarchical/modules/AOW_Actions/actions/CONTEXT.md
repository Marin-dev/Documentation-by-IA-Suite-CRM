# 📁 actions

**Chemin :** `modules/AOW_Actions/actions/`
**Profondeur :** 4
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Contient les classes d'actions concrètes du moteur de workflow AOW. Chaque classe implémente un type d'action exécutable sur un bean CRM lors du déclenchement d'un workflow.

## ⚙️ Responsabilité technique
Classes PHP héritant de `actionBase`. Chargées dynamiquement par `AOW_WorkFlow::run_actions()` selon le type d'action (`action{NomAction}`). Supportent les overrides dans `custom/modules/AOW_Actions/actions/`.

---

## 📂 Contenu

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `actionBase.php` | Classe de base abstraite pour toutes les actions | [→ fiche](actionBase.doc.md) |
| `actionSendEmail.php` | Action d'envoi d'email avec template | [→ fiche](actionSendEmail.doc.md) |
| `actionModifyRecord.php` | Action de modification de champs d'un enregistrement | [→ fiche](actionModifyRecord.doc.md) |
| `actionCreateRecord.php` | Action de création d'un nouvel enregistrement | [→ fiche](actionCreateRecord.doc.md) |
| `actionComputeField.php` | Action de calcul de champ via formule | [→ fiche](actionComputeField.doc.md) |
| `templateParser.php` | Parseur de templates pour les emails workflow | [→ fiche](templateParser.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Appelé par :** `AOW_WorkFlow::run_actions()` (chargement dynamique)
- **Peut être surchargé dans :** `custom/modules/AOW_Actions/actions/custom{NomAction}.php`
- **Flux typique :** Workflow déclenché → `run_actions()` → charge `action{Nom}` → appelle `run_action($bean, $params, $in_save)`

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre l'interface des actions | [`actionBase.php`](actionBase.doc.md) |
| Voir l'envoi d'email depuis workflow | [`actionSendEmail.php`](actionSendEmail.doc.md) |
| Voir la modification de champs | [`actionModifyRecord.php`](actionModifyRecord.doc.md) |
| Voir la création d'enregistrement | [`actionCreateRecord.php`](actionCreateRecord.doc.md) |

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
