# Fichier : Projects.php

**Chemin :** `install/suite_install/Projects.php`
**Type :** installer (configuration module Projects)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Configure les logic hooks du module Projects lors de l'installation : suppression en cascade des taches de projet, et hooks de synchronisation des taches projet.

## Role technique
Fonction `install_projects()` qui enregistre des hooks via `check_logic_hook_file()` sur les modules Project et ProjectTask.

---

## Dependances cles
- **Imports principaux :**
  - `ModuleInstall/ModuleInstaller.php`

## Exports / Symboles principaux
| Symbole | Role |
|---|---|
| `install_projects()` | Enregistre les hooks du module Projects |

**Hooks configures :**
- `Project before_delete` order 1 → `delete_project_tasks::delete_tasks`
- `ProjectTask before_save` → INCONNU (lignes non lues)

## Interactions
- **Appele par :** `install/suite_install/suite_install.php` (ligne 43)
- **Appelle :**
  - `check_logic_hook_file()` — enregistrement hooks
  - `modules/Project/delete_project_tasks.php`

---

## Notes
- La suppression en cascade des taches lors de la suppression du projet est geree via hook (pas en DB foreign key).
