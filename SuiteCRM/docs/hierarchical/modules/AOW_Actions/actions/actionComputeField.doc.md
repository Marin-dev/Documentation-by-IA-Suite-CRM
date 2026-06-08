# actionComputeField.php

**Chemin :** `modules/AOW_Actions/actions/actionComputeField.php`
**Type :** PHP - Action workflow (classe concrete)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Action de workflow qui calcule la valeur d'un ou plusieurs champs d'un enregistrement via des formules `FormulaCalculator`. Permet de creer des automatisations de calcul (ex: concatenation, calcul de dates, compteurs).

## Role technique
Etend `actionBase`. Utilise `FormulaCalculator` pour evaluer les formules. Supporte deux modes de valeur : RAW (valeur brute) et FORMATTED (valeur formatee). Utilise `SuiteValidator` pour la validation des entrees.

---

## Dependances / Imports
- `actionBase` (classe parente)
- `modules/AOW_Actions/FormulaCalculator.php` — moteur de formules
- `SuiteCRM\Utility\SuiteValidator`

## Constantes
| Constante | Valeur | Role |
|---|---|---|
| `RAW_VALUE` | `"raw"` | Mode valeur brute |
| `FORMATTED_VALUE` | `"formatted"` | Mode valeur formatee |

## Relations cles
- **Appele par :** `AOW_WorkFlow->run_actions()` (dynamique)
- **Appelle :** `FormulaCalculator`, `SuiteValidator`

---

## Points d'attention
- La logique complete de `run_action` et `edit_display` est dans la suite du fichier (limite de lecture) — INCONNU pour les details d'execution.
- Contribue par "diligent technology & business consulting GmbH".
