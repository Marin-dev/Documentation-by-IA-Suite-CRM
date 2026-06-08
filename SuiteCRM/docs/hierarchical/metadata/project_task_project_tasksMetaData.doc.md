# project_task_project_tasksMetaData.php

**Chemin :** `metadata/project_task_project_tasksMetaData.php`
**Type :** config (métadonnées de table de dépendances entre tâches projet)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table `project_task_project_tasks` qui matérialise les relations de dépendance entre les tâches d'un projet. Permet de modéliser les précédences entre tâches (Gantt).

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['project_task_project_tasks']` | variable globale PHP | Définition de la table de dépendances tâches |

### Structure de la table `project_task_project_tasks`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | id | Clé primaire UUID (requis) |
| `project_task_id` | id | FK vers la tâche courante (requis) |
| `predecessor_project_task_id` | id | FK vers la tâche prédécesseur (requis) |
| `deleted` | bool | Soft delete (défaut : 0) |

### Relation

- **Type :** many-to-many auto-référentielle
- **LHS et RHS :** module `ProjectTasks2`, table `project_tasks`
- La jointure `(project_task_id → predecessor_project_task_id)` exprime "cette tâche dépend de cette autre tâche"

## Notes

- Relation auto-référentielle sur `project_tasks` : une tâche peut avoir plusieurs prédécesseurs et plusieurs successeurs.
- Module référencé : `ProjectTasks2` (alias pour `project_tasks`) — INCONNU si ce module existe indépendamment du module `ProjectTask`.
- Pas de champ `date_modified`.
