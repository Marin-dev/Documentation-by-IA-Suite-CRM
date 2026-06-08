# RelationshipFactory.php

**Chemin :** `modules/ModuleBuilder/parsers/relationships/RelationshipFactory.php`
**Type :** PHP (helper / factory)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Factory pour instancier le bon type de relation selon la définition fournie. Supporte 1-1, 1-N, N-1, N-N, et le cas spécial Activities.

## Type
helper (factory)

## Dépendances clés
- `constants.php` (`parsers/constants.php`) — constantes MB_ONETOONE, MB_ONETOMANY, etc.
- `OneToOneRelationship`, `OneToManyRelationship`, `ManyToOneRelationship`, `ManyToManyRelationship`, `ActivitiesRelationship`

## Exports/Symboles principaux
- `RelationshipFactory` — classe (méthodes statiques)
  - `newRelationship($definition)` (statique) — instancie le bon type de relation

## Interactions
- **Appelé par :** `AbstractRelationships::addFromPost()`, `MBRelationship::add()`
- **Appelle :** les 5 classes de relation concrètes

## Notes
- Si `relationship_type` non défini, le type par défaut est `many-to-many`. Ligne 58.
- Le cas `for_activities == true` est traité avant le switch sur le type. Ligne 62.
