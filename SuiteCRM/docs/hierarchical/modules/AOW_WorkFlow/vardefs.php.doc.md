# Fichier vardefs.php — AOW_WorkFlow

**Chemin :** `modules/AOW_WorkFlow/vardefs.php`
**Type :** PHP — configuration
**Dernière mise à jour doc :** 2026-05-31

## Rôle fonctionnel
Définit le schéma de la table `aow_workflow` : champs (flow_module, status, run_when, flow_run_on, multiple_runs, run_on_import, condition_lines, action_lines) et relations vers AOW_Conditions, AOW_Actions, AOW_Processed.

## Type
config

## Notes
Template VardefManager `basic`, `assignable`, `security_groups`. Les champs `condition_lines` et `action_lines` sont des function fields non-db.
