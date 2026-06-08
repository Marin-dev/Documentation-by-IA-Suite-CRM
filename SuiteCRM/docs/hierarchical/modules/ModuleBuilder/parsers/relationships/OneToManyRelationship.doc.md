# OneToManyRelationship.php

**Chemin :** `modules/ModuleBuilder/parsers/relationships/OneToManyRelationship.php`
**Type :** PHP (model)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Implémente les métadonnées et la construction d'une relation One-To-Many. Génère : un subpanel sur le module LHS, un champ relate sur le module RHS, les vardefs correspondants, les labels, et les layoutdefs.

## Type
model

## Dépendances clés
- `AbstractRelationship` (classe parente)

## Exports/Symboles principaux
- `OneToManyRelationship` — classe (hérite de `AbstractRelationship`)
  - Méthodes de build similaires à `ManyToManyRelationship` mais pour 1-N

## Interactions
- **Créée par :** `RelationshipFactory`
- **Héritée par :** `ManyToOneRelationship` (inverse), `ActivitiesRelationship`

## Notes
La relation 1-N = subpanel côté LHS + champ relate côté RHS. Différent de N-N qui génère une table de jointure.
