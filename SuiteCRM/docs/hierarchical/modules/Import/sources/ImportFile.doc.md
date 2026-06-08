# ImportFile.php

**Chemin :** `modules/Import/sources/ImportFile.php`
**Type :** PHP - Model / Source
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Source de données d'import basée sur un fichier. Hérite de `ImportDataSource`. Gère la lecture ligne par ligne d'un fichier CSV importé, en s'appuyant sur `CsvAutoDetect` pour la détection automatique des paramètres.

## Type
model / source

## Dépendances clés
- `modules/Import/CsvAutoDetect.php`
- `modules/Import/sources/ImportDataSource.php` — classe parente abstraite

## Exports / Symboles principaux
- `ImportFile` (classe) — étend `ImportDataSource`
  - Propriété interne de suppression du fichier à la destruction

## Interactions
- **Appelé par :** `ImportController`, `Importer`
- **Appelle :** `CsvAutoDetect`

## Notes
- Implémente l'interface Iterator/source pour itération ligne par ligne.
