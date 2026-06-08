# Delete.php

**Chemin :** `modules/ProspectLists/Delete.php`
**Type :** PHP - Script d'action (suppression)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Gère la suppression d'une liste de prospects. Vérifie les droits ACL, marque l'enregistrement comme supprimé, puis redirige.

## Type
helper

## Dépendances clés
- `BeanFactory::newBean('ProspectLists')`
- `ACLController::displayNoAccess()`
- `include/formbase.php` — `handleRedirect()`

## Exports / Symboles principaux
Aucune classe. Script procédural.

## Interactions
- **Appelé par :** action Delete du module ProspectLists
- **Appelle :** `mark_deleted()`, `handleRedirect()`

## Notes
- Utilise `mark_deleted()` (soft delete), pas `delete()`.
