# Fichier : field_arrays.php

**Chemin :** `modules/Opportunities/field_arrays.php`
**Type :** `PHP`
**Categorie :** configuration (tableau de champs cache)
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure

Definit `$fields_array['Opportunity']` : `column_fields`, `list_fields` et `required_fields`.

---

## Parametres cles

| Parametre | Contenu |
| --- | --- |
| `column_fields` | amount, currency_id, date_closed, name, probability, sales_stage, lead_source, description, etc. |
| `list_fields` | id, name, amount, date_closed, sales_stage, assigned_user_name, account_name |
| `required_fields` | `name`, `date_closed`, `sales_stage`, `amount` |

## Points d'attention

- Vestige pre-Vardefs. Avec `new_schema = true`, les vardefs font autorite.
