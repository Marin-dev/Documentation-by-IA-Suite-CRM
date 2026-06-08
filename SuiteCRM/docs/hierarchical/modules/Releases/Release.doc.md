# Release.php

**Chemin :** `modules/Releases/Release.php`
**Type :** PHP - Model
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Bean représentant une version de produit (Release) dans SuiteCRM. Utilisé dans le module Bugs pour associer des bogues à des versions de livraison cibles.

## Type
model

## Dépendances clés
- `SugarBean` (classe parente)

## Exports / Symboles principaux
- `Release` (classe) — étend `SugarBean`
  - Champs : `$id`, `$deleted`, et autres (INCONNU — lecture partielle)

## Interactions
- **Appelé par :** module Bugs (relation release)
- **Appelle :** logique `SugarBean`
