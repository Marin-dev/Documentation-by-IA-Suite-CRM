# MBRelationship.php

**Chemin :** `modules/ModuleBuilder/MB/MBRelationship.php`
**Type :** PHP (model / adaptateur)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Adaptateur (pattern Adapter) qui encapsule `UndeployedRelationships` pour maintenir la compatibilité avec l'ancien format d'interface de ModuleBuilder. Délègue toutes les opérations à l'implémentation `UndeployedRelationships`.

## Type
model (adaptateur)

## Dépendances clés
- `UndeployedRelationships` (`parsers/relationships/UndeployedRelationships.php`)
- `AbstractRelationships` (`parsers/relationships/AbstractRelationships.php`)
- `AbstractRelationship` (`parsers/relationships/AbstractRelationship.php`)
- `ManyToManyRelationship` (`parsers/relationships/ManyToManyRelationship.php`)
- `RelationshipFactory` (`parsers/relationships/RelationshipFactory.php`)

## Exports/Symboles principaux
- `MBRelationship` — classe adaptateur
  - `findRelatableModules()` — délègue à `UndeployedRelationships`
  - `addFromPost()` — délègue
  - `getRelationshipList()` — délègue
  - `get($name)` — délègue
  - `add($rel)` — convertit ancien format, crée via `RelationshipFactory`, délègue
  - `delete($name)` / `save()` / `build($path)` / `addInstallDefs()` — délèguent tous
- `$relationships` — tableau public maintenu en sync avec l'implémentation (compatibilité ascendante)

## Interactions
- **Appelé par :** code ancien ModuleBuilder (peu utilisé directement — `MBModule` utilise `UndeployedRelationships` directement)
- **Appelle :** `UndeployedRelationships`, `RelationshipFactory`, `AbstractRelationships::convertFromOldFormat()`

## Notes
- Ce fichier est explicitement marqué comme transitoire dans les commentaires (ligne 50) : "As ModuleBuilder is updated, references to this class should be replaced by direct references to UndeployedRelationships".
- `updateRelationshipVariable()` synchronise `$this->relationships` (format ancien) à partir de l'implémentation — méthode privée appelée après chaque mutation.
