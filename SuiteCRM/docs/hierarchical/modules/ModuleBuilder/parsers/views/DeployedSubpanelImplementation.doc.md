# DeployedSubpanelImplementation.php

**Chemin :** `modules/ModuleBuilder/parsers/views/DeployedSubpanelImplementation.php`
**Type :** PHP (model / implémentation Bridge)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Implémentation Bridge pour les subpanels de modules déployés. Utilise `SubPanelDefinitions` pour charger les définitions et crée un fichier intermédiaire pour que le mécanisme d'historique puisse les gérer.

## Type
model

## Dépendances clés
- `AbstractMetaDataImplementation` (classe parente)
- `MetaDataImplementationInterface`
- `SubPanelDefinitions` (`include/SubPanel/SubPanelDefinitions.php`)

## Exports/Symboles principaux
- `DeployedSubpanelImplementation` — classe
  - `HISTORYFILENAME = 'restored.php'`
  - `HISTORYVARIABLENAME = 'layout_defs'`
  - Charge via `SubPanelDefinitions`, expose `getViewdefs()`, `deploy()`

## Interactions
- **Créée par :** `SubpanelMetaDataParser` (quand `packageName` vide)
- **Appelle :** `SubPanelDefinitions`
