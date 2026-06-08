# Relationship.php

**Chemin :** `modules/Relationships/Relationship.php`
**Type :** PHP - Model
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Bean représentant une relation entre deux modules dans SuiteCRM (table `relationships`). Décrit les métadonnées d'une relation : modules gauche/droit, tables, clés de jointure, type de relation (many-to-many, one-to-many, etc.).

## Type
model

## Dépendances clés
- `SugarBean` (classe parente)

## Exports / Symboles principaux
- `Relationship` (classe) — étend `SugarBean`
  - Table : `relationships`
  - Champs : `$relationship_name`, `$lhs_module`, `$lhs_table`, `$lhs_key`, `$rhs_module`, et autres (INCONNU)

## Interactions
- **Appelé par :** `RelationshipHandler`, Studio, ModuleBuilder
- **Appelle :** logique `SugarBean`

## Notes
- Utilisé par le framework de relations SugarCRM/SuiteCRM pour déterminer les jointures SQL.
