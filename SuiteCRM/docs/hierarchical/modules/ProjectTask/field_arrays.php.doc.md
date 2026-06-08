# Fichier : field_arrays.php (configuration)

**Chemin :** `modules/ProjectTask/field_arrays.php`
**Configure :** Tableaux de champs du bean `ProjectTask`
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure

Declare `$fields_array['ProjectTask']` avec les sous-tableaux utilises par le framework SuiteCRM pour le cache et les requetes SQL.

---

## Parametres cles

| Parametre | Valeur | Effet |
| --- | --- | --- |
| `column_fields` | 25 colonnes | Champs charges depuis la DB pour un bean ProjectTask |
| `list_fields` | 10 champs | Champs affiches en vue liste |
| `required_fields` | `name, project_id, project_task_id, duration, duration_unit` | Champs obligatoires avec ordre de validation |

---

## Points d'attention

- `project_task_id` est requis (position 3) — doit etre renseigne avant la sauvegarde (auto-calcule dans les workflows via `getNumberOfTasksInProject()`).
- `duration_unit` est requis — ne peut pas etre NULL en DB, une chaine vide `" "` est utilisee en fallback dans `Save.php`.
