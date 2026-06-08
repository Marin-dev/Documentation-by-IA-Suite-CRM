# Fichier : field_arrays.php

**Chemin :** `modules/Meetings/field_arrays.php`
**Type :** config (tableaux de champs)
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure
Declare le tableau global `$fields_array['Meeting']` avec trois sous-tableaux utilises par le framework SuiteCRM pour le cache et les requetes SQL : `column_fields` (colonnes a charger), `list_fields` (colonnes de la vue liste), `required_fields` (champs obligatoires avec ordre de validation).

## Parametres cles
| Parametre | Valeur | Effet |
|---|---|---|
| `column_fields` | liste de 19 colonnes | champs charges depuis la DB pour un bean Meeting |
| `list_fields` | liste de 21 champs | champs affiches/disponibles en vue liste |
| `required_fields` | `name, date_start, time_start, duration_hours` | validation obligatoire cote serveur |

---

## Points d'attention
- `name` dans `list_fields` contient une tabulation parasite (`'name\t'`) — potentielle anomalie.
