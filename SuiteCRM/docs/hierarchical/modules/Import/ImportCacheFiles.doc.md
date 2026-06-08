# ImportCacheFiles.php

**Chemin :** `modules/Import/ImportCacheFiles.php`
**Type :** PHP - Helper
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Classe statique fournissant les noms des fichiers cache utilisés pendant l'import (fichier de divers, de doublons, etc.). Centralise la gestion des chemins de cache pour l'ensemble du processus d'import.

## Type
helper / utilitaire

## Dépendances clés
- Aucune (classe statique auto-suffisante)

## Exports / Symboles principaux
- `ImportCacheFiles` (classe statique)
  - Constantes : `FILE_MISCELLANEOUS` (`'misc'`), `FILE_DUPLICATES` (`'dupes'`), et autres (INCONNU)

## Interactions
- **Appelé par :** `Importer`, vues d'import

## Notes
- Classe utilitaire sans état.
