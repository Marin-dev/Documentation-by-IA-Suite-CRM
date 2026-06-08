# UserPreference.php

**Chemin :** `modules/UserPreferences/UserPreference.php`
**Type :** PHP - Model
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Bean gérant les préférences utilisateur dans SuiteCRM. Stocke et récupère les préférences individuelles (langue, fuseau horaire, format de date, disposition des dashlets, etc.) dans une table dédiée, séparée de la table `users`.

## Type
model

## Dépendances clés
- `SugarBean` (classe parente)

## Exports / Symboles principaux
- `UserPreference` (classe) — étend `SugarBean`
  - Champs : `$id`, `$date_entered`, et autres (INCONNU — lecture partielle)

## Interactions
- **Appelé par :** `$current_user->getPreference()` / `setPreference()`, tous les modules utilisant des préférences
- **Appelle :** logique `SugarBean`

## Notes
- Table centrale pour toutes les personnalisations par utilisateur.
