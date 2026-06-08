# SugarMerge.php

**Chemin :** `modules/UpgradeWizard/SugarMerge/SugarMerge.php`
**Type :** PHP - Service
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Classe orchestrant la fusion des métadonnées de vues (EditView, DetailView, ListView, SearchView, QuickCreate) lors d'une mise à niveau. Préserve les customisations utilisateur tout en intégrant les nouvelles définitions du patch.

## Type
service

## Dépendances clés
- `modules/UpgradeWizard/SugarMerge/EditViewMerge.php`
- `modules/UpgradeWizard/SugarMerge/DetailViewMerge.php`
- `modules/UpgradeWizard/SugarMerge/SearchMerge.php`
- `modules/UpgradeWizard/SugarMerge/ListViewMerge.php`
- `modules/UpgradeWizard/SugarMerge/QuickCreateMerge.php`
- `modules/ModuleBuilder/parsers/views/History.php`

## Exports / Symboles principaux
- `SugarMerge` (classe)
  - Méthodes de fusion par type de vue (INCONNU — lecture partielle)

## Interactions
- **Appelé par :** `commit.php`, scripts d'upgrade
- **Appelle :** `EditViewMerge`, `DetailViewMerge`, `SearchMerge`, `ListViewMerge`, `QuickCreateMerge`

## Notes
- Critique pour les upgrades : préserve les personnalisations Studio.
