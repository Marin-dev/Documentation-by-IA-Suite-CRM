# Fichier AOW_Condition.php

**Chemin :** `modules/AOW_Conditions/AOW_Condition.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Modèle d'une condition de workflow. Chaque enregistrement représente un critère de déclenchement : si le bean cible satisfait toutes les conditions, les actions du workflow s'exécutent. Gère la sauvegarde en masse depuis le formulaire POST.

## Type
model

---

## Dépendances clés
- `Basic` (classe parente)
- `modules/AOW_WorkFlow/aow_utils.php` — `fixUpFormatting()`, `encodeMultienumValue()`
- `BeanFactory`

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `AOW_Condition` | classe | Bean condition de workflow |
| `save_lines()` | méthode | Sauvegarde/supprime les conditions depuis POST |

### Champs importants
| Champ | Rôle |
|---|---|
| `aow_workflow_id` | Lien vers le workflow parent |
| `condition_order` | Ordre d'évaluation |
| `module_path` | Chemin de module sérialisé base64 |
| `field` | Champ cible |
| `operator` | Opérateur (Equal_To, Contains, Greater_Than, is_null, etc.) |
| `value` | Valeur de comparaison |
| `value_type` | Type de valeur (Value, Field, Date, Multi, Any_Change, SecurityGroup) |
| `condition_operator` | Opérateur de combinaison entre conditions (INCONNU — non utilisé dans le code lu) |

## Interactions
- **Appelé par :** `AOW_WorkFlow::save()`, `AOW_WorkFlow::build_flow_query_where()`, `AOW_WorkFlow::check_valid_bean()`
- **Table BD :** `aow_conditions`

## Notes
- Similaire à `AOR_Condition` mais pour les workflows — les types de valeurs diffèrent légèrement (ajout `Any_Change`, `SecurityGroup`).
- `module_path` est sérialisé comme dans AOR : `base64_encode(serialize($array))`.
- `bean_implements()` retourne `false` — pas d'ACL propre, protégé par le workflow parent.
