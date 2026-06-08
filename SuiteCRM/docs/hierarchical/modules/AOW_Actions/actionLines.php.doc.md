# Fichier actionLines.php — AOW_Actions
**Chemin :** `modules/AOW_Actions/actionLines.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

## Rôle fonctionnel
Bibliothèque de rendu HTML pour le widget des lignes d'actions dans le formulaire EditView de AOW_WorkFlow. Génère le tableau interactif permettant d'ajouter/configurer les actions.

## Type
helper / vue

## Notes
Invoqué via un function field dans les vardefs de AOW_WorkFlow. Délègue à `actionBase::edit_display()` pour chaque type d'action.
