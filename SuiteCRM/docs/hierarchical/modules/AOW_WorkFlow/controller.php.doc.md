# Fichier controller.php — AOW_WorkFlow

**Chemin :** `modules/AOW_WorkFlow/controller.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Contrôleur du module AOW_WorkFlow. Gère les requêtes AJAX de l'interface d'édition du workflow (champs de module, relations, types, widgets de saisie) en délégant aux fonctions de `aow_utils.php`.

## Type
controller

## Dépendances clés
- `SugarController`
- `modules/AOW_WorkFlow/aow_utils.php`

## Exports / Symboles principaux
| Symbole | Rôle |
|---|---|
| `AOW_WorkFlowController` | Classe contrôleur |
| Actions AJAX (getModuleFields, getModuleRelationships, getModuleField, etc.) | Même pattern que `AOR_ReportsController` |

## Notes
Partagent la même logique AJAX que `AOR_ReportsController` — les actions de type `getModuleFields`, `getModuleField`, `getRelFieldTypeSet`, etc. sont dupliquées entre les deux contrôleurs.
