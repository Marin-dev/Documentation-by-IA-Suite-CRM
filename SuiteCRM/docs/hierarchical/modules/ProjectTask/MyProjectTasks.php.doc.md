# Fichier : MyProjectTasks.php

**Chemin :** `modules/ProjectTask/MyProjectTasks.php`
**Type :** PHP - Vue (liste "Mes Taches Projet")
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Affiche la liste des taches projet assignees a l'utilisateur courant dont la date de debut est aujourd'hui ou dans le passe. Equivalent de `Tasks/MyTasks.php` pour le module ProjectTask.

## Role technique

Script PHP de rendu direct. Calcule `$today` en format DB, filtre sur `assigned_user_id = current_user.id` et `date_start <= today`. Utilise `ListView` pour le rendu.

---

## Dependances principales

| Import / Classe | Role |
| --- | --- |
| `ListView` | Composant de rendu de liste SuiteCRM |
| `$timedate` (global) | Calcul de la date du jour en format DB |
| `$current_user` (global) | Filtrage par utilisateur courant |

---

## Exports / Symboles principaux

Aucun. Script de rendu direct.

---

## Relations cles

- **Appele par :** INCONNU (probablement `index.php?module=ProjectTask&action=MyProjectTasks`)
- **Appelle :** `ListView` avec filtre SQL

---

## Points d'attention

- Structure similaire a `Tasks/MyTasks.php` — duplication de logique.
