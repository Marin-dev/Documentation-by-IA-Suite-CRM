# AOW_Action.php

**Chemin :** `modules/AOW_Actions/AOW_Action.php`
**Type :** PHP - Modele (Model)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Modele representant une action de workflow AOW. Chaque action est une etape a executer sur un enregistrement CRM quand le workflow est declenche (ex: envoyer un email, modifier un champ, creer un enregistrement).

## Role technique
Etend `Basic`. La methode `save_lines` parse le POST et serialise les parametres de chaque action en `base64(serialize(array))`. Les parametres sont specifiques a chaque type d'action et varies selon le type.

---

## Attributs principaux
| Attribut | Role |
|---|---|
| `aow_workflow_id` | FK vers le workflow parent |
| `action_order` | Ordre d'execution de l'action |
| `action` | Nom du type d'action (ex: `SendEmail`, `ModifyRecord`, `CreateRecord`, `CalculateFields`) |
| `parameters` | Parametres serialises en `base64(serialize(array))` |

## Relations cles
- **Appele par :** `AOW_WorkFlow->save()` (via `save_lines`), `AOW_WorkFlow->run_actions()` (via chargement dynamique)
- **Table DB :** `aow_actions`
- **Relation parent :** `aow_workflow_id` vers `aow_workflow`
- **Classes d'actions concretes :** `actionSendEmail`, `actionModifyRecord`, `actionCreateRecord`, `actionComputeField`

---

## Points d'attention
- La logique de formatage des valeurs (`fixUpFormatting`) est appliquee aux parametres de type `Value` — tient compte du module cible via `rel_type` si une relation est specifiee.
- Les parametres multienum sont encodes via `encodeMultienumValue`.
- `bean_implements` retourne toujours `false` — pas de ACL sur les actions.
