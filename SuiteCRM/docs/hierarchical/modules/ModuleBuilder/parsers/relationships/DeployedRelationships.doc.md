# DeployedRelationships.php

**Chemin :** `modules/ModuleBuilder/parsers/relationships/DeployedRelationships.php`
**Type :** PHP (model)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Gère les relations d'un module déployé (OOB ou installé). Charge les relations depuis la table `relationships` (via le SugarRelationshipFactory) et les fichiers working custom. Les relations OOB sont en lecture seule. Implémente `RelationshipsInterface`.

## Type
model

## Dépendances clés
- `AbstractRelationships` (classe parente)
- `RelationshipsInterface`
- `RelationshipFactory` (`parsers/relationships/RelationshipFactory.php`)
- `SugarRelationshipFactory` (`data/Relationships/RelationshipFactory.php`) — accès aux relations déployées

## Exports/Symboles principaux
- `DeployedRelationships` — classe (hérite de `AbstractRelationships`, implémente `RelationshipsInterface`)
  - `load()` — charge relations custom (working) + relations déployées (readonly)
  - `save()` — sauvegarde les relations custom dans `custom/working/modules/{Module}/metadata/`
  - `build()` — reconstruit les fichiers Extension pour toutes les relations custom
  - `delete($name)` — marque comme supprimée et rebuild
  - `addFromPost()` — crée depuis `$_POST`, sauvegarde et build
  - `findRelatableModules()` — délègue au parent (inclut sous-modules Activities)

## Interactions
- **Appelé par :** `ModuleBuilderController` (`action_SaveRelationship`, `action_DeleteRelationship`, `action_SaveRelationshipLabel`), `StudioModule::getRelationships()`, `MBPackage::getCustomRelationshipsByModuleName()`
- **Appelle :** `SugarRelationshipFactory`, `RelationshipFactory`, `AbstractRelationship::build*()` méthodes

## Notes
- Les relations déployées (OOB) sont marquées `readonly=true` — elles apparaissent dans la liste mais ne peuvent pas être modifiées. Commentaire ligne 75.
- `build()` génère les fichiers dans `custom/Extension/modules/{module}/Ext/{Language|Vardefs|Layoutdefs|Relationships}/` — format Extension SugarCRM.
