# Fichier : field_arrays.php

**Chemin :** `modules/Users/field_arrays.php`
**Type :** PHP — Configuration (tableaux de champs)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Declare les listes de champs utilisees par le module Users pour les differentes operations : colonnes de base de donnees, champs de liste, champs d'export, et champs obligatoires. Egalement declare les champs pour `UserSignature`.

## Role technique

Fichier de configuration peuplant `$fields_array['User']` et `$fields_array['UserSignature']`. Utilise par le framework SugarCRM pour le cache de champs et les operations de liste/export.

---

## Exports / Symboles principaux

| Variable | Cles | Role |
|---|---|---|
| `$fields_array['User']['column_fields']` | liste | Champs selectionnes en base |
| `$fields_array['User']['list_fields']` | liste | Champs affiches en vue liste |
| `$fields_array['User']['export_fields']` | liste | Champs exportes |
| `$fields_array['User']['required_fields']` | assoc | Champs obligatoires : `last_name`, `user_name`, `status` |
| `$fields_array['UserSignature']` | — | Champs signature (id, dates, user_id, name, signature) |

---

## Relations cles

- **Appele par :** framework SugarCRM (cache de champs, import/export)
- **Complementaire de :** `vardefs.php` (schema complet)

---

## Points d'attention

- `full_name` apparait dans `column_fields` et `list_fields` mais est un champ calcule (non stocke directement) — depend de la logique du bean `Person`.
