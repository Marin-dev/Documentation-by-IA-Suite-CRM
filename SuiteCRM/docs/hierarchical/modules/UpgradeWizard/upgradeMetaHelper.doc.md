# upgradeMetaHelper.php

**Chemin :** `modules/UpgradeWizard/upgradeMetaHelper.php`
**Type :** PHP - Helper (fusion des métadonnées lors de mise à jour)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Classe orchestrant la fusion des métadonnées de vues lors des mises à jour SuiteCRM. Gère les répertoires source/destination, détecte les modules modifiés par l'utilisateur, et coordonne les parsers EditView/DetailView pour la fusion.

## Type
helper

## Dépendances clés
- `include/utils/sugar_file_utils.php` — utilitaires de fichiers
- `$upgrade_dir`, `$source_dir`, `$dest_dir` — répertoires de travail
- `$evparser`, `$dvparser` — parsers EditView et DetailView

## Exports / Symboles principaux
- `UpgradeMetaHelper` (classe)
  - `$upgrade_dir`, `$source_dir`, `$dest_dir`, `$debug_mode`
  - `$upgrade_modules`, `$customized_modules`
  - `$path_to_master_copy`
  - Constructeur : `__construct($dir, $masterCopyDirectory, $debugMode = false)`

## Interactions
- **Appelé par :** scripts de mise à jour (`silentUpgrade_step2.php`, `commit.php`)
- **Appelle :** `SugarMerge` (EditViewMerge, DetailViewMerge, etc.)

## Notes
- Détecte les modules dont les layouts ont été personnalisés par l'utilisateur (`$customized_modules`).
