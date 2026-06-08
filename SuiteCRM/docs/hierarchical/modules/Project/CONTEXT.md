# 📁 Project

**Chemin :** `modules/Project/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module Project gère les projets dans SuiteCRM. Un projet représente un ensemble de tâches coordonnées avec des ressources (utilisateurs, contacts), des dates et des dépendances. Supporte la création depuis un template (`AM_ProjectTemplates`) avec calcul automatique des dates en heures ouvrables. Vue principale : diagramme de Gantt.

## ⚙️ Responsabilité technique
Bean `Project` (hérite de `SugarBean`). `save()` fortement surchargée pour synchroniser les ressources et créer les `ProjectTask` depuis un template. Utilise `AOBH_BusinessHours` pour les calculs de dates. Contient `echo $sql` laissé en production (dette technique).

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `views/` | Vue Gantt du projet | [→ CONTEXT](views/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `Project.php` | Bean principal du projet | [→ fiche](Project.php.doc.md) |
| `Save.php` | Action de sauvegarde | [→ fiche](Save.php.doc.md) |
| `controller.php` | Contrôleur MVC (vue Gantt, création depuis template) | [→ fiche](controller.php.doc.md) |
| `gantt.php` | Classe de rendu du diagramme Gantt | [→ fiche](gantt.php.doc.md) |
| `Delete.php` | Suppression d'un projet | [→ fiche](Delete.php.doc.md) |
| `delete_project_tasks.php` | Suppression des tâches d'un projet | [→ fiche](delete_project_tasks.php.doc.md) |
| `project_table.php` | Rendu HTML du tableau de tâches | [→ fiche](project_table.php.doc.md) |
| `ProjectJjwg_MapsLogicHook.php` | Hook de géolocalisation | [→ fiche](ProjectJjwg_MapsLogicHook.php.doc.md) |
| `vardefs.php` | Schéma de la table `project` | [→ fiche](vardefs.php.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `AM_ProjectTemplates`, `ProjectTask`, `AOBH_BusinessHours`, `BeanFactory`
- **Consommé par :** `AM_ProjectTemplatesController` (création depuis template), Contacts (relations)
- **Flux typique :** Création projet avec template → `Project::save()` → `AOBH_BusinessHours` calcule dates → création `ProjectTask`

---

## ⚠️ Zones INCONNU
- `echo $sql` aux lignes 409 et 430 : sortie HTML non voulue en production
- Méthodes de calcul d'effort total commentées — totaux non calculés
