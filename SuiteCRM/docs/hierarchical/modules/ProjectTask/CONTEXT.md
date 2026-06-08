# 📁 ProjectTask

**Chemin :** `modules/ProjectTask/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module ProjectTask gère les tâches individuelles d'un projet. Chaque tâche représente une activité avec durée, ressource assignée, prédécesseurs et dépendances. Les tâches sont visualisées dans le diagramme de Gantt du projet.

## ⚙️ Responsabilité technique
Bean `ProjectTask` (hérite de `SugarBean`). Table `project_task`. Gestion des dépendances via `updateDependencies.php`. Mise à jour du projet parent via `updateProject.php`.

---

## 📂 Contenu

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `ProjectTask.php` | Bean principal des tâches de projet | [→ fiche](ProjectTask.php.doc.md) |
| `Save.php` | Sauvegarde d'une tâche | [→ fiche](Save.php.doc.md) |
| `Delete.php` | Suppression d'une tâche | [→ fiche](Delete.php.doc.md) |
| `updateProject.php` | Mise à jour du projet parent | [→ fiche](updateProject.php.doc.md) |
| `updateDependencies.php` | Mise à jour des dépendances entre tâches | [→ fiche](updateDependencies.php.doc.md) |
| `MyProjectTasks.php` | Mes tâches de projet | [→ fiche](MyProjectTasks.php.doc.md) |
| `ProjectTaskQuickCreate.php` | Création rapide de tâche | [→ fiche](ProjectTaskQuickCreate.php.doc.md) |
| `vardefs.php` | Schéma de la table `project_task` | [→ fiche](vardefs.php.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `Project` (projet parent), `SugarBean`
- **Consommé par :** `Project::save()` (création des tâches depuis template), diagramme Gantt
- **Flux typique :** Tâche créée/modifiée → `updateProject.php` met à jour les dates du projet → `updateDependencies.php` recalcule les dépendances

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
