# Fichier : Save.php

**Chemin :** `modules/Project/Save.php`
**Type :** PHP - Controleur (point d'entree action)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Point d'entree de l'action `Save` du module Project. Gere la creation, la modification, la duplication d'un projet, ainsi que la conversion projet <-> template. Sauvegarde egalement les `ProjectTask` associees lors d'une duplication ou d'une conversion.

## Role technique

Script PHP de ~140 lignes. Utilise `BeanFactory::newBean('Project')` et `populateFromPost()`. Selon le parametre `save_type` (TemplateToProject / ProjectToTemplate) ou `duplicateSave`, il clone les `ProjectTask` existantes vers le nouveau projet. Apres sauvegarde, redirige vers la vue GanttChart ou la vue detail du template selon `is_template`.

---

## Dependances principales

| Import / Fichier | Role |
|---|---|
| `include/formbase.php` | `populateFromPost()`, `handleRedirect()` |
| `BeanFactory` | Instanciation de `Project` et `ProjectTask` |
| `ACLController` | Verification des droits de sauvegarde |

---

## Exports / Symboles principaux

Aucun symbole exporte. Script d'execution directe.

**Parametres POST/REQUEST cles :**

| Parametre | Valeur | Effet |
|---|---|---|
| `save_type` | `TemplateToProject` | Convertit template -> projet, renomme avec `project_name` |
| `save_type` | `ProjectToTemplate` | Convertit projet -> template, renomme avec `template_name` |
| `duplicateSave` | `true` | Duplique le projet avec ses taches |
| `is_template` | `1` | Marque comme template |
| `user_invitees` | CSV d'IDs | Liste des utilisateurs ressources |
| `contact_invitees` | CSV d'IDs | Liste des contacts ressources |

---

## Relations cles

- **Appele par :** routeur SuiteCRM (`index.php?module=Project&action=Save`)
- **Appelle :** `Project::save()`, `ProjectTask::save()`, `handleRedirect()`
- **Position dans le flux :** Apres soumission du formulaire projet ou GanttChart

---

## Points d'attention

- Si `is_template`, la redirection va vers `ProjectTemplatesDetailView` (ligne 134), sinon vers `view_GanttChart` (ligne 137).
- Les taches dupliquees ont leurs `date_entered` et `date_modified` remises a blanc (ligne 72-73) pour etre regenerees.
- Si `is_template` est vrai et que c'est une duplication, `assigned_user_id` des taches est efface (ligne 122) — les taches du template n'ont pas de responsable.
