# Fichier actionComputeField.php

**Chemin :** `modules/AOW_Actions/actions/actionComputeField.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Action de workflow qui calcule et assigne une valeur à un champ d'un bean à partir d'une formule ou d'une valeur fixe. Utilise le moteur `FormulaCalculator` pour évaluer des expressions arithmétiques ou logiques.

## Type
helper (action)

---

## Dépendances clés
- `actionBase` (classe parente)
- `SuiteCRM\Utility\SuiteValidator` — validation
- `modules/AOW_Actions/FormulaCalculator.php` — évaluation de formules

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `actionComputeField` | classe | Action calcul de champ |
| `run_action()` | méthode | Calcule la valeur et l'assigne au champ du bean |
| `edit_display()` | méthode | Interface de configuration (champ cible, type, formule/valeur) |

## Interactions
- **Appelé par :** `AOW_WorkFlow::run_actions()`
- **Appelle :** `FormulaCalculator`

## Notes
- La formule peut référencer d'autres champs du bean via des variables.
- `SuiteValidator` est utilisé pour sécuriser les entrées de formule.
