# AbstractMetaDataImplementation.php

**Chemin :** `modules/ModuleBuilder/parsers/views/AbstractMetaDataImplementation.php`
**Type :** PHP (model / classe abstraite)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Classe abstraite de base (pattern Bridge) pour les implémentations de métadonnées de vues. Gère la résolution des fichiers source (base, custom, working, history), le chargement des viewdefs, et l'interface commune entre les parsers et les fichiers de layouts.

## Type
model (classe abstraite)

## Dépendances clés
- `constants.php` (`parsers/constants.php`)
- `History` (`parsers/views/History.php`)

## Exports/Symboles principaux
- `AbstractMetaDataImplementation` — classe abstraite
  - `getViewdefs()` — retourne les viewdefs chargées
  - `getFielddefs()` — retourne les field_defs du module
  - `getOriginalViewdefs()` — retourne les viewdefs de base (non-customisées)
  - `getHistory()` — retourne l'objet `History`
  - `getLanguage()` — retourne le module pour la langue
  - `deploy($layoutDefinitions)` — sauvegarde les définitions (implémenté dans les sous-classes)
  - `$_fileVariables` — mapping view type -> variable PHP dans le fichier (ex. `listview => listViewDefs`)

## Interactions
- **Héritée par :** `DeployedMetaDataImplementation`, `UndeployedMetaDataImplementation`, `DeployedSubpanelImplementation`, `UndeployedSubpanelImplementation`
- **Utilisée par :** `AbstractMetaDataParser` (via composition)

## Notes
Implémente le pattern Bridge : sépare l'abstraction (parsers) de l'implémentation (lecture/écriture des fichiers). Le pattern permet de switcher entre modules déployés et non-déployés sans modifier les parsers.
