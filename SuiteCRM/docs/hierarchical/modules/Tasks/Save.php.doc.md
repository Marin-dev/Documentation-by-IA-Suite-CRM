# Fichier : Save.php

**Chemin :** `modules/Tasks/Save.php`
**Type :** controller (point d'entree action)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Traite la soumission du formulaire de sauvegarde d'une tache. Gere les cas : fermeture de tache ("Close And Create New"), dates vides, email entrant (inbound email) et conflit relate_id/parent_id.

## Role technique
Script PHP (~160 lignes). Utilise `populateFromPost()` et `$focus->save()`. Gestion speciale si `inbound_email_id` : sauvegarde la tache, attache l'email et redirige vers EditView Emails. Gere le flag `isCloseAndCreateNewPressed()` pour passer le statut a `Completed`.

---

## Dependances cles
- `include/formbase.php` — `populateFromPost()`, `handleRedirect()`
- `BeanFactory::newBean('Tasks')`, `BeanFactory::newBean('Emails')`
- `ACLController`
- `TimeDate` — formatage dates

## Exports / Symboles principaux
Aucun. Script d'execution directe.

---

## Relations cles
- **Appele par :** routeur SuiteCRM (`module=Tasks&action=Save`)
- **Appelle :** `Task::save()`, `Email::save()`, `handleRedirect()`

---

## Points d'attention
- Si `relate_id != parent_id`, `relate_id` est ignore pour eviter d'ecraser la relation parent (bugs 41103 et 43751).
- Les dates `date_due` et `date_start` sont ignorees si leur longueur < 8 (date sans valeur complete).
