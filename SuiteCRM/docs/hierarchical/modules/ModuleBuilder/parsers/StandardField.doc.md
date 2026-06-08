# StandardField.php

**Chemin :** `modules/ModuleBuilder/parsers/StandardField.php`
**Type :** PHP (model)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Extension de `DynamicField` spécialisée pour la modification des champs standard (OOB) d'un module déployé depuis Studio. Permet de modifier les propriétés d'un champ existant sans créer un nouveau champ custom, en écrivant uniquement les delta par rapport à la définition de base.

## Type
model

## Dépendances clés
- `DynamicField` (`modules/DynamicFields/DynamicField.php`) — classe parente
- `FieldCases` (`modules/DynamicFields/FieldCases.php`) — `get_widget()`

## Exports/Symboles principaux
- `StandardField` — classe (hérite de `DynamicField`)
  - `addFieldObject(&$field)` — applique les modifications d'un champ standard en écrivant uniquement les deltas (différences par rapport à la définition de base) dans l'extension vardef
  - `loadCustomDef($field)` — charge la définition custom existante depuis `custom/Extension/modules/{module}/Ext/Vardefs/sugarfield_{field}.php`
  - `loadBaseDef($field)` — charge la définition de base depuis `modules/{module}/vardefs.php`

## Interactions
- **Appelé par :** `ModuleBuilderController::action_saveSugarField()`
- **Appelle :** `DynamicField::writeVardefExtension()`, `get_widget()`

## Notes
- `addFieldObject()` utilise `isDefaultValue()` (héritée) pour éviter d'écrire les valeurs par défaut dans l'extension — optimisation pour ne pas "polluer" les customisations. Ligne 133.
- Gère le cas `duplicate_merge_dom_value` sans `duplicate_merge` pour éviter des entrées orphelines. Ligne 164.
- Différence clé avec `DynamicField` : modifie les champs existants (OOB), ne crée pas de nouveau champ.
