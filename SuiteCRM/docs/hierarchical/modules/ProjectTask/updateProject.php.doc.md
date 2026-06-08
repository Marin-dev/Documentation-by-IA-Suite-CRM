# Fichier : updateProject.php

**Chemin :** `modules/ProjectTask/updateProject.php`
**Type :** PHP - Logic Hook (after_save)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Logic hook `after_save` sur le module ProjectTask. Etend automatiquement la date de fin du projet parent lorsque la date de fin d'une tache depasse la date de fin du projet. Maintient ainsi la coherence temporelle entre les taches et leur projet.

## Role technique

Classe `updateEndDate` avec une methode `update()`. Charge les beans Project lies via `get_linked_beans('projects')`. Si `bean->date_finish` > `project->estimated_end_date`, met a jour `estimated_end_date` du projet et le sauvegarde. Utilise `$timedate->fromDbDate()` pour la comparaison.

---

## Dependances principales

| Import / Classe | Role |
|---|---|
| `SugarBean` / `$bean` | Bean ProjectTask transmis par le framework hooks |
| `TimeDate` (`$timedate` global) | Conversion et comparaison des dates |
| `Project` (via `get_linked_beans`) | Projet parent dont la date est mise a jour |

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `updateEndDate` | Classe | Logic hook de mise a jour de la date de fin projet |
| `updateEndDate::update()` | Methode | Etend `estimated_end_date` du projet si necessaire |

---

## Relations cles

- **Appele par :** Framework logic hooks SuiteCRM (after_save sur ProjectTask), declaration dans `logic_hooks.php` de ProjectTask
- **Appelle :** `Project::save()` si date depasse
- **Position dans le flux :** Post-sauvegarde de toute ProjectTask ayant un projet lie

---

## Points d'attention

- Peut declencher une sauvegarde en cascade du projet a chaque save de tache — impact performance sur les gros projets.
- Le flag `$project_task->set_project_end_date = 0` dans `Project::save()` (ligne 589) est utilise pour desactiver ce hook lors de la creation initiale des taches depuis un template.
- La comparaison de dates utilise `fromDbDate()` — s'assurer que les dates sont bien au format DB (Y-m-d).
