# Spots.php

**Chemin :** `modules/Spots/Spots.php`
**Type :** PHP - Model
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Bean représentant un "Spot" dans SuiteCRM (table `spots`). Fonctionnalité spécifique SuiteCRM pour des zones de contenu personnalisables (INCONNU précisément — le rôle métier exact n'est pas documenté dans le code). Non importable, sécurité par ligne désactivée.

## Type
model

## Dépendances clés
- `Basic` (classe parente)

## Exports / Symboles principaux
- `Spots` (classe) — étend `Basic`
  - Table : `spots`
  - `$disable_row_level_security = true`
  - `$importable = false`

## Interactions
- **Appelé par :** `SpotsDashlet`, contrôleur Spots
- **Appelle :** logique `Basic`

## Notes
- Rôle métier INCONNU — documentation interne insuffisante.
