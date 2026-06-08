# UpgradeWizard_commit.php

**Chemin :** `modules/Administration/UpgradeWizard_commit.php`
**Type :** PHP (action / upgrade)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Phase de validation/commit de l'assistant de mise a jour. Execute les scripts de rebuild post-installation (extensions, BDD, etc.) via `UWrebuild()`.

## Role technique
Inclut `UpgradeWizardCommon.php` et `Configurator.php`. Definit `UWrebuild()` qui appelle les operations de reconstruction post-upgrade.

---

## Dependances cles
| Element | Role |
|---|---|
| `modules/Administration/UpgradeWizardCommon.php` | Fonctions communes upgrade |
| `modules/Configurator/Configurator.php` | Configuration |

## Interactions
- **Appele par :** `UpgradeWizardCommon.php` pendant le processus d'upgrade
