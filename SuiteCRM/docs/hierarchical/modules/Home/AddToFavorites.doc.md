# AddToFavorites.php

**Chemin :** `modules/Home/AddToFavorites.php`
**Type :** PHP - Helper (action AJAX)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Script AJAX qui ajoute un enregistrement CRM dans les favoris de l'utilisateur courant. Reçoit `target_module` et `target_id` en paramètres POST/GET et stocke la référence dans les préférences utilisateur (clé `objects` de la catégorie `favorites`). Retourne 1 en cas de succès, 0 sinon.

## Type
helper

## Dépendances clés
- `$current_user` (global) — pour `getPreference` / `setPreference`

## Exports / Symboles principaux
Aucune classe ni fonction exportée. Script procédural.

## Interactions
- **Appelé par :** appels AJAX front-end depuis les vues liste/détail (bouton "Ajouter aux favoris")
- **Appelle :** `$current_user->getPreference()`, `$current_user->setPreference()`

## Notes
- Pas de protection `sugarEntry` en haut du fichier (contrairement à la plupart des autres scripts).
- Stocke dans `$current_user->preferences['favorites']['objects'][$module][$id] = true`.
