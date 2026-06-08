# ImportMapTab.php

**Chemin :** `modules/Import/maps/ImportMapTab.php`
**Type :** PHP - Modèle (mapping d'import)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Classe de mapping pour l'import de fichiers TSV (Tab-Separated Values). Hérite de `ImportMapOther` avec délimiteur tabulation `\t`.

## Type
model

## Dépendances clés
- `modules/Import/maps/ImportMapOther.php` — classe parente

## Exports / Symboles principaux
- `ImportMapTab` (classe, étend `ImportMapOther`)
  - `$name` = `'tab'`
  - `$delimiter` = `"\t"`
  - `$enclosure` non défini

## Interactions
- **Appelé par :** `ImportMap::getImportMap()` lors de la sélection du format Tab
- **Appelle :** `ImportMapOther` (héritage)

## Notes
- Classe minimale — uniquement la configuration du délimiteur tabulation.
