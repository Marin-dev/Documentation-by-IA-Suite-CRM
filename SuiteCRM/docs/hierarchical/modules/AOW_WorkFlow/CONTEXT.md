# 📁 AOW_WorkFlow

**Chemin :** `modules/AOW_WorkFlow/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module AOW_WorkFlow est le moteur de workflows de SuiteCRM. Il permet de configurer des automatisations déclenchées sur sauvegarde de bean (`after_save`) ou par le scheduler (batch). Chaque workflow définit un module cible, des conditions (`AOW_Conditions`) et des actions (`AOW_Actions`) à exécuter. C'est le pivot de l'automatisation métier dans SuiteCRM.

## ⚙️ Responsabilité technique
Bean `AOW_WorkFlow` (hérite de `Basic`). Double mode d'exécution : hook `run_bean_flows()` (déclenchement temps réel) et `run_flows()` (batch scheduler). Protection anti-récursion via `$doNotRunInSaveLogic`. Chargement dynamique des actions depuis `AOW_Actions/actions/`. Cascade `mark_deleted` sur conditions/actions/processed.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `Dashlets/` | Dashlet liste des workflows | [→ CONTEXT](Dashlets/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `AOW_WorkFlow.php` | Bean et moteur principal des workflows | [→ fiche](AOW_WorkFlow.doc.md) |
| `aow_utils.php` | Utilitaires partagés (gestion des champs, modules) | [→ fiche](aow_utils.doc.md) |
| `controller.php` | Contrôleur MVC du module | [→ fiche](controller.doc.md) |
| `vardefs.php` | Schéma de la table `aow_workflow` | [→ fiche](vardefs.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `AOW_Conditions`, `AOW_Actions`, `AOW_Processed`, `AOBH_BusinessHours`, `BeanFactory`, `ACLController`
- **Consommé par :** Hooks `after_save` de tous les modules SuiteCRM, Scheduler SuiteCRM
- **Expose :** `run_bean_flows()` (appelé par les hooks), `run_flows()` (appelé par le scheduler)
- **Flux typique :** Bean sauvegardé → `run_bean_flows($bean)` → vérification conditions → exécution actions → `AOW_Processed` créé/mis à jour

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le moteur workflow | [`AOW_WorkFlow.php`](AOW_WorkFlow.doc.md) |
| Voir les conditions disponibles | [`AOW_Conditions/`](../AOW_Conditions/CONTEXT.md) |
| Voir les actions disponibles | [`AOW_Actions/actions/`](../AOW_Actions/actions/CONTEXT.md) |
| Voir les utilitaires partagés | [`aow_utils.php`](aow_utils.doc.md) |

---

## ⚠️ Zones INCONNU
- `Any_Change` : non évaluable par le scheduler
- `check_valid_bean` : double passe PHP + SQL pour les modules liés
