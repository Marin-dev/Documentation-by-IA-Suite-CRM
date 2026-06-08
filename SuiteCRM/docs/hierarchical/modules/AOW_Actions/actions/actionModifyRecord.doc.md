# actionModifyRecord.php

**Chemin :** `modules/AOW_Actions/actions/actionModifyRecord.php`
**Type :** PHP - Action workflow (classe concrete)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Action de workflow qui modifie les champs d'un enregistrement existant (le bean courant ou un bean lie). Permet par exemple de mettre a jour le statut, la date ou n'importe quel champ lors du declenchement d'un workflow.

## Role technique
Etend `actionCreateRecord`. Surcharge `edit_display` pour afficher un select de relation (`rel_type`) permettant de choisir quel module/enregistrement modifier. La logique de modification effective est dans `run_action` (heritee ou surchargee — INCONNU pour la suite).

---

## Dependances / Imports
- `actionCreateRecord` (classe parente — `modules/AOW_Actions/actions/actionCreateRecord.php`)
- `modules/AOW_WorkFlow/aow_utils.php` — `getModuleRelationships()`

## Parametres de configuration
| Parametre | Role |
|---|---|
| `rel_type` | Module ou relation a modifier (vide = record courant) |
| `record_type` | Type de record (module) |
| Champs de valeur | Tableau de champs a modifier avec leurs valeurs |

## Relations cles
- **Appele par :** `AOW_WorkFlow->run_actions()` (dynamique)
- **Herite de :** `actionCreateRecord`

---

## Points d'attention
- Le formulaire d'edition genere un select `rel_type` qui declenche `show_mrModuleFields($line)` en JavaScript lors du changement.
- La logique complete de `run_action` est INCONNU (non lue dans ce contexte).
