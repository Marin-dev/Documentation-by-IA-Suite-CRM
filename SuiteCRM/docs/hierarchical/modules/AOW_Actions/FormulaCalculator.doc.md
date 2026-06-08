# FormulaCalculator.php

**Chemin :** `modules/AOW_Actions/FormulaCalculator.php`
**Type :** PHP - Helper (moteur de formules)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Moteur d'evaluation de formules pour l'action `CalculateFields` du workflow AOW. Permet de calculer des valeurs complexes en combinant des fonctions logiques, mathematiques, de chaines et de dates, avec des parametres variables.

## Role technique
Deux classes : `FormulaNode` (noeud d'arbre syntaxique) et `FormulaCalculator` (evaluateur). Le parsing transforme la formule textuelle en arbre (`createTree`), puis l'arbre est evalue recursivement (`evaluateTreeLevel`). Les fonctions sont encadrees par `{...}`, les parametres separes par `;`.

---

## Fonctions supportees
| Categorie | Fonctions |
|---|---|
| Logique | `equal`, `notEqual`, `greaterThan`, `greaterThanOrEqual`, `lessThan`, `lessThanOrEqual`, `empty`, `notEmpty`, `not`, `and`, `or`, `ifThenElse` |
| Chaines | `substring`, `length`, `replace`, `position`, `lowercase`, `uppercase` |
| Maths | `add`, `subtract`, `multiply`, `divide`, `power`, `squareRoot`, `absolute` |
| Dates | `now`, `yesterday`, `tomorrow`, `date`, `datediff`, `addYears/Months/Days/Hours/Minutes/Seconds`, `subtractYears/Months/Days/Hours/Minutes/Seconds` |
| Compteurs | `GlobalCounter`, `GlobalCounterPerUser`, `GlobalCounterPerModule`, `GlobalCounterPerUserPerModule`, `DailyCounter*` |

## Parametres de substitution
- `{P0}`, `{P1}`, ... — parametres du bean courant
- `{R0}`, `{R1}`, ... — parametres de relation
- Variables globales : compteurs incrementaux persistants dans la config SuiteCRM

## Relations cles
- **Appele par :** `actionComputeField` (INCONNU — non lu dans ce contexte)
- **Appelle :** `Configurator` (pour les compteurs globaux)

---

## Points d'attention
- Les compteurs globaux (`GlobalCounter*`) sont stockes dans la table de configuration SuiteCRM via `Configurator->saveConfig()` — acces concurrent possible.
- `divide` par zero retourne `INF` (pas d'exception).
- `getDBFormat` convertit les dates du format utilisateur vers le format DB avant calcul — depend de `$current_user->timezone`.
- Le mode debug (`SweeterCalc.DebugEnabled`) ecrit dans un fichier log configurable depuis l'interface.
