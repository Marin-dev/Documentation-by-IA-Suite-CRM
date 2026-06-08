# ListViewMerge.php

**Chemin :** `modules/UpgradeWizard/SugarMerge/ListViewMerge.php`
**Type :** PHP - Helper (fusion de métadonnées de liste)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Classe de fusion des métadonnées de ListView lors des mises à jour. Transforme les métadonnées de liste en format EditView pour la fusion, puis les re-transforme en format ListView. Utilise `$listViewDefs` au lieu de `$viewdefs`.

## Type
helper

## Dépendances clés
- `modules/UpgradeWizard/SugarMerge/EditViewMerge.php` — classe parente

## Exports / Symboles principaux
- `ListViewMerge` (classe, étend `EditViewMerge`)
  - `$varName` = `'listViewDefs'`

## Interactions
- **Appelé par :** `SugarMerge` lors de la fusion des layouts de liste
- **Appelle :** `EditViewMerge` (héritage)

## Notes
- Transforme les données listview en format editview pour réutiliser l'algorithme de fusion.
