# MetaDataImplementationInterface.php

**Chemin :** `modules/ModuleBuilder/parsers/views/MetaDataImplementationInterface.php`
**Type :** PHP (interface)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Interface définissant le contrat pour les implémentations de métadonnées (composant du pattern Bridge).

## Type
autre (interface)

## Exports/Symboles principaux
- `MetaDataImplementationInterface` — interface
  - `getViewdefs()` — retourne les viewdefs
  - `getFielddefs()` — retourne les field_defs
  - `getLanguage()` — retourne le module de langue
  - `deploy($layoutDefinitions)` — persiste les définitions
  - `getHistory()` — retourne l'historique

## Interactions
- **Implémentée par :** `DeployedMetaDataImplementation`, `UndeployedMetaDataImplementation`, `DeployedSubpanelImplementation`, `UndeployedSubpanelImplementation`
