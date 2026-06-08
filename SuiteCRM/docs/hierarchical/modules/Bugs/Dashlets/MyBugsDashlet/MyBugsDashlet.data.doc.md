# MyBugsDashlet.data.php

**Chemin :** `modules/Bugs/Dashlets/MyBugsDashlet/MyBugsDashlet.data.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Fichier de donnees declaratives pour le dashlet MyBugsDashlet. Definit les champs de recherche et les colonnes de la vue liste du dashlet.

## Type
config / data

## Dependances cles
- `$current_user` (global) — valeur par defaut du filtre `assigned_user_id`

## Exports / Symboles principaux
- `$dashletData['MyBugsDashlet']['searchFields']` — filtres : date_entered, priority, status (defaut : Assigned/New/Pending), type, name, assigned_user_id
- `$dashletData['MyBugsDashlet']['columns']` — colonnes : bug_number, name, priority, status, resolution, release_name, type, fixed_in_release_name, source, date_entered, date_modified, created_by, assigned_user_name

## Interactions
- **Appele par :** `MyBugsDashlet.php` (require dans le constructeur)

## Notes
- Fichier purement declaratif.
