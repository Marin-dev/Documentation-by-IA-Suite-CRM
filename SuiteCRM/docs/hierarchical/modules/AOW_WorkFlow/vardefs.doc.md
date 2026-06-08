# vardefs.php (AOW_WorkFlow)

**Chemin :** `modules/AOW_WorkFlow/vardefs.php`
**Type :** PHP - Configuration (definition des champs)
**Derniere mise a jour doc :** 2026-05-31

## Ce que ce fichier configure
Definit le schema de la table `aow_workflow` et les champs/relations du module AOW_WorkFlow.

## Champs cles attendus (bases sur les attributs de la classe)
| Champ | Type attendu | Description |
|---|---|---|
| `flow_module` | enum | Module cible du workflow |
| `status` | enum | Active/Inactive |
| `run_when` | enum | Always, On_Save, In_Scheduler, Create |
| `flow_run_on` | enum | New_Records, Modified_Records |
| `multiple_runs` | bool | Autoriser plusieurs executions par record |

## Relations (bases sur les methodes de la classe)
| Relation | Type | Module lie |
|---|---|---|
| `aow_conditions` | link (1-N) | AOW_Conditions |
| `aow_actions` | link (1-N) | AOW_Actions |
| `aow_processed` | link (1-N) | AOW_Processed |

## Points d'attention
- Contenu exact INCONNU — fichier non lu directement.
