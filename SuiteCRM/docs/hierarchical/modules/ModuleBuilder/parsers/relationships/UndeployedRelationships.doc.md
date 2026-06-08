# UndeployedRelationships.php

**Chemin :** `modules/ModuleBuilder/parsers/relationships/UndeployedRelationships.php`
**Type :** PHP (model)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Gère les relations d'un module non-deployé dans un package MB. Charge depuis `{path}/relationships.php`, sauvegarde dans le même fichier, et build les fichiers dans le répertoire de build du package. Implémente `RelationshipsInterface`.

## Type
model

## Dépendances clés
- `AbstractRelationships` (classe parente)
- `RelationshipsInterface`
- `RelationshipFactory` (`parsers/relationships/RelationshipFactory.php`)
- `ModuleBuilder` (`MB/ModuleBuilder.php`) — pour récupérer la clé du package

## Exports/Symboles principaux
- `UndeployedRelationships` — classe (hérite de `AbstractRelationships`, implémente `RelationshipsInterface`)
  - `load()` — charge depuis `{basepath}/relationships.php`
  - `save()` — sauvegarde dans `{basepath}/relationships.php`
  - `build($basepath)` — construit les fichiers de relation dans le répertoire de build du package
  - `addInstallDefs(&$installDefs)` — ajoute les entrées `relationships` dans les installdefs du package
  - `findRelatableModules()` — modules déployés ET non-déployés (packages MB)

## Interactions
- **Appelé par :** `MBModule` (à la construction), `MBRelationship`, `ModuleBuilderController`
- **Appelle :** `RelationshipFactory`, `ModuleBuilder`

## Notes
- `findRelatableModules()` inclut les modules non-deployés des packages MB — différence clé avec `DeployedRelationships`. Ligne 80.
- La clé de package (`$packageKey`) est résolue via `ModuleBuilder::getPackageKey()` depuis le manifest. Ligne 72.
- `$basepath` est le répertoire du module dans le package (ex. `custom/modulebuilder/packages/{pkg}/modules/{mod}`).
