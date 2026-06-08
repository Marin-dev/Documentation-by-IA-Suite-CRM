# Fichier : vardefs.php (configuration)

**Chemin :** `modules/ProjectTask/vardefs.php`
**Configure :** Schema du bean `ProjectTask` / table SQL `project_task`
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure

Definition complete du schema `$dictionary['ProjectTask']` pour la table `project_task`. Declare tous les champs, relations, index et l'activation de l'audit. Sert de source de verite pour l'ORM, les vues et le diagramme de Gantt.

---

## Parametres cles

| Parametre | Valeur / Type | Effet |
| --- | --- | --- |
| `table` | `project_task` | Table SQL principale |
| `audited` | `true` | Audit des modifications actif |
| `unified_search` | `true` | Inclus dans la recherche globale |
| `project_id` | id, required, importable:required | FK vers `project` |
| `project_task_id` | int | Numero de tache interne au projet (ordre) |
| `name` | varchar(50), required | Nom de la tache |
| `status` | enum `project_task_status_options` | Statut de la tache |
| `date_start` / `date_finish` | date | Plage temporelle, validation `isbefore/isafter` |
| `duration` | int, required | Duree de la tache |
| `duration_unit` | enum `project_duration_units_dom` | Unite de duree (Days/Hours) |
| `percent_complete` | int | Pourcentage d'avancement (calcule pour les parents) |
| `predecessors` | text | IDs des taches predecesseurs (chaine) |
| `relationship_type` | enum `relationship_type_list` | Type de dependance (FS, SS, FF, SF) |
| `parent_task_id` | int | ID de la tache parente (hierarchie) |
| `milestone_flag` | bool | Indique si la tache est un jalon |
| `utilization` | int | Taux d'utilisation de la ressource (0-100%) |
| `estimated_effort` | int | Effort estime en heures |
| `actual_effort` | int | Effort reel en heures |

---

## Relations declarees

| Relation | Type | Description |
| --- | --- | --- |
| `projects` (link via `project_id`) | many-to-many | Projets auxquels la tache appartient |
| `assigned_user` | relate | Utilisateur responsable de la tache |

---

## Impacte par / impacte

- Lu par `ProjectTask::updateStatistic()` pour le calcul du % avancement
- Lu par `gantt.php` et `project_table.php` pour le rendu Gantt
- Lu par `updateDependencies.php` pour la propagation des dependances

---

## Points d'attention

- `predecessors` est de type `text` (pas un FK) — les dependances sont des chaines d'IDs, parsing applicatif.
- `time_start` et `time_finish` sont de type `int` et non reportables — champs internes Gantt.
- `date_due` et `time_due` existent en parallele de `date_finish` — heritage de l'arborescence SugarBean, potentiellement source de confusion.
