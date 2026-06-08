# Fichier : controller.php

**Chemin :** `modules/Project/controller.php`
**Type :** PHP - Controleur MVC
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Controleur MVC du module Project. Gere les actions specifiques au module : affichage du diagramme de Gantt et generation des donnees du graphique. Centralise les redirections ACL pour les vues non standards.

## Role technique

Classe `ProjectController` heritant de `SugarController`. Deux actions principales : `action_view_GanttChart()` (route vers la vue Gantt) et `action_generate_chart()` (charge `gantt.php` et `project_table.php`, genere le HTML du diagramme). Chaque action verifie les droits d'acces via `$current_user->hasActionAccess()`.

---

## Dependances principales

| Import / Classe | Role |
|---|---|
| `SugarController` | Classe de base MVC |
| `BeanFactory` | Chargement du bean Project |
| `gantt.php` (`modules/Project/gantt.php`) | Classe Gantt de rendu graphique |
| `project_table.php` (`modules/Project/project_table.php`) | Rendu du tableau des taches |
| `DBManagerFactory` | Requetes SQL pour les taches |

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `ProjectController` | Classe | Controleur module Project |
| `action_view_GanttChart()` | Methode | Route vers la vue diagramme Gantt |
| `action_generate_chart()` | Methode | Genere et affiche le diagramme Gantt |

---

## Relations cles

- **Appele par :** Routeur SuiteCRM (`index.php?module=Project&action=view_GanttChart` ou `action=generate_chart`)
- **Appelle :** `gantt.php::Gantt`, `project_table.php`, `BeanFactory::newBean('Project')`
- **Position dans le flux :** Intermediaire entre les URLs de la vue Gantt et les classes de rendu

---

## Points d'attention

- La vue GanttChart est la vue principale post-sauvegarde d'un projet (voir `Save.php` ligne 137).
- `action_generate_chart()` inclut directement les fichiers PHP de rendu (pas d'heritage de vue) — sortie HTML directe.
