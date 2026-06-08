# Fichier : ProjectTask.php

**Chemin :** `modules/ProjectTask/ProjectTask.php`
**Type :** PHP - Modele (Model)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Classe metier centrale du module ProjectTask. Represente une tache dans un projet, avec dates de debut/fin, duree, predecesseurs, priorite, pourcentage d'avancement et affectation utilisateur. Gere le calcul automatique du pourcentage d'avancement des taches parentes en fonction de leurs enfants.

## Role technique

Herite de `SugarBean`. La methode `save()` appelle `updateStatistic()` apres chaque sauvegarde pour recalculer le pourcentage d'avancement des taches parentes (sauf si `skipParentUpdate()` a ete appele). `updateStatistic()` construit un arbre des taches du projet, identifie les noeuds parents et recalcule leurs pourcentages. Fournit aussi `updateDependencies` (logic hook externe) pour decaler les taches dependantes.

---

## Dependances principales

| Import / Classe | Role |
|---|---|
| `SugarBean` | Classe de base ORM SuiteCRM |
| `BeanFactory` | Instanciation de beans `ProjectTask` |
| `DBManagerFactory` | Requetes SQL directes pour l'arbre des taches |
| `SecurityGroup` (`modules/SecurityGroups/`) | Controle d'acces par groupe |
| `ACLController` | Controle ACL par module/vue |

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `ProjectTask` | Classe | Modele metier de la tache projet |
| `ProjectTask::save()` | Methode | Sauvegarde + mise a jour statistiques parentes |
| `ProjectTask::updateStatistic()` | Methode | Recalcule le % avancement de toutes les taches parentes du projet |
| `ProjectTask::updateParentProjectTaskPercentage()` | Methode | Recalcule uniquement le parent direct |
| `ProjectTask::getAllSubProjectTasks()` | Methode | Retourne toutes les taches filles (recursif) |
| `ProjectTask::getProjectTaskParent()` | Methode | Retourne la tache parente directe |
| `ProjectTask::skipParentUpdate()` | Methode | Desactive la mise a jour statistique (evite les boucles) |
| `ProjectTask::_calculateCompletePercent()` | Methode (privee) | Calcul pondere du % selon les durees (heures vs jours) |
| `getUtilizationDropdown()` | Fonction globale | Genere le select HTML pour le taux d'utilisation en EditView |

**Tables DB :** `project_task`

---

## Relations cles

- **Appele par :** `Project::save()`, `modules/ProjectTask/Save.php`, `updateProject.php` (logic hook), `updateDependencies.php` (logic hook)
- **Appelle :** `BeanFactory::getBean('ProjectTask')`, `DBManagerFactory::getInstance()`
- **Position dans le flux :** Feuille du sous-systeme projet, agregee par `Project`

---

## Points d'attention

- `updateStatistic()` charge TOUTES les taches du projet a chaque sauvegarde (ligne 517) — peut etre lent sur les gros projets.
- `skipParentUpdate()` doit imperativement etre appele lors de la sauvegarde en masse pour eviter les cascades infinies (ligne 588).
- `_calculateCompletePercent()` convertit les jours en heures (x8) — suppose des journees de 8h, non configurable.
- `getNumberOfTasksInProject()` est appelee uniquement dans les workflows (`in_workflow`) pour attribuer un `project_task_id` auto (ligne 124).
- La relation `predecessors` stocke un ID de tache sous forme de chaine ; la logique de dependance est dans `updateDependencies.php`.
