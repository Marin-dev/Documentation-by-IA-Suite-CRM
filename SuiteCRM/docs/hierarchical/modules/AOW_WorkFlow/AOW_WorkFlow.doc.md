# AOW_WorkFlow.php

**Chemin :** `modules/AOW_WorkFlow/AOW_WorkFlow.php`
**Type :** PHP - Modele (Model)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Modele principal du moteur de workflow AOW (Advanced OpenWorkflow). Orchestre l'execution automatique d'actions (envoi d'emails, modification de champs, creation de records) sur des enregistrements CRM selon des conditions configurables. Peut etre declenche par un scheduler ou lors de la sauvegarde d'un bean.

## Role technique
Etend `Basic`. Contient la logique complete de selection des beans cibles (via requete SQL construite dynamiquement), de verification des conditions, et d'execution des actions. La methode `run_bean_flows` est appelee dans les hooks `after_save` des modules cibles. La methode `run_flows` est appelee par le scheduler.

---

## Attributs principaux
| Attribut | Role |
|---|---|
| `flow_module` | Module cible du workflow |
| `status` | Statut (Active/Inactive) |
| `run_when` | Declencheur (Always, On_Save, In_Scheduler, Create) |
| `flow_run_on` | Filtre sur records (New_Records, Modified_Records) |
| `multiple_runs` | Si false, ne s'execute qu'une fois par record |
| `$doNotRunInSaveLogic` | Statique — evite les boucles de recursion lors d'execution scheduler |

## Methodes principales
| Methode | Role |
|---|---|
| `run_flows()` | Selectionne et execute tous les workflows actifs (appele par scheduler) |
| `run_flow()` | Execute le workflow sur les beans correspondants |
| `run_bean_flows(SugarBean $bean)` | Execute les workflows applicables lors d'une sauvegarde de bean |
| `get_flow_beans()` | Retourne les beans correspondant aux conditions SQL |
| `build_flow_query_where($query)` | Construit le WHERE SQL avec conditions et filtre "non deja traite" |
| `build_query_where(AOW_Condition, $module, $query)` | Ajoute une condition SQL pour un champ specifique |
| `check_valid_bean(SugarBean $bean)` | Verifie si un bean satisfait toutes les conditions (evaluation PHP) |
| `compare_condition($var1, $var2, $operator)` | Compare deux valeurs avec un operateur logique |
| `run_actions(SugarBean $bean, $in_save)` | Execute les actions du workflow sur un bean |
| `check_in_group($bean_id, $module, $group)` | Verifie si un record appartient a un groupe securite |

## Relations cles
- **Appele par :** Scheduler SuiteCRM, hooks `after_save` de modules
- **Appelle :** `AOW_Condition`, `AOW_Action`, `AOW_Processed`, `BeanFactory`, `AOBH_BusinessHours`
- **Table DB :** `aow_workflow`
- **Relations 1-N :** vers `aow_conditions`, `aow_actions`, `aow_processed`

---

## Points d'attention
- `$doNotRunInSaveLogic = true` pendant `run_flow()` pour eviter les boucles de recursion (un workflow qui modifie un bean ne doit pas re-declencher d'autres workflows dans le meme contexte).
- La verification `check_valid_bean` est faite en deux passes : evaluation PHP directe pour les champs du module principal, requete SQL pour les champs de modules lies.
- Les actions sont chargees dynamiquement depuis `modules/AOW_Actions/actions/action{Nom}.php` avec support override depuis `custom/modules/AOW_Actions/actions/`.
- Le type `Any_Change` dans les conditions n'est pas evaluable par le scheduler (retourne `array()` vide).
- `mark_deleted` supprime en cascade toutes les conditions, actions et processed lies.
