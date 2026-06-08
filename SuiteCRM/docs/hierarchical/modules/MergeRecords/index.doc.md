# index.php

**Chemin :** `modules/MergeRecords/index.php`
**Type :** PHP - Point d'entrée du module
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Point d'entrée du module MergeRecords. Vérifie les droits ACL Edit sur les deux enregistrements à fusionner avant de lancer le processus. Reçoit les IDs via `$_REQUEST['uid']` (séparés par virgules).

## Type
view (entrée)

## Dépendances clés
- `SugarModule::get()` — chargement des beans
- `$_REQUEST['uid']` — IDs des enregistrements à fusionner
- `$_REQUEST['action_module']` — module source

## Exports / Symboles principaux
Aucune classe. Script procédural.

## Interactions
- **Appelé par :** actions de masse "Fusionner" dans les vues liste
- **Appelle :** `SugarModule::get()`, `loadBean()`

## Notes
- Vérification ACL Edit sur les 2 beans (Bug 18852 commenté).
