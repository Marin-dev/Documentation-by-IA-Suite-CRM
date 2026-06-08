# MBVardefs.php

**Chemin :** `modules/ModuleBuilder/MB/MBVardefs.php`
**Type :** PHP (model)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Gère les définitions de champs (vardefs) d'un module ModuleBuilder non-deployé. Charge les vardefs depuis les templates SugarObjects et fusionne avec les champs personnalisés du module. Écrit `vardefs.php` lors de la sauvegarde.

## Type
model

## Dépendances clés
- Constantes `MB_TEMPLATES` et `MB_IMPLEMENTS` (définies dans `MBModule.php`)
- Fonctions globales : `write_array_to_file()`

## Exports/Symboles principaux
- `MBVardefs` — classe
  - `load()` — charge `$vardefs` depuis `{path}/vardefs.php`
  - `mergeVardefs($by_group)` — fusionne les vardefs des templates avec les champs custom
  - `updateVardefs($by_group)` — alias de `mergeVardefs()`
  - `getVardefs()` — retourne les vardefs fusionnées (templates + custom)
  - `getVardef()` — retourne uniquement les vardefs custom
  - `addFieldVardef($vardef)` — ajoute un champ custom
  - `deleteField($field)` — supprime un champ custom
  - `save()` — écrit `{path}/vardefs.php` (uniquement les champs custom)
  - `build($path)` — écrit `{path}/vardefs.php` complet (fusionné) au format `$dictionary`

## Interactions
- **Appelé par :** `MBModule`
- **Appelle :** fonctions globales Sugar

## Notes
- Distinction importante : `$vardef` = champs custom seuls (sauvegardés), `$vardefs` = champs fusionnés templates+custom (utilisés en mémoire).
- `loadTemplate()` supprime le champ `name` si le template est `file` (Bug40450 — fix pour éviter doublon du champ Name). Ligne 84.
- `build()` écrit le format `$dictionary["moduleName"]` tandis que `save()` écrit le format `$vardefs` — formats différents pour deux usages différents.
