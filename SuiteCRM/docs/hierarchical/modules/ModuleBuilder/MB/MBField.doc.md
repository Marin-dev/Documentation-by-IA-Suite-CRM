# MBField.php

**Chemin :** `modules/ModuleBuilder/MB/MBField.php`
**Type :** PHP (model)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Représente un champ simple dans un module ModuleBuilder non-deployé. Fournit la génération de la définition vardef (`getFieldVardef()`) pour les types de base (varchar, int, float, bool, enum, date, datetime).

## Type
model

## Dépendances clés
Aucune dépendance externe explicite.

## Exports/Symboles principaux
- `MBField` — classe
  - `getFieldVardef()` — construit et retourne le tableau vardef pour ce champ
  - `addDropDown()` — retourne `$this->options` (stub)
  - `addLabel()` — retourne `$this->vname` (stub)
- Propriétés publiques : `$type`, `$name`, `$label`, `$vname`, `$options`, `$length`, `$required`, `$reportable`, `$default`, `$comment`

## Interactions
- **Appelé par :** INCONNU (classe peu utilisée directement — la logique champ MB passe plutôt par `DynamicFields/FieldCases.php` via `get_widget()`)
- **Appelle :** rien

## Notes
- La valeur sentinel `'MSI1'` pour `$default` (ligne 53) distingue "pas de défaut fourni" de "défaut = null/vide". Logique non-évidente.
- Ne couvre que les types primitifs. Les types complexes (relate, currency, etc.) ne sont pas gérés ici.
