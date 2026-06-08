# UndeployedSubpanelImplementation.php

**Chemin :** `modules/ModuleBuilder/parsers/views/UndeployedSubpanelImplementation.php`
**Type :** PHP (model / implémentation Bridge)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Implémentation Bridge pour les subpanels de modules non-déployés (packages MB). Similaire à `DeployedSubpanelImplementation` mais lit/écrit dans le répertoire du package MB.

## Type
model

## Dépendances clés
- `AbstractMetaDataImplementation` (classe parente)
- `MetaDataImplementationInterface`
- `constants.php`

## Exports/Symboles principaux
- `UndeployedSubpanelImplementation` — classe
  - `HISTORYFILENAME = 'restored.php'`
  - `HISTORYVARIABLENAME = 'layout_defs'`

## Interactions
- **Créée par :** `SubpanelMetaDataParser` (quand `packageName` non vide)
