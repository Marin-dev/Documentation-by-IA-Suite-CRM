# DeployedMetaDataImplementation.php

**Chemin :** `modules/ModuleBuilder/parsers/views/DeployedMetaDataImplementation.php`
**Type :** PHP (model / implémentation Bridge)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Implémentation Bridge pour les modules déployés (Studio). Gère la lecture depuis `modules/{Module}/metadata/` et `custom/modules/{Module}/metadata/`, et la sauvegarde vers `custom/modules/{Module}/metadata/`. Supporte l'historique des versions.

## Type
model

## Dépendances clés
- `AbstractMetaDataImplementation` (classe parente)
- `MetaDataImplementationInterface`
- `StudioModuleFactory` — pour les overrides de type de vue
- `History` — gestion de l'historique
- `ListLayoutMetaDataParser`, `GridLayoutMetaDataParser`, `PopupMetaDataParser`

## Exports/Symboles principaux
- `DeployedMetaDataImplementation` — classe
  - Constructeur : détermine les chemins source (base/custom/working) pour la vue donnée
  - `getViewdefs()` / `getFielddefs()` / `getLanguage()` / `getHistory()`
  - `deploy($layoutDefinitions)` — sauvegarde dans `custom/modules/{Module}/metadata/`

## Interactions
- **Créée par :** `GridLayoutMetaDataParser`, `ListLayoutMetaDataParser` (quand `packageName` vide ou 'studio')
- **Appelle :** `History`, `StudioModuleFactory`

## Notes
Pattern : working > custom > base pour la résolution du fichier source (priorité au brouillon). Décision implicite dans le constructeur.
