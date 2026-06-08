# OneToOneRelationship.php

**Chemin :** `modules/ModuleBuilder/parsers/relationships/OneToOneRelationship.php`
**Type :** PHP (model)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Implémente les métadonnées et la construction d'une relation One-To-One. Génère un champ relate de chaque côté de la relation.

## Type
model

## Dépendances clés
- `AbstractRelationship` (classe parente)

## Exports/Symboles principaux
- `OneToOneRelationship` — classe (hérite de `AbstractRelationship`)

## Interactions
- **Créée par :** `RelationshipFactory`
- **Appelle :** méthodes du parent

## Notes
Relations 1-1 peu communes dans SuiteCRM — exemples OOB dans InboundEmail et Schedulers. Deux champs relate, un de chaque côté.
