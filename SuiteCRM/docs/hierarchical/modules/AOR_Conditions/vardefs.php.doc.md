# Fichier vardefs.php — AOR_Conditions

**Chemin :** `modules/AOR_Conditions/vardefs.php`
**Type :** PHP — configuration
**Dernière mise à jour doc :** 2026-05-31

## Rôle fonctionnel
Définit le schéma de la table `aor_conditions` : champs (field, operator, value, value_type, logic_op, parenthesis, condition_order, module_path, parameter, aor_report_id).

## Type
config

## Notes
Utilise `VardefManager::createVardef` avec le template `basic`. Lié à AOR_Reports par `aor_report_id` (FK one-to-many).
