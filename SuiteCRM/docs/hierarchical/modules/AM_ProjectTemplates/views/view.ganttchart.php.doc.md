# Fichier : view.ganttchart.php

**Chemin :** `modules/AM_ProjectTemplates/views/view.ganttchart.php`
**Type :** PHP - Vue (Gantt Chart template)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Vue principale d'affichage du diagramme de Gantt d'un modele de projet. Equivalent de `Project/views/view.ganttchart.php` pour les templates. Permet la gestion visuelle des taches modeles avec leurs dependances.

## Role technique

Classe `AM_ProjectTemplatesViewGanttChart` heritant de `ViewDetail`. Charge le bean `AM_ProjectTemplates`, recupere les ressources (users/contacts), injecte les assets CSS/JS specifiques au module (`modules/AM_ProjectTemplates/css/`, `js/`) et les donnees JSON pour le JS cote client.

---

## Dependances principales

| Import / Classe | Role |
| --- | --- |
| `ViewDetail` | Classe parente vue detail |
| `BeanFactory` | Chargement du bean `AM_ProjectTemplates` |
| `DBManagerFactory` | Requetes SQL taches template |

---

## Exports / Symboles principaux

| Symbole | Type | Role |
| --- | --- | --- |
| `AM_ProjectTemplatesViewGanttChart` | Classe | Vue Gantt du template de projet |
| `display()` | Methode | Rendu HTML + injection JSON ressources |

---

## Relations cles

- **Appele par :** `AM_ProjectTemplatesController::action_view_GanttChart()`
- **Appelle :** `AM_ProjectTemplates::get_linked_beans()` pour users et contacts
- **Position dans le flux :** Vue principale du module AM_ProjectTemplates

---

## Points d'attention

- Les assets JS/CSS sont separes de ceux du module Project — `modules/AM_ProjectTemplates/js/main_lib.js` vs `modules/Project/js/main_lib.js`.
- Structure quasi-identique a `ProjectViewGanttChart` — code duplique.
