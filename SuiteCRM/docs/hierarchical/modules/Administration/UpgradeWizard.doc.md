# UpgradeWizard.php

**Chemin :** `modules/Administration/UpgradeWizard.php`
**Type :** PHP (view / action complexe)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Interface de l'Assistant de Mise a Jour et du Chargeur de Modules. Permet d'uploader des fichiers ZIP (patches, modules, themes, langpacks), de les valider (manifest, scanner de securite), et de les mettre en file d'attente pour installation. Gere aussi la suppression de paquets en attente.

## Role technique
Script procedral inclus par d'autres fichiers (necessite `$view` et `$form_action` definis). Gere l'action `run=upload` : upload via form multipart OU copie depuis un repertoire commun (`use_common_ml_dir`). Valide avec `ModuleScanner::scanFile()` et `validate_manifest()`. Selon `$view` ('module' ou 'default'), filtre les types acceptes. Utilise `PackageManagerDisplay` pour l'affichage.

---

## Dependances cles
| Element | Role |
|---|---|
| `modules/Administration/UpgradeWizardCommon.php` | Fonctions communes (extractManifest, etc.) |
| `ModuleInstall/PackageManager/PackageManagerDisplay.php` | Rendu liste paquets |
| `ModuleInstall/ModuleScanner.php` | Scan securite du manifest |
| `UploadFile` | Gestion upload securise |
| `UpgradeHistory` | Verification MD5 deja installe |
| `PackageManager` | Telechargement depuis store (release_id) |

## Symboles principaux

| Fonction | Role |
|---|---|
| `unlinkTempFiles()` | Supprime les fichiers temporaires d'upload |

## Interactions
- **Inclus par :** `UpgradeWizardCommon.php` (qui l'inclut en definissant `$view`)
- **Appelle :** `ModuleScanner::lockConfig()`, `ModuleScanner::scanFile()`, `validate_manifest()`, `PackageManagerDisplay::buildPackageDisplay()`

---

## Notes
- Securite critique : `ModuleScanner::scanFile()` verifie que le manifest ne contient pas de copies de fichiers malicieuses (ligne 148).
- Securite : verifie que `upgrade_zip_escaped` est bien un `.zip` (lignes 115, 129) et rejette les chemins `phar://` (ligne 110).
- `SUGARCRM_MIN_UPLOAD_MAX_FILESIZE_BYTES = 6MB` : avertit si `upload_max_filesize` est insuffisant.
- Le code de listing des paquets disponibles est commente (lignes 279-360) — fonctionnalite desactivee.
