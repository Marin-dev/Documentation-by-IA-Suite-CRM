# ImportDataSource.php

**Chemin :** `modules/Import/sources/ImportDataSource.php`
**Type :** PHP - Modèle (classe abstraite)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Classe abstraite définissant l'interface commune pour toutes les sources de données d'import. Implémente `Iterator` pour permettre l'itération sur les lignes de données. Gère l'offset et le comptage des lignes traitées. Base pour `ImportFile` et `ExternalSourceEAPMAdapter`.

## Type
model (abstract)

## Dépendances clés
- `modules/Import/ImportCacheFiles.php` — gestion du cache d'import
- Interface PHP `Iterator`

## Exports / Symboles principaux
- `ImportDataSource` (classe abstraite, implémente `Iterator`)
  - `$_offset` — offset courant dans le jeu de données
  - Méthodes Iterator : `current()`, `next()`, `key()`, `valid()`, `rewind()` — à implémenter dans les sous-classes

## Interactions
- **Appelé par :** `Importer` (via `ImportFile` ou `ExternalSourceEAPMAdapter`)
- **Appelle :** `ImportCacheFiles`

## Notes
- Pattern Iterator : permet de parcourir les données d'import ligne par ligne comme un tableau.
- Les sous-classes doivent implémenter toutes les méthodes de l'interface `Iterator`.
