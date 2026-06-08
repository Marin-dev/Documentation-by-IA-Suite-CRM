# Fichier : gantt.php

**Chemin :** `modules/Project/gantt.php`
**Type :** PHP - Helper de rendu (View Helper)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Classe de rendu graphique du diagramme de Gantt pour un projet. Prend en entree les dates de debut/fin du projet et la liste des taches, et genere le HTML/SVG du diagramme affichant les barres de taches avec leur progression.

## Role technique

Classe `Gantt` avec un constructeur qui appelle directement `draw()`. La methode `draw()` calcule la grille temporelle (jours/semaines) et positionne les barres de taches proportionnellement a leur duree et dates. Rendu HTML direct (echo). Appelee depuis `ProjectController::action_generate_chart()`.

---

## Dependances principales

| Import / Classe | Role |
|---|---|
| `ProjectController` | Appelant (via `include_once`) |
| `project_table.php` | Inclus en parallele pour le tableau des taches |

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `Gantt` | Classe | Moteur de rendu du diagramme de Gantt |
| `Gantt::__construct()` | Methode | Initialise et declenche le rendu |
| `Gantt::draw()` | Methode | Genere le HTML du diagramme |

---

## Relations cles

- **Appele par :** `modules/Project/controller.php::action_generate_chart()` via `include_once`
- **Appelle :** Rendu HTML direct (echo)
- **Position dans le flux :** Rendu final de la vue GanttChart

---

## Points d'attention

- Rendu HTML par echo direct — pas de separation template/logique.
- Les proprietes `$start_date`, `$end_date`, `$tasks` sont privees (ligne 49-51) — pas extensible sans modification.
