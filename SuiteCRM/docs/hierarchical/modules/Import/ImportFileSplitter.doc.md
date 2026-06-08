# ImportFileSplitter.php

**Chemin :** `modules/Import/ImportFileSplitter.php`
**Type :** PHP - Service
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Découpe un fichier CSV source en plusieurs sous-fichiers lorsque le nombre de lignes dépasse un seuil configurable (`$_recordThreshold`). Permet le traitement par lots lors des imports volumineux.

## Type
service / helper

## Dépendances clés
- Fonctions fichier PHP (fopen, fread, etc.)

## Exports / Symboles principaux
- `ImportFileSplitter` (classe)
  - `$_sourceFile` — chemin du fichier source
  - `$_fileCount` — nombre de fichiers créés
  - `$_recordCount` — nombre total d'enregistrements
  - `$_recordThreshold` — seuil de découpe

## Interactions
- **Appelé par :** logique d'import (étape de préparation)

## Notes
- Fichier lu partiellement (80 lignes). Le comportement exact de la découpe est INCONNU sans lecture complète.
