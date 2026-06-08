# Fichier : controller.php

**Chemin :** `modules/AM_ProjectTemplates/controller.php`
**Type :** PHP - Controleur MVC
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Controleur MVC du module AM_ProjectTemplates. Gere l'affichage de la vue GanttChart du template et la creation d'un nouveau projet a partir d'un template avec selection optionnelle des taches a copier.

## Role technique

Classe `AM_ProjectTemplatesController` heritant de `SugarController`. Action `action_view_GanttChart()` route vers la vue GanttChart. Action `action_create_project()` lit les parametres POST (nom du projet, template_id, date de debut, selection de taches), instancie un `Project` bean, copie les taches template selectionnees en `ProjectTask` avec calcul des dates selon les heures ouvrables, sauvegarde le projet et redirige.

---

## Dependances principales

| Import / Classe | Role |
| --- | --- |
| `SugarController` | Classe de base MVC |
| `BeanFactory` | Instanciation de `Project`, `AM_ProjectTemplates`, `AOBH_BusinessHours` |
| `DateTime` (PHP natif) | Calcul des dates de taches |
| `DBManagerFactory` | Requetes SQL |

---

## Exports / Symboles principaux

| Symbole | Type | Role |
| --- | --- | --- |
| `AM_ProjectTemplatesController` | Classe | Controleur module AM_ProjectTemplates |
| `action_view_GanttChart()` | Methode | Route vers vue Gantt du template |
| `action_create_project()` | Methode | Cree un projet depuis le template avec selection de taches |

---

## Relations cles

- **Appele par :** Routeur SuiteCRM (`index.php?module=AM_ProjectTemplates&action=view_GanttChart` ou `action=create_project`)
- **Appelle :** `BeanFactory::newBean('Project')`, `BeanFactory::newBean('ProjectTask')`, `AOBH_BusinessHours`
- **Position dans le flux :** Alternative a `Project::save()` pour creer un projet depuis un template avec selection de taches

---

## Points d'attention

- La logique de calcul des dates est dupliquee entre ce controleur et `Project::save()` — risque de divergence.
- `action_create_project()` permet de selectionner individuellement les taches a copier (`copy_tasks`) ou de tout copier (`copy_all = 1`).
- Utilise `$_POST` directement sans validation systematique — attention aux entrees non sanitizees.
