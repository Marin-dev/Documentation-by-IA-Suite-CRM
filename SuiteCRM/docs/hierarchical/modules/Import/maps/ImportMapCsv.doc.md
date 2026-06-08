# ImportMapCsv.php

**Chemin :** `modules/Import/maps/ImportMapCsv.php`
**Type :** PHP - Modèle (mapping d'import)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Classe de mapping minimal pour l'import de fichiers CSV standard. Hérite de `ImportMapOther` et se distingue uniquement par le délimiteur virgule et l'identifiant `'csv'`.

## Type
model

## Dépendances clés
- `modules/Import/maps/ImportMapOther.php` — classe parente

## Exports / Symboles principaux
- `ImportMapCsv` (classe, étend `ImportMapOther`)
  - `$name` = `'csv'`
  - `$delimiter` = `','`
  - `$enclosure` non défini (null)

## Interactions
- **Appelé par :** `ImportMap::getImportMap()` lors de la sélection du format CSV
- **Appelle :** `ImportMapOther` (héritage)

## Notes
- Classe très légère — uniquement la configuration de délimiteur. Tout le mapping est hérité.
