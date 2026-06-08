# Fichier : vardefs.php

**Chemin :** `modules/Calls_Reschedule/vardefs.php`
**Type :** config (definition du schema)
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure
Definition du schema `$dictionary['Calls_Reschedule']` pour la table `calls_reschedule`.

## Parametres cles
| Parametre | Valeur | Effet |
|---|---|---|
| `table` | `calls_reschedule` | table SQL |
| `audited` | `true` | audit des modifications |
| `reason` | enum `call_reschedule_dom` | raison de la replanification |
| `call_id` | id | FK vers `calls` |
| `call_name` | relate (non-db) | nom de l'appel lie |
| `optimistic_locking` | `true` | protection editions concurrentes |

## Dependances
- `VardefManager::createVardef('Calls_Reschedule', 'Calls_Reschedule', ['basic', 'assignable'])`

---

## Points d'attention
- Pas de relations many-to-many declarees — relation simple via `call_id`.
