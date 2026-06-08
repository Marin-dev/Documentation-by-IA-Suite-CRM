# Fichier : view.ganttchart.php

**Chemin :** `modules/Project/views/view.ganttchart.php`
**Type :** PHP - Vue (Gantt Chart)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Vue principale d'affichage du diagramme de Gantt d'un projet. Charge le projet et ses ressources (utilisateurs et contacts), injecte les donnees JSON pour le JavaScript cote client, et affiche les assets CSS/JS du module Gantt.

## Role technique

Classe `ProjectViewGanttChart` heritant de `ViewDetail`. La methode `display()` charge le bean `Project` via `BeanFactory`, recupere les ressources via `get_linked_beans()`, construit un tableau d'objets `stdClass` pour users et contacts, et les serialise en JSON pour injection dans le template JavaScript. Injecte les CSS (`style.css`, `jquery.qtip.min.css`) et JS (`main_lib.js`, `splitter.js`, `jquery.blockUI.js`, `jquery.validate.min.js`).

---

## Dependances principales

| Import / Classe | Role |
| --- | --- |
| `ViewDetail` | Classe parente vue detail |
| `BeanFactory` | Chargement du bean `Project` |
| `DBManagerFactory` | Requetes SQL taches |
| `mod_strings` | Labels traduits |

---

## Exports / Symboles principaux

| Symbole | Type | Role |
| --- | --- | --- |
| `ProjectViewGanttChart` | Classe | Vue diagramme de Gantt |
| `display()` | Methode | Rendu HTML + injection JSON ressources |

---

## Relations cles

- **Appele par :** `ProjectController::action_view_GanttChart()`, `modules/Project/Save.php` (redirection post-save)
- **Appelle :** `Project::get_linked_beans('project_users_1')`, `Project::get_linked_beans('project_contacts_1')`
- **Position dans le flux :** Vue post-sauvegarde et vue principale de gestion des taches

---

## Points d'attention

- La vue injecte les ressources (users + contacts) en JSON directement dans le HTML — pas de separation propre vue/donnees.
- Les assets JS/CSS sont dans `modules/Project/js/` et `modules/Project/css/` — non minifies en production.
- `$_REQUEST["project_id"]` est utilise en fallback de `$_REQUEST["record"]` (ligne 43-45).
