# QuickCreateMerge.php

**Chemin :** `modules/UpgradeWizard/SugarMerge/QuickCreateMerge.php`
**Type :** PHP - Helper (fusion de métadonnées)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Classe de fusion des métadonnées de vues QuickCreate lors des mises à jour. Identique à `EditViewMerge` avec `$viewDefs = 'QuickCreate'`.

## Type
helper

## Dépendances clés
- `modules/UpgradeWizard/SugarMerge/EditViewMerge.php` — classe parente

## Exports / Symboles principaux
- `QuickCreateMerge` (classe, étend `EditViewMerge`)
  - `$viewDefs` = `'QuickCreate'`

## Interactions
- **Appelé par :** `SugarMerge` lors de la fusion des formulaires de création rapide
- **Appelle :** `EditViewMerge` (héritage)
