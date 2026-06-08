# Fichier : field_arrays.php

**Chemin :** `modules/Schedulers/field_arrays.php`
**Type :** PHP — configuration (tableau de champs)
**Derniere mise a jour doc :** 2026-06-02

---

## Ce que ce fichier configure
Declare les tableaux de champs pour les modules `Scheduler` et `Job` : champs de colonne DB, champs de liste, et champs obligatoires. Utilise par le framework SugarCRM pour les formulaires et vues legacy.

## Parametres cles
| Parametre | Valeur notable | Effet |
|---|---|---|
| `$fields_array['Scheduler']['column_fields']` | id, name, job, job_interval, status, catch_up, ... | Champs persistes en DB |
| `$fields_array['Scheduler']['required_fields']` | name, list_order, status | Validation cote serveur |
| `$fields_array['Job']['column_fields']` | id, job_id, execute_time, status | Champs de la file de jobs |

## Impacte par / impacte
- Consomme par le framework SugarCRM (vues legacy, formulaires)
- Lie a `modules/Schedulers/vardefs.php` pour la definition complete

## Points d'attention
- `list_order` est dans `required_fields` mais pas dans `column_fields` — potentiel inconsistance (champ virtuel ou absent de la table ?).
