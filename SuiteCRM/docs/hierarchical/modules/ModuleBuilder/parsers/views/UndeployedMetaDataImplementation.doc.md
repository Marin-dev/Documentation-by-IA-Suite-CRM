# UndeployedMetaDataImplementation.php

**Chemin :** `modules/ModuleBuilder/parsers/views/UndeployedMetaDataImplementation.php`
**Type :** PHP (model / implémentation Bridge)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Implémentation Bridge pour les modules non-déployés dans un package ModuleBuilder. Lit et écrit les métadonnées depuis/vers le répertoire du package MB (`custom/modulebuilder/packages/{pkg}/modules/{mod}/metadata/`).

## Type
model

## Dépendances clés
- `AbstractMetaDataImplementation` (classe parente)
- `MetaDataImplementationInterface`
- `ModuleBuilder` (`MB/ModuleBuilder.php`) — accès au module MB
- `ListLayoutMetaDataParser`, `GridLayoutMetaDataParser`

## Exports/Symboles principaux
- `UndeployedMetaDataImplementation` — classe
  - Constructeur : charge le module MB via `ModuleBuilder::getPackageModule()`
  - `deploy($layoutDefinitions)` — sauvegarde dans le répertoire MB metadata

## Interactions
- **Créée par :** `GridLayoutMetaDataParser`, `ListLayoutMetaDataParser` (quand `packageName` non vide et non 'studio')
- **Appelle :** `ModuleBuilder`
