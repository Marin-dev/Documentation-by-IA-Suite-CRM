# vardefs.php (AOR_Reports)

**Chemin :** `modules/AOR_Reports/vardefs.php`
**Type :** PHP - Configuration (definition des champs)
**Derniere mise a jour doc :** 2026-05-31

## Ce que ce fichier configure
Definit le schema de la table `aor_reports` et les relations du module AOR_Reports.

## Champs specifiques au module
| Champ | Type | Description |
|---|---|---|
| `report_module` | enum (`aor_moduleList`) | Module cible du rapport |
| `graphs_per_row` | int (defaut: 2) | Nombre de graphiques par ligne dans le PDF |
| `field_lines` | function (non-db) | Rendu HTML des lignes champs (via `fieldLines.php`) |
| `condition_lines` | function (non-db) | Rendu HTML des lignes conditions (via `conditionLines.php`) |

## Relations definies
| Relation | Type | Module lie |
|---|---|---|
| `aor_fields` | link (1-N) | AOR_Fields (`aor_report_id`) |
| `aor_conditions` | link (1-N) | AOR_Conditions (`aor_report_id`) |
| `aor_charts` | link | AOR_Charts |
| `aor_scheduled_reports` | link (1-N) | AOR_Scheduled_Reports (`aor_report_id`) |

## Mixins appliques
`VardefManager::createVardef('AOR_Reports', 'AOR_Report', ['basic', 'assignable', 'security_groups'])`
