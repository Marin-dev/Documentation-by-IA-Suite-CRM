# constants.php

**Chemin :** `modules/ModuleBuilder/parsers/constants.php`
**Type :** PHP (config)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Définit toutes les constantes et la classe `MBConstants` utilisées dans l'ensemble du module ModuleBuilder. Référentiel central des noms de vues, types de métadonnées, types de relations, et limites techniques.

## Type
config

## Dépendances clés
Aucune.

## Exports/Symboles principaux
Constantes définies :
| Constante | Valeur | Rôle |
|---|---|---|
| `MB_BASEMETADATALOCATION` | `'base'` | Emplacement metadata de base |
| `MB_CUSTOMMETADATALOCATION` | `'custom'` | Emplacement metadata custom |
| `MB_WORKINGMETADATALOCATION` | `'working'` | Emplacement metadata de travail |
| `MB_HISTORYMETADATALOCATION` | `'history'` | Emplacement historique |
| `MB_LISTVIEW` | `'listview'` | Type vue liste |
| `MB_BASICSEARCH` | `'basic_search'` | Vue recherche basique |
| `MB_ADVANCEDSEARCH` | `'advanced_search'` | Vue recherche avancée |
| `MB_DASHLET` | `'dashlet'` | Vue dashlet |
| `MB_EDITVIEW` | `'editview'` | Vue édition |
| `MB_DETAILVIEW` | `'detailview'` | Vue détail |
| `MB_QUICKCREATE` | `'quickcreate'` | Vue création rapide |
| `MB_POPUPLIST` | `'popuplist'` | Vue popup liste |
| `MB_POPUPSEARCH` | `'popupsearch'` | Vue popup recherche |
| `MB_ONETOONE` | `'one-to-one'` | Type relation 1-1 |
| `MB_ONETOMANY` | `'one-to-many'` | Type relation 1-N |
| `MB_MANYTOONE` | `'many-to-one'` | Type relation N-1 |
| `MB_MANYTOMANY` | `'many-to-many'` | Type relation N-N |
| `MB_MAXDBIDENTIFIERLENGTH` | `30` | Longueur max identifiant DB |
| `MB_EXPORTPREPEND` | `'project_'` | Préfixe export projet |
| `MB_LABEL` | `'label'` | Type label |
| `MB_VISIBILITY` | `'visibility'` | Type visibilité |

- `MBConstants::$EMPTY` / `MBConstants::$FILLER` — slots vides/filler dans les layouts

## Interactions
- **Inclus par :** `ModuleBuilderController`, `ParserFactory`, `GridLayoutMetaDataParser`, `RelationshipFactory`, `StudioModule`, `AbstractMetaDataImplementation`, et la majorité des parsers

## Notes
Fichier inclus en tout premier dans la chaîne de dépendances — critique pour toute la logique de vues et de relations.
