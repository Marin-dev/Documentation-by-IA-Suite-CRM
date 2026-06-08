# Fichier AOR_Condition.php

**Chemin :** `modules/AOR_Conditions/AOR_Condition.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Modèle d'une condition de filtrage associée à un rapport AOR. Chaque enregistrement représente une ligne de condition (champ, opérateur, valeur, type de valeur, ordre, opérateur logique AND/OR, parenthèses). Gère la sauvegarde en masse depuis le formulaire POST.

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
| `AOR_Condition` | classe | Bean condition de rapport |
| `save_lines()` | méthode | Sauvegarde/supprime les lignes de conditions depuis POST |

### Champs importants
| Champ | Rôle |
|---|---|
| `aor_report_id` | Lien vers le rapport parent |
| `condition_order` | Ordre d'exécution |
| `field` | Nom du champ cible |
| `logic_op` | Opérateur logique (AND/OR) |
| `parenthesis` | START ou CLOSE pour les groupes de conditions |
| `operator` | Opérateur de comparaison (Equal_To, Contains, etc.) |
| `value` | Valeur de comparaison |
| `value_type` | Type de valeur (Value, Field, Date, Period, Multi, CurrentUserID) |
| `parameter` | Si 1 : condition paramétrable dynamiquement |
| `module_path` | Chemin du module (sérialisé base64) |

## Interactions
- **Appelé par :** `AOR_Report::save()`, `AOR_Report::build_report_query_where()`
- **Table BD :** `aor_conditions`

## Notes
- `save_lines()` gère la correspondance des parenthèses START/CLOSE via une pile `$lastParenthesisStartConditionIds`. Une exception est levée si une parenthèse CLOSE n'a pas de START correspondant.
- Les valeurs de type Date sont sérialisées en base64 (`base64_encode(serialize($array))`).
- Les valeurs Period sont sauvegardées en base64 simple (`base64_encode($string)`).
- `module_path` est stocké comme `base64_encode(serialize(explode(':', $path)))`.
