# SearchMerge.php

**Chemin :** `modules/UpgradeWizard/SugarMerge/SearchMerge.php`
**Type :** PHP - Helper (fusion de métadonnées de recherche)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Classe de fusion des métadonnées de formulaires de recherche lors des mises à jour. Utilise `$searchdefs['Search']` et hérite de `ListViewMerge` car les searchdefs ont une structure similaire aux listviewdefs.

## Type
helper

## Dépendances clés
- `modules/UpgradeWizard/SugarMerge/ListViewMerge.php` — classe parente

## Exports / Symboles principaux
- `SearchMerge` (classe, étend `ListViewMerge`)
  - `$varName` = `'searchdefs'`
  - `$viewDefs` = `'Search'`

## Interactions
- **Appelé par :** `SugarMerge` lors de la fusion des formulaires de recherche
- **Appelle :** `ListViewMerge` (héritage)
