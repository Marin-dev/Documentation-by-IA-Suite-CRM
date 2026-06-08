# AOR_Condition.php

**Chemin :** `modules/AOR_Conditions/AOR_Condition.php`
**Type :** PHP - Modele (Model)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Modele representant une condition de filtrage dans un rapport AOR. Chaque condition correspond a une ligne de filtre (ex: "Montant > 1000") associee a un rapport. Gere la persistance des conditions depuis le formulaire d'edition.

## Role technique
Etend `Basic`. La methode `save_lines` parse les donnees POST pour creer/mettre a jour/supprimer les conditions. Les valeurs de type tableau (Date, Multi) sont serialisees en `base64(serialize(...))` avant stockage.

---

## Attributs principaux
| Attribut | Role |
|---|---|
| `aor_report_id` | FK vers le rapport parent |
| `condition_order` | Ordre d'evaluation de la condition |
| `field` | Champ cible de la condition |
| `logic_op` | Operateur logique (AND/OR) avec la condition precedente |
| `parenthesis` | Marqueur de parenthese (START ou id de la parenthese de fermeture) |
| `operator` | Operateur de comparaison (Equal_To, Contains, etc.) |
| `value` | Valeur de comparaison (peut etre serialisee) |
| `value_type` | Type de la valeur (Value, Field, Date, Multi, Period, CurrentUserID) |
| `parameter` | Booleen — si true, la condition est parametrable par l'utilisateur |
| `module_path` | Chemin de module serialise en base64 |

## Relations cles
- **Appele par :** `AOR_Report->save()` (via `save_lines`) et `AOR_Report->build_report_query_where()`
- **Table DB :** `aor_conditions`
- **Relation parent :** `aor_report_id` vers `aor_reports` (one-to-many)

---

## Points d'attention
- La gestion des parentheses utilise un tableau de pile `$lastParenthesisStartConditionIds` pour apparer les ouvertures et fermetures. Si une fermeture n'a pas d'ouverture correspondante, une `Exception` est levee.
- Le type `Period` est sauvegarde en `base64_encode($_POST['aor_conditions_value'][$i])` — pas via la logique generale du loop.
- Le champ `parameter` est normalise a `0` si absent du POST (checkbox non cochee).
