# ManyToManyRelationship.php

**Chemin :** `modules/ModuleBuilder/parsers/relationships/ManyToManyRelationship.php`
**Type :** PHP (model)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Implémente les métadonnées et la construction d'une relation Many-To-Many. Génère les subpanels, vardefs, layoutdefs, labels, et la table de jointure pour les deux modules participants.

## Type
model

## Dépendances clés
- `AbstractRelationship` (classe parente)

## Exports/Symboles principaux
- `ManyToManyRelationship` — classe (hérite de `AbstractRelationship`)
  - `buildSubpanelDefs()` — génère les définitions de subpanels pour LHS et RHS
  - `buildVardefs()` — génère les vardefs (champs link) pour LHS et RHS
  - `buildRelationshipMetaData()` — génère la métadonnée de relation (table de jointure)
  - `buildLabels()` — génère les labels pour LHS et RHS
  - `buildLayoutFields()` — ajoute le champ link dans les layouts existants

## Interactions
- **Créée par :** `RelationshipFactory`
- **Héritée par :** (aucune connue)
- **Appelle :** méthodes du parent `AbstractRelationship`

## Notes
Chaque relation N-N génère sa propre table de jointure (`{relationship_name}`) — différence avec l'approche OOB qui partage des tables. Commentaire dans le fichier source.
