# UpgradeWizardCommon.php

**Chemin :** `modules/Administration/UpgradeWizardCommon.php`
**Type :** PHP (helper / utilitaires upgrade)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Bibliotheque de fonctions communes pour l'assistant de mise a jour et le chargeur de modules. Gere la validation des vues (module vs default), les limites d'upload, et les operations communes du processus d'upgrade.

## Role technique
Verifie `$_REQUEST['view']` (accepte 'default' ou 'module'), augmente `max_execution_time` a 3600s. Inclut les utilitaires DB et ZIP. Definit `$view` et `$form_action` utilises par `UpgradeWizard.php`.

---

## Dependances cles
| Element | Role |
|---|---|
| `include/utils/db_utils.php` | Utilitaires BDD |
| `include/utils/php_zip_utils.php` | Utilitaires ZIP |

## Interactions
- **Inclus par :** `UpgradeWizard.php`, `UpgradeWizard_prepare.php`, `UpgradeWizard_commit.php`
- **Definit :** `$view`, `$form_action`, `$base_upgrade_dir`, `$base_tmp_upgrade_dir`, `$GLOBALS['subdirs']`
