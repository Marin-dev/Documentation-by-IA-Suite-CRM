# Fichier : Project.php

**Chemin :** `modules/Project/Project.php`
**Type :** PHP - Modele (Model)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Classe metier centrale du module Project. Represente un projet avec ses dates, ressources (utilisateurs et contacts), et taches associees. Permet la creation d'un projet a partir d'un modele de projet (`AM_ProjectTemplates`), la duplication, et la gestion des ressources affectees. Le projet peut etre marque comme "template" pour etre reutilise.

## Role technique

Herite de `SugarBean`. La methode `save()` est fortement surchargee pour : synchroniser les ressources (users/contacts invitees via POST), detecter un changement de modele de projet, et si un nouveau modele est selectionne, creer automatiquement les `ProjectTask` en calculant les dates de debut/fin en fonction des heures ouvrables (`AOBH_BusinessHours`). Fournit des methodes utilitaires de calcul d'effort total (commentees en production).

---

## Dependances principales

| Import / Classe | Role |
|---|---|
| `SugarBean` | Classe de base ORM SuiteCRM |
| `BeanFactory` | Instanciation de `ProjectTask`, `AM_ProjectTemplates`, `AOBH_BusinessHours` |
| `DBManagerFactory` | Acces direct SQL (gestion ressources, taches template) |
| `AM_ProjectTemplates` | Lecture du modele de projet selectionne |
| `AOBH_BusinessHours` | Calcul des heures ouvrables pour dates des taches |
| `DateTime` | Calcul des dates de debut/fin des taches template |

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `Project` | Classe | Modele metier du projet |
| `Project::save()` | Methode | Sauvegarde avec gestion ressources et creation de taches depuis template |
| `Project::getAllProjectTasks()` | Methode | Retourne toutes les ProjectTask liees au projet (non supprimees) |
| `Project::_get_total_estimated_effort()` | Methode | Somme des `estimated_effort` des taches (non appelee en prod) |
| `Project::_get_total_actual_effort()` | Methode | Somme des `actual_effort` des taches (non appelee en prod) |
| `Project::save_relationship_changes()` | Methode | Gere les relations dynamiques, notamment contacts->accounts |
| `Project::getDefaultStatus()` | Methode | Retourne le statut par defaut depuis les field_defs |

**Tables DB :** `project`, `project_users_1_c`, `project_contacts_1_c`, `am_tasktemplates_am_projecttemplates_c`

---

## Relations cles

- **Appele par :** `modules/Project/Save.php`, `ProjectController`, vues GanttChart/detail/edit
- **Appelle :** `BeanFactory::newBean('ProjectTask')`, `BeanFactory::newBean('AM_ProjectTemplates')`, `AOBH_BusinessHours`
- **Position dans le flux :** Entite racine du sous-systeme projet ; `ProjectTask` en est la feuille

---

## Points d'attention

- La methode `save()` contient un `echo $sql;` (lignes 409 et 430) laisse en production lors de la suppression de ressources — sortie HTML non souhaitee.
- Le calcul des dates des taches depuis un template (lignes 495-648) n'est declenche que si `$current_template_id != $new_template_id` — pas de mise a jour si le modele reste le meme.
- Les methodes `_get_total_estimated_effort()` et `_get_total_actual_effort()` existent mais sont commentees dans `fill_in_additional_detail_fields()` et `fill_in_additional_list_fields()` — les totaux ne sont pas calcules.
- La relation `am_projecttemplates_project_1` doit etre chargee avant `save()` pour detecter le changement de template (ligne 342).
- `is_template` permet de convertir un projet en template et vice-versa via `Save.php` (parametre `save_type`).
