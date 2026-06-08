# Fichier : field_arrays.php

**Chemin :** `modules/Leads/field_arrays.php`
**Type :** `PHP`
**Categorie :** configuration (tableau de champs cache)
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure

Definit `$fields_array['Lead']` : les tableaux de champs utilises pour le cache du module Leads. Contient `column_fields`, `list_fields` et `required_fields`.

---

## Parametres cles

| Parametre | Contenu |
| --- | --- |
| `column_fields` | Champs persistes en base (nom, prenom, adresse, telephones, status, lead_source, etc.) |
| `list_fields` | Champs affiches en vue liste : id, first_name, last_name, status, lead_source, email1, phone_work, account_name |
| `required_fields` | `last_name => 1` (seul champ requis) |

## Points d'attention

- Vestige pre-Vardefs. Avec `new_schema = true`, les vardefs font autorite.
- `last_name` est le seul champ requis, coherent avec le modele `Person`.
