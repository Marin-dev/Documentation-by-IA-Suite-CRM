# actionCreateRecord.php

**Chemin :** `modules/AOW_Actions/actions/actionCreateRecord.php`
**Type :** PHP - Action workflow (classe concrete)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Action de workflow qui cree un nouvel enregistrement dans un module CRM avec des valeurs configurees. Permet par exemple de creer automatiquement une tache, un email ou un autre record lors du declenchement d'un workflow.

## Role technique
Etend `actionBase`. Charge le fichier JS `actionCreateRecord.js` pour le formulaire d'edition. La methode `edit_display` genere le HTML du formulaire de configuration de l'action. La logique de creation du record est dans `run_action` (non visible dans le troncon lu).

---

## Dependances / Imports
- `actionBase` (classe parente)

## Methodes
| Methode | Role |
|---|---|
| `loadJS()` | Charge `actionCreateRecord.js` |
| `edit_display($line, $bean, $params)` | Genere le HTML du formulaire de configuration |
| `run_action($bean, $params, $in_save)` | Cree le record cible (logique INCONNU — suite non lue) |

## Relations cles
- **Etendue par :** `actionModifyRecord` (heritage direct)
- **Appele par :** `AOW_WorkFlow->run_actions()` (dynamique)

---

## Points d'attention
- `actionModifyRecord` etend directement `actionCreateRecord` — partage la logique de selection de module et de champs.
