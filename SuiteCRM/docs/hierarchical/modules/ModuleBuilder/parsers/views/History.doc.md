# History.php

**Chemin :** `modules/ModuleBuilder/parsers/views/History.php`
**Type :** PHP (helper)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Gère l'historique des versions de layouts dans ModuleBuilder/Studio. Maintient une liste de fichiers de sauvegarde dans le répertoire `history/`, permet de naviguer entre versions et de restaurer une version précédente.

## Type
helper

## Dépendances clés
- `HistoryInterface`
- `constants.php` (MB_HISTORYMETADATALOCATION)

## Exports/Symboles principaux
- `History` — classe (implémente `HistoryInterface`)
  - `append($filename)` — ajoute la version courante à l'historique
  - `getFirst()` — retourne l'identifiant du premier élément (le plus récent)
  - `getNext()` — retourne le suivant (vers le passé)
  - `getPrevious()` — retourne le précédent (vers le présent)
  - `restore($id)` — restaure un fichier de l'historique
  - `getFilename($id)` — chemin complet vers un fichier d'historique
  - `$_previewFilename` — fichier de prévisualisation temporaire

## Interactions
- **Utilisée par :** `AbstractMetaDataImplementation`, `DeployedMetaDataImplementation`, `AbstractMetaDataParser`
- **Appelée par :** vues `view.history.php`

## Notes
Les fichiers d'historique sont nommés par timestamp ou index dans le répertoire `{custom/working/}history/`.
