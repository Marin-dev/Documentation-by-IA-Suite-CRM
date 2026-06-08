# MetaDataParserInterface.php

**Chemin :** `modules/ModuleBuilder/parsers/views/MetaDataParserInterface.php`
**Type :** PHP (interface)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Interface définissant le contrat pour les parsers de métadonnées de vues (abstraction du pattern Bridge).

## Type
autre (interface)

## Exports/Symboles principaux
- `MetaDataParserInterface` — interface
  - `handleSave()` — sauvegarde le layout
  - `getLayout()` — retourne le layout courant
  - `getLanguage()` — retourne le module de langue
  - `getHistory()` — retourne l'historique

## Interactions
- **Implémentée par :** `GridLayoutMetaDataParser`, `ListLayoutMetaDataParser` (via `AbstractMetaDataParser`)
