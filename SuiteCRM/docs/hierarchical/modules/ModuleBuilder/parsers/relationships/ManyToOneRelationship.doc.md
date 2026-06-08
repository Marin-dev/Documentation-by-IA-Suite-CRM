# ManyToOneRelationship.php

**Chemin :** `modules/ModuleBuilder/parsers/relationships/ManyToOneRelationship.php`
**Type :** PHP (model)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Implémente une relation Many-To-One. Identique à `OneToManyRelationship` mais avec les modules LHS et RHS inversés.

## Type
model

## Dépendances clés
- `AbstractRelationship` (classe parente)
- `OneToManyRelationship` (`parsers/relationships/OneToManyRelationship.php`) — délégation
- `constants.php`

## Exports/Symboles principaux
- `ManyToOneRelationship` — classe (hérite de `AbstractRelationship`)
  - Délègue l'essentiel à `OneToManyRelationship` avec inversion LHS/RHS

## Interactions
- **Créée par :** `RelationshipFactory`

## Notes
Commentaire explicite dans le code source (ligne 52) : "Exactly the same as a one-to-many relationship except lhs and rhs modules have been reversed."
