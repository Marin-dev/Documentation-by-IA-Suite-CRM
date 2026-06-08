# RelationshipsInterface.php

**Chemin :** `modules/ModuleBuilder/parsers/relationships/RelationshipsInterface.php`
**Type :** PHP (interface)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Interface définissant le contrat pour les classes de gestion de relations (DeployedRelationships et UndeployedRelationships).

## Type
autre (interface)

## Dépendances clés
Aucune.

## Exports/Symboles principaux
- `RelationshipsInterface` — interface
  - `findRelatableModules()` (statique) — liste des modules pouvant participer
  - `load()` — chargement des relations
  - `getRelationshipList()` — liste des noms
  - `get($relationshipName)` — accès par nom
  - `add($relationship)` — ajout d'une relation

## Interactions
- **Implémentée par :** `DeployedRelationships`, `UndeployedRelationships`

## Notes
`delete()` est commenté dans l'interface (ligne 59) — les implémentations le définissent mais le contrat formel ne l'exige pas.
