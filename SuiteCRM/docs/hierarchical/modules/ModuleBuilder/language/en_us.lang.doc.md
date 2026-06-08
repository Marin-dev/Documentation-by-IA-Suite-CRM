# en_us.lang.php

**Chemin :** `modules/ModuleBuilder/language/en_us.lang.php`
**Type :** PHP (config / fichier de langue)
**Dernière mise à jour doc :** 2026-05-31

---

## Ce que ce fichier configure
Fichier de langue anglais (en_us) pour le module ModuleBuilder. Définit `$mod_strings` avec tous les libellés de l'interface Studio/ModuleBuilder utilisés par les vues et le contrôleur (LBL_STUDIO, LBL_MODULEBUILDER, LBL_DROPDOWNEDITOR, LBL_FIELDS, LBL_LABELS, LBL_RELATIONSHIPS, LBL_LAYOUTS, LBL_SUBPANELS, etc.).

## Rôle
config

## Paramètres clés
Les labels importants incluent (non exhaustif) :
- Sections : `LBL_STUDIO`, `LBL_MODULEBUILDER`, `LBL_DROPDOWNEDITOR`
- Navigation : `LBL_FIELDS`, `LBL_LABELS`, `LBL_RELATIONSHIPS`, `LBL_LAYOUTS`, `LBL_SUBPANELS`
- Actions : `LBL_SAVE`, `LBL_CANCEL`, `LBL_DELETE`, `LBL_DEPLOY`
- Export custom : `LBL_EC_CUSTOMFIELD`, `LBL_EC_CUSTOMLAYOUT`, `LBL_EC_NOCUSTOM`, etc.

## Impacte
- Consommé par `$mod_strings` global dans toutes les vues et le contrôleur ModuleBuilder
- Référencé par `ModuleBuilderController::getModuleTitle()` (`LBL_STUDIO`, `LBL_MODULEBUILDER`, etc.)
- Référencé par `MBLanguage::save()` pour les labels requis (`LBL_LIST`, `LBL_VIEW`, etc.)

## Notes
Fichier standard SugarCRM — chargé automatiquement par le framework lors du traitement d'une requête `module=ModuleBuilder`.
