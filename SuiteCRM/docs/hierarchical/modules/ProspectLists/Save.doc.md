# Save.php

**Chemin :** `modules/ProspectLists/Save.php`
**Type :** PHP - Script d'action (sauvegarde)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Gère la sauvegarde d'une liste de prospects. Vérifie si l'utilisateur assigné a changé pour déclencher une notification. Charge l'enregistrement existant et applique les modifications.

## Type
helper

## Dépendances clés
- `BeanFactory::newBean('ProspectLists')`
- `$_POST['record']`, `$_POST['assigned_user_id']`
- `$current_user`

## Exports / Symboles principaux
Aucune classe. Script procédural.

## Interactions
- **Appelé par :** formulaires EditView de ProspectLists
- **Appelle :** `ProspectList::retrieve()`, `ProspectList::save()`

## Notes
- `$check_notify = true` si l'utilisateur assigné change et est différent de l'utilisateur courant.
