# parser.searchfields.php

**Chemin :** `modules/ModuleBuilder/parsers/parser.searchfields.php`
**Type :** PHP (model / parser)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Parser pour les champs de recherche (`SearchFields.php`). Gère la lecture et l'écriture des métadonnées de recherche pour les modules déployés (Studio) et non-déployés (MB). Utilisé pour ajouter/supprimer des champs des formulaires de recherche.

## Type
model

## Dépendances clés
- `ModuleBuilderParser` (classe parente)
- `MBPackage` (`MB/MBPackage.php`) — pour récupérer la clé du package

## Exports/Symboles principaux
- `ParserSearchFields` — classe (hérite de `ModuleBuilderParser`)
  - `getSearchFields()` — charge depuis MB, custom, ou base selon contexte
  - `addSearchField($name, $searchField)` — ajoute un champ de recherche
  - `removeSearchField($name)` — supprime un champ de recherche
  - `saveSearchFields($searchFields)` — sauvegarde dans le fichier `SearchFields.php` approprié

## Interactions
- **Appelé par :** `SearchViewMetaDataParser` (INCONNU — à vérifier dans les parsers/views/)
- **Appelle :** `MBPackage`

## Notes
- Chemin de sauvegarde différent selon contexte : `custom/modulebuilder/packages/{pkg}/modules/{mod}/metadata/SearchFields.php` (MB) ou `custom/modules/{mod}/metadata/SearchFields.php` (Studio). Ligne 107.
