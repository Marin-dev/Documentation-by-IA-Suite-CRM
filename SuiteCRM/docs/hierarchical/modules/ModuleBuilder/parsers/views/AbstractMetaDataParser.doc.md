# AbstractMetaDataParser.php

**Chemin :** `modules/ModuleBuilder/parsers/views/AbstractMetaDataParser.php`
**Type :** PHP (model / classe abstraite)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Classe abstraite commune à tous les parsers de métadonnées de vues. Fournit l'interface de base (handleSave, getLayout, getLanguage, getHistory) et les propriétés communes (fielddefs, viewdefs, implementation, history).

## Type
model (classe abstraite)

## Dépendances clés
- `AbstractMetaDataImplementation` (composant via Bridge pattern)
- `History`

## Exports/Symboles principaux
- `AbstractMetaDataParser` — classe abstraite
  - `handleSave()` — sauvegarde le layout (via implementation)
  - `getLayout()` — retourne les viewdefs courantes
  - `getLanguage()` — retourne le module de langue
  - `getHistory()` — retourne l'historique
  - `removeField($fieldName)` — retire un champ du layout
  - `writeWorkingFile()` — écrit en fichier de travail
  - `$_fielddefs` / `$_viewdefs` — données principales
  - `$implementation` — implémentation Bridge

## Interactions
- **Héritée par :** `GridLayoutMetaDataParser`, `ListLayoutMetaDataParser`
- **Implémente :** `MetaDataParserInterface`

## Notes
Utilisé conjointement avec `AbstractMetaDataImplementation` selon le pattern Bridge pour découpler logique de parsing et I/O fichier.
