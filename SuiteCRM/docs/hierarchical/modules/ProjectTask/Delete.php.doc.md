# Fichier : Delete.php

**Chemin :** `modules/ProjectTask/Delete.php`
**Type :** PHP - Controleur (point d'entree action)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Point d'entree de l'action `Delete` du module ProjectTask. Supprime logiquement une tache projet apres verification ACL, puis redirige.

## Role technique

Script PHP identique dans sa structure a `Project/Delete.php`. Recupere le bean `ProjectTask`, verifie `ACLAccess('Delete')`, appelle `mark_deleted()`, redirige.

---

## Exports / Symboles principaux

Aucun symbole exporte. Script d'execution directe.

---

## Relations cles

- **Appele par :** Routeur SuiteCRM (`index.php?module=ProjectTask&action=Delete&record=...`)
- **Appelle :** `ProjectTask::mark_deleted()`, `ACLController::displayNoAccess()`

---

## Points d'attention

- La suppression d'une tache peut laisser des taches dependantes avec des predecesseurs invalides — pas de nettoyage automatique visible.
