# Delete.php

**Chemin :** `modules/Prospects/Delete.php`
**Type :** PHP - Script d'action (suppression)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Gère la suppression d'un enregistrement Prospect. Vérifie les droits ACL avant de supprimer, et redirige vers le module si pas de record.

## Type
helper

## Dépendances clés
- `BeanFactory::newBean('Prospects')`
- `ACLController::displayNoAccess()`
- `$_REQUEST['record']`
- `$mod_strings['ERR_DELETE_RECORD']`

## Exports / Symboles principaux
Aucune classe. Script procédural.

## Interactions
- **Appelé par :** action Delete du module Prospects
- **Appelle :** `BeanFactory::newBean()`, `ACLController::displayNoAccess()`, `sugar_cleanup()`

## Notes
- Vérifie `$focus->ACLAccess('Delete')` avant suppression (ligne 57).
