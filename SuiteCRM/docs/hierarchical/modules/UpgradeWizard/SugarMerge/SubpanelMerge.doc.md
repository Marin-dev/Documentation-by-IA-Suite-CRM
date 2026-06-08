# SubpanelMerge.php

**Chemin :** `modules/UpgradeWizard/SugarMerge/SubpanelMerge.php`
**Type :** PHP - Helper (fusion de métadonnées de sous-panneau)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Classe de fusion des métadonnées de sous-panneaux lors des mises à jour. Hérite de `ListViewMerge` car les sous-panneaux ont une structure mixte entre listview et editview.

## Type
helper

## Dépendances clés
- `modules/UpgradeWizard/SugarMerge/ListViewMerge.php` — classe parente

## Exports / Symboles principaux
- `SubpanelMerge` (classe, étend `ListViewMerge`)

## Interactions
- **Appelé par :** `SugarMerge` lors de la fusion des layouts de sous-panneaux
- **Appelle :** `ListViewMerge` (héritage)
