# SavedSearch.php

**Chemin :** `modules/SavedSearch/SavedSearch.php`
**Type :** PHP - Model
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Bean représentant une recherche sauvegardée par un utilisateur dans SuiteCRM. Stocke les critères de recherche sérialisés pour un module donné, permettant à l'utilisateur de réutiliser des filtres fréquents.

## Type
model

## Dépendances clés
- `SugarBean` (classe parente)
- `include/templates/TemplateGroupChooser.php`

## Exports / Symboles principaux
- `SavedSearch` (classe) — étend `SugarBean`
  - Champs : `$id`, `$assigned_user_id`, `$date_entered`, `$date_modified`, etc.

## Interactions
- **Appelé par :** vues de liste des modules (barre de recherche), `SavedSearch/ListView.php`

## Notes
- Données de recherche stockées sous forme sérialisée/JSON.
