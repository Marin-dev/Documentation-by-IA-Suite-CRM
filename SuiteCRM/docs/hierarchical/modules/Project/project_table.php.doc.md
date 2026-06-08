# Fichier : project_table.php

**Chemin :** `modules/Project/project_table.php`
**Type :** PHP - Helper de rendu (View Helper)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Genere le tableau HTML des taches projet affiché a gauche du diagramme de Gantt. Affiche colonnes : ID tache, nom, predecesseurs, date debut, date fin, duree, responsable, pourcentage avancement.

## Role technique

Classe `ProjectTable` avec constructeur appelant `draw()`. Rendu HTML direct par echo. Utilise `TimeDate` pour le formatage des dates. Affiche chaque tache avec ses champs cles et gere le formatage de la duree (jours ou heures).

---

## Dependances principales

| Import / Classe | Role |
| --- | --- |
| `TimeDate` | Formatage des dates en affichage utilisateur |
| `$mod_strings` (global) | Labels traduits des colonnes |
| `$app_list_strings` (global) | Listes de valeurs (statut, priorite, etc.) |

---

## Exports / Symboles principaux

| Symbole | Type | Role |
| --- | --- | --- |
| `ProjectTable` | Classe | Rendu du tableau gauche du Gantt |
| `ProjectTable::draw()` | Methode | Genere le HTML du tableau |

---

## Relations cles

- **Appele par :** `ProjectController::action_generate_chart()` via `include_once`
- **Position dans le flux :** Rendu en parallele de `Gantt` dans la vue GanttChart

---

## Points d'attention

- Rendu par echo direct — pas de separation template/logique.
- La duree est affichee en "Days" ou "Hours" selon `duration_unit` — mais le libelle est en anglais.
