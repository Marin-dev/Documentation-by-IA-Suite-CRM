# Fichier conditionLines.php — AOR_Conditions

**Chemin :** `modules/AOR_Conditions/conditionLines.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

## Rôle fonctionnel
Bibliothèque de rendu HTML pour le widget de saisie des lignes de conditions dans le formulaire EditView de AOR_Reports. Génère le tableau interactif des conditions avec sélecteurs de champ, opérateur, type et valeur.

## Type
helper / vue

## Dépendances clés
- `$app_list_strings` — listes opérateurs, types
- `aor_utils.php` — `getDisplayForField()`
- JavaScript front-end de l'éditeur de rapport

## Notes
Invoqué via le function field `condition_lines` déclaré dans `AOR_Reports/vardefs.php`. La fonction d'entrée est probablement `display_condition_lines()`.
