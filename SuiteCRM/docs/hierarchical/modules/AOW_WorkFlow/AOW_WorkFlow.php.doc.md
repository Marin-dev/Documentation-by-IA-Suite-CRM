# Fichier AOW_WorkFlow.php

**Chemin :** `modules/AOW_WorkFlow/AOW_WorkFlow.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Modèle principal du moteur de workflow. Représente un flux de travail configurable attaché à un module SuiteCRM. Orchestre l'évaluation des conditions et l'exécution des actions sur les beans correspondants. Peut être déclenché par le scheduler (run_flows) ou lors de la sauvegarde d'un bean (run_bean_flows).

## Type
model

---

## Dépendances clés
- `Basic` (classe parente)
- `modules/AOW_WorkFlow/aow_utils.php` — utilitaires partagés
- `modules/AOW_Conditions/AOW_Condition.php` — conditions du workflow
- `modules/AOW_Actions/AOW_Action.php` — actions du workflow
- `modules/AOW_Processed/AOW_Processed.php` — journal d'exécution
- `modules/AOBH_BusinessHours/AOBH_BusinessHours.php` — heures ouvrées (optionnel)
- `BeanFactory`, `$beanList`, `$app_list_strings`

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `AOW_WorkFlow` | classe | Bean workflow |
| `$doNotRunInSaveLogic` | static bool | Guard anti-récursion lors de l'exécution depuis save |
| `run_flows()` | méthode | Exécute tous les workflows actifs (depuis scheduler) |
| `run_flow()` | méthode | Exécute un workflow sur tous les beans correspondants |
| `run_bean_flows()` | méthode | Exécute les workflows applicables lors de la sauvegarde d'un bean |
| `get_flow_beans()` | méthode | Requête SQL pour sélectionner les beans à traiter |
| `build_flow_query_where()` | méthode | Construit la clause WHERE (conditions + multiple_runs + deleted) |
| `build_query_where()` | méthode | Évalue une condition individuelle (SQL ou comparaison PHP) |
| `check_valid_bean()` | méthode | Vérifie qu'un bean satisfait toutes les conditions du workflow |
| `compare_condition()` | méthode | Comparaison de valeurs (==, !=, >, <, Contains, One_of, etc.) |
| `run_actions()` | méthode | Exécute toutes les actions du workflow sur un bean |
| `check_in_group()` | méthode | Vérifie si un bean appartient à un groupe de sécurité |
| `load_flow_beans()` | méthode | Charge la liste `aow_moduleList` dans `$app_list_strings` |
| `mark_deleted()` | méthode | Supprime le workflow + conditions + actions + processed |
| `save()` | méthode | Sauvegarde workflow + conditions + actions |

### Champs importants
| Champ | Rôle |
|---|---|
| `flow_module` | Module cible du workflow |
| `status` | Active / Inactive |
| `run_when` | Always, On_Save, In_Scheduler, Create |
| `flow_run_on` | New_Records ou Modified_Records (filtre temporel) |
| `multiple_runs` | Si faux : s'exécute une seule fois par bean |

## Interactions
- **Appelé par :** Scheduler SuiteCRM (`cron.php`), hook `after_save` sur tous les modules
- **Appelle :** `AOW_Condition`, `AOW_Action` (dynamiquement via `require_once`), `AOW_Processed`
- **Table BD :** `aow_workflow`, `aow_conditions`, `aow_actions`, `aow_processed`

## Notes
- Les actions sont chargées dynamiquement depuis `modules/AOW_Actions/actions/action{Name}.php` avec fallback `custom/`.
- `$doNotRunInSaveLogic` est un flag statique pour éviter la récursion infinie lors de l'exécution en save.
- `run_when = 'Create'` est traité à la fois par le scheduler ET par `run_bean_flows` (ligne 229).
- Le type de condition `Any_Change` n'est pas supporté depuis le scheduler (retourne tableau vide) — uniquement via `check_valid_bean`.
- Support des heures ouvrées via `AOBH_BusinessHours` pour les conditions de type Date avec unité `business_hours`.
