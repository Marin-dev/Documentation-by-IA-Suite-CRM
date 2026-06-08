# Favorites.php

**Chemin :** `modules/Favorites/Favorites.php`
**Type :** PHP - Model
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Bean représentant un favori utilisateur dans SuiteCRM (table `favorites`). Permet aux utilisateurs de marquer des enregistrements comme favoris. Non importable, pas de visibilité tracker, sécurité par ligne désactivée.

## Type
model

## Dépendances clés
- `Basic` (classe parente SugarCRM)

## Exports / Symboles principaux
- `Favorites` (classe) — étend `Basic`
  - Table : `favorites`
  - `$tracker_visibility = false`
  - `$disable_row_level_security = true`

## Interactions
- **Appelé par :** `FavoritesDashlet`, contrôleur Favorites
- **Appelle :** logique `Basic`
