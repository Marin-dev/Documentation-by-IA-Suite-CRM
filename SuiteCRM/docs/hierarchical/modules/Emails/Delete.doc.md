# Fichier : Delete.php

**Chemin :** `modules/Emails/Delete.php`
**Type :** PHP — Script d'action (suppression)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Supprime logiquement un enregistrement Email (soft delete) et redirige vers la liste appropriee selon le type d'email (archive vs autre).

## Role technique

Script procedural. Recupere le bean, verifie l'ACL, appelle `mark_deleted()`, puis redirige.

---

## Dependances

- **Utilise :** `BeanFactory::newBean('Emails')`, `ACLController::displayNoAccess()`

## Exports / Symboles principaux

- Aucun — script de traitement uniquement

## Relations cles

- **Appele par :** URL `index.php?module=Emails&action=Delete&record={id}`
- **Position :** action de suppression standard Sugar

---

## Points d'attention

- Si le type est 'archived', la redirection renvoie vers le module Emails sans parametre supplementaire.
- Si `record` n'est pas fourni dans la requete, le script plante avec `sugar_die()`.
