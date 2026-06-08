# Fichier : updateDependencies.php

**Chemin :** `modules/ProjectTask/updateDependencies.php`
**Type :** PHP - Logic Hook (after_save)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Logic hook `after_save` sur ProjectTask. Lorsque la date de fin d'une tache change, recalcule et met a jour automatiquement les dates debut/fin de toutes les taches dependantes (predecesseurs). Supporte les types de dependance "Finish to Start" (FS) et "Start to Start" (SS).

## Role technique

Classe `updateDependencies` avec `update_dependency()` et `count_days()`. Recherche toutes les taches du meme projet dont `predecessors` correspond au `project_task_id` de la tache sauvegardee. Calcule le delta de jours (`count_days()`), et decale les dates des taches dependantes en fonction du type de relation (`relationship_type` : FS ou SS). Chaque tache dependante est sauvegardee via `$task->save()`.

---

## Dependances principales

| Import / Classe | Role |
|---|---|
| `BeanFactory::getBean('ProjectTask')` | Chargement des taches dependantes |
| `DateTime` (PHP natif) | Calcul et decalage des dates |

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `updateDependencies` | Classe | Logic hook de propagation des dependances de taches |
| `updateDependencies::update_dependency()` | Methode | Propagation du changement de date aux taches dependantes |
| `updateDependencies::count_days()` | Methode | Calcule le delta en jours entre deux dates, signe inclus |

---

## Relations cles

- **Appele par :** Framework logic hooks SuiteCRM (after_save sur ProjectTask)
- **Appelle :** `ProjectTask::save()` sur chaque tache dependante
- **Position dans le flux :** Post-sauvegarde d'une ProjectTask, en cascade apres `updateEndDate`

---

## Points d'attention

- Risque de cascade infinie si des taches dependantes se sauvegardent mutuellement — pas de garde contre les boucles cycliques.
- Seuls FS et SS sont geres — les types FF (Finish to Finish) et SF (Start to Finish) ne sont pas traites.
- Pour SS, la mise a jour n'est effectuee que si la duree de la tache parente n'a pas change (ligne 86) — comportement potentiellement surprenant.
- `count_days()` retourne une chaine compatible avec `DateTime::modify()` (ex: `"+3 days"` ou `"-2 days"`).
- `$bean->fetched_row` peut etre `false` (nouvelle tache) — gere a la ligne 54 avec `$fetchedDateFinish = null`.
