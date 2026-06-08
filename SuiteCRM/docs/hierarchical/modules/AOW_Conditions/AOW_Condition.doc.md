# AOW_Condition.php

**Chemin :** `modules/AOW_Conditions/AOW_Condition.php`
**Type :** PHP - Modele (Model)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Modele representant une condition de declenchement dans un workflow AOW. Chaque condition definit une regle a verifier sur un enregistrement (ex: "Statut = Ferme"). L'ensemble des conditions doit etre satisfait pour que le workflow s'execute.

## Role technique
Etend `Basic`. La methode `save_lines` parse le POST et persiste les conditions. Les types de valeurs (`Date`, `Multi`, `module_path`) sont serialises en base64. Supporte les conditions sur les modules lies via `module_path`.

---

## Attributs principaux
| Attribut | Role |
|---|---|
| `aow_workflow_id` | FK vers le workflow parent |
| `condition_order` | Ordre d'evaluation |
| `module_path` | Chemin de module serialise (pour conditions sur relations) |
| `field` | Champ cible |
| `operator` | Operateur (Equal_To, Not_Equal_To, Greater_Than, Contains, Starts_With, Ends_With, is_null) |
| `value` | Valeur de comparaison |
| `value_type` | Type (Value, Field, Date, Multi, Any_Change, SecurityGroup) |
| `condition_operator` | Operateur logique avec condition suivante (INCONNU — non utilise dans code lu) |

## Relations cles
- **Appele par :** `AOW_WorkFlow->save()` (via `save_lines`), `AOW_WorkFlow->build_flow_query_where()`, `check_valid_bean()`
- **Table DB :** `aow_conditions`
- **Relation parent :** `aow_workflow_id` vers `aow_workflow`

---

## Points d'attention
- `bean_implements` retourne toujours `false` — pas de ACL sur les conditions.
- Le type `Any_Change` ne peut pas etre evalue par le scheduler (necessite la valeur `fetched_row` du bean precedent la sauvegarde).
- Le type `SecurityGroup` verifie l'appartenance a un groupe de securite via une sous-requete SQL sur `securitygroups_records`.
