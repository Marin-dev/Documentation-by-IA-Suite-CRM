# Fichier actionModifyRecord.php

**Chemin :** `modules/AOW_Actions/actions/actionModifyRecord.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Action de workflow qui modifie les champs d'un enregistrement existant (le bean cible du workflow ou un bean lié via une relation). Hérite de `actionCreateRecord` et réutilise son interface de configuration.

## Type
helper (action)

---

## Dépendances clés
- `actionCreateRecord` (classe parente)
- `modules/AOW_WorkFlow/aow_utils.php` — `getModuleRelationships()`

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `actionModifyRecord` | classe | Action modification d'enregistrement |
| `run_action()` | méthode | Modifie les champs du bean cible ou d'un bean lié |
| `edit_display()` | méthode | Affiche le formulaire de configuration (module/relation, champs, valeurs) |

## Interactions
- **Appelé par :** `AOW_WorkFlow::run_actions()`
- **Appelle :** `actionCreateRecord::run_action()` (héritage)

## Notes
- La configuration permet de cibler le bean du workflow lui-même ou un bean dans une relation (`rel_type`).
- Utilise le même mécanisme de résolution de valeurs que `actionCreateRecord` (Field, Value, Date, Round_Robin, etc.).
