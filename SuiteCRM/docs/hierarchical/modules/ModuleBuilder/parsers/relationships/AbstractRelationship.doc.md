# AbstractRelationship.php

**Chemin :** `modules/ModuleBuilder/parsers/relationships/AbstractRelationship.php`
**Type :** PHP (model / classe abstraite)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Classe abstraite de base pour toutes les relations dans ModuleBuilder/Studio. Stocke la définition complète d'une relation (métadonnées), fournit les méthodes communes de construction (labels, vardefs, subpanels, layoutdefs) et la validation.

## Type
model (classe abstraite)

## Dépendances clés
- Aucune dépendance explicite dans ce fichier — les sous-classes l'étendent

## Exports/Symboles principaux
- `AbstractRelationship` — classe abstraite
  - `$definitionKeys` (statique) — liste des 30+ clés définissant une relation (relationship_name, lhs_module, rhs_module, relationship_type, join_table, etc.)
  - `getDefinition()` / `setDefinition()` — accès à la définition
  - `buildLabels()`, `buildVardefs()`, `buildSubpanelDefs()`, `buildRelationshipMetaData()`, `buildLayoutFields()` — méthodes de construction (implémentées dans les sous-classes)
  - `getFromStudio()` / `isReadonly()` — attributs de la relation
  - Accesseurs : `getLhsModule()`, `getRhsModule()`, `getRelationshipName()`, `getType()`
  - `validSubpanel($file)` (statique) — vérifie qu'un fichier subpanel est valide

## Interactions
- **Héritée par :** `ManyToManyRelationship`, `OneToManyRelationship`, `OneToOneRelationship`, `ManyToOneRelationship`, `ActivitiesRelationship`
- **Utilisée par :** `AbstractRelationships`, `RelationshipFactory`

## Notes
- `$definition['readonly']` = true pour les relations OOB non modifiables.
- `$definition['deleted']` = true pour les relations supprimées (elles restent stockées mais ne sont pas buildées).
- `relationship_role_column` / `relationship_role_column_value` permettent des relations conditionnelles sur une même table. Commentaire ligne 92.
