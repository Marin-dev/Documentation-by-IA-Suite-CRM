# Fichier : Delete.php

**Chemin :** `modules/Project/Delete.php`
**Type :** PHP - Controleur (point d'entree action)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Point d'entree de l'action `Delete` du module Project. Supprime logiquement un projet apres verification ACL, puis redirige vers l'emplacement de retour.

## Role technique

Script PHP de ~40 lignes utiles. Recupere le bean via `BeanFactory::newBean('Project')`, verifie `ACLAccess('Delete')`, appelle `mark_deleted()`, puis construit la redirection depuis les parametres REQUEST (`return_module`, `return_action`, `return_id`).

---

## Exports / Symboles principaux

Aucun symbole exporte. Script d'execution directe.

---

## Relations cles

- **Appele par :** Routeur SuiteCRM (`index.php?module=Project&action=Delete&record=...`)
- **Appelle :** `Project::mark_deleted()`, `ACLController::displayNoAccess()`
- **Note :** Ne supprime pas automatiquement les `ProjectTask` enfants — voir `modules/Project/delete_project_tasks.php`

---

## Points d'attention

- La suppression des taches associees n'est pas effectuee ici — elle est dans un fichier separe `delete_project_tasks.php`.
