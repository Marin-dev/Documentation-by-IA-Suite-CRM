# field_arrays.php

**Chemin :** `modules/Campaigns/field_arrays.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Définit les tableaux de champs utilisés pour le cache du module Campaign : colonnes de la table, champs de liste et champs obligatoires.

## Type

`config`

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `$fields_array['Campaign']` | tableau | `column_fields`, `list_fields`, `required_fields` |

### Champs obligatoires (required_fields)

| Champ | Priorité |
|---|---|
| `name` | 1 |
| `end_date` | 2 |
| `status` | 3 |
| `campaign_type` | 4 |

---

## Interactions

- **Consommé par :** Framework ORM SuiteCRM (cache champs)

---

## Points d'attention

- RAS.
