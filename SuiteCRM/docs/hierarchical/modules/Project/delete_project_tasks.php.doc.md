# Fichier : delete_project_tasks.php

**Chemin :** `modules/Project/delete_project_tasks.php`
**Type :** PHP - Logic Hook (after_delete)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Logic hook `after_delete` sur le module Project. Supprime logiquement toutes les taches (`ProjectTask`) liees a un projet lorsque ce projet est supprime. Assure la coherence referentielle entre projets et taches.

## Role technique

Classe `delete_project_tasks` avec methode `delete_tasks()`. Recupere toutes les `ProjectTask` du projet via `get_full_list()`, puis execute un UPDATE SQL direct (`project_task.deleted = 1`) pour chaque tache. Utilise `DBManagerFactory` pour les requetes directes.

---

## Dependances principales

| Import / Classe | Role |
| --- | --- |
| `BeanFactory::getBean('ProjectTask')` | Chargement de la liste des taches |
| `DBManagerFactory` | Execution des UPDATE de suppression logique |

---

## Exports / Symboles principaux

| Symbole | Type | Role |
| --- | --- | --- |
| `delete_project_tasks` | Classe | Logic hook de suppression en cascade |
| `delete_project_tasks::delete_tasks()` | Methode | Marque toutes les taches du projet comme supprimees |

---

## Relations cles

- **Appele par :** Framework logic hooks SuiteCRM (after_delete sur Project)
- **Appelle :** `ProjectTask::get_full_list()`, `DBManagerFactory::query()`
- **Position dans le flux :** Post-suppression d'un projet, avant la redirection

---

## Points d'attention

- Utilise un UPDATE SQL direct plutot que `$task->mark_deleted()` — les logic hooks `after_delete` des taches ne sont pas declenches.
- Si une tache a des taches dependantes dans d'autres projets, leurs dates ne sont pas mises a jour (pas d'appel a `updateDependencies`).
- L'ordre de tri `order_number` dans `get_full_list()` est cosmétique — n'impacte pas la suppression.
