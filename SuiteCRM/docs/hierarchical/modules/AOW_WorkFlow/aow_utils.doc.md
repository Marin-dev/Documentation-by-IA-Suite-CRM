# aow_utils.php

**Chemin :** `modules/AOW_WorkFlow/aow_utils.php`
**Type :** PHP - Helper (fonctions utilitaires AOW)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Bibliotheque de fonctions utilitaires partagees par les modules AOW (Workflow) et AOR (Reports). Fournit des fonctions pour inspecter les champs et relations des modules, generer des widgets HTML de formulaires dynamiques, et formater/fixer les valeurs des champs selon leur type.

## Role technique
Fichier de fonctions globales PHP. Largement utilise par les controleurs AOR et AOW pour construire dynamiquement les formulaires d'edition de conditions et d'actions. Contient une liste de champs bloques pour le module `Users` (securite).

---

## Fonctions principales (partiellement visibles)
| Fonction | Role |
|---|---|
| `getModuleFields($module, $view, $value, $valid, $override)` | Retourne un tableau de champs disponibles pour un module (avec filtrage ACL et champs bloques Users) |
| `getRelatedModule($module, $rel)` | INCONNU — probablement retourne le module lie via une relation |
| `getModuleRelationships($module, $view, $rel_type)` | Retourne les relations d'un module (select HTML ou tableau) |
| `getModuleTreeData($module)` | Retourne les donnees arborescentes de navigation d'un module |
| `getModuleField($module, $field, $name, $view, $value, ...)` | Retourne le widget HTML d'un champ |
| `fixUpFormatting($module, $field, $value)` | Corrige le format d'une valeur selon le type du champ |
| `getRelatedEmailableFields($module)` | Retourne les champs de relation avec un email |
| `getEmailableModules()` | Retourne les modules ayant un champ email |
| `getAssignField($field, $view, $value)` | Retourne le widget de champ d'assignation utilisateur |
| `getDropdownList($list, $selected)` | Retourne un select HTML pour une liste de dropdowns |

**Consommateurs identifies :**
- `modules/AOR_Reports/controller.php`
- `modules/AOR_Reports/AOR_Report.php`
- `modules/AOR_Fields/AOR_Field.php`
- `modules/AOR_Conditions/AOR_Condition.php`
- `modules/AOW_WorkFlow/AOW_WorkFlow.php`
- `modules/AOW_Actions/AOW_Action.php`

## Points d'attention
- Les champs `Users` bloques incluent `id`, `user_hash`, `user_name`, `is_admin` — protection contre la modification des champs sensibles via le workflow.
- ACL est verifie via `ACLController::checkAccess($mod->module_dir, 'list', true)` pour chaque module.
- La logique complete de nombreuses fonctions est dans la suite du fichier (limite de lecture) — INCONNU pour les details.
