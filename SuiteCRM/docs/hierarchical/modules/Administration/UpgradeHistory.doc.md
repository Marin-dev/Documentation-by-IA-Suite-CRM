# UpgradeHistory.php

**Chemin :** `modules/Administration/UpgradeHistory.php`
**Type :** PHP (Model / SugarBean)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Modele ORM de l'historique des mises a jour et modules installes. Stocke dans la table `upgrade_history` chaque installation (patch, module, theme, langpack) avec son nom, version, MD5, statut et manifest serialise. Sert a verifier les dependances, detecter les conflits de fichiers et determiner si une desinstallation est possible.

## Role technique
Etend `SugarBean` avec `$table_name = "upgrade_history"`. Desactive la securite par ligne (`$disable_row_level_security = true`) et la visibilite du tracker. La methode `retrieve()` surcharge la parente pour ignorer le filtre `deleted` (la table n'a pas cette colonne). Inclut une logique de comparaison de version semver.

---

## Dependances cles
| Element | Role |
|---|---|
| `SugarBean` (parent) | ORM de base |
| `DBManager` (global via SugarBean) | Acces BDD |
| `$timedate` (global) | Conversion dates pour comparaisons |

## Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `UpgradeHistory` | Classe | Modele historique mises a jour |
| `getAll()` | Methode | Tous les enregistrements triees par date desc |
| `getAllOrderBy($orderBy)` | Methode | Tous les enregistrements avec tri specifique |
| `findByMd5($var_md5)` | Methode | Recherche par checksum MD5 |
| `checkForExisting($patch)` | Methode | Verifie si un paquet est deja installe (par id_name ou name) |
| `determineIfUpgrade($id_name, $version)` | Methode | Detecte si c'est une mise a jour d'un module existant |
| `UninstallAvailable($patch_list, $patch_to_check)` | Methode | Verifie si la desinstallation est possible (conflits de fichiers) |
| `foundConflict($check_path, $recent_path)` | Methode | Detection recursive de conflits de fichiers |
| `checkDependencies($dependencies)` | Methode | Verifie que toutes les dependances sont installees |
| `is_right_version_greater($left, $right)` | Methode | Comparaison semver recursive |
| `retrieve($id)` | Methode | Override : ignore le filtre `deleted` |

## Interactions
- **Appele par :** `UpgradeWizard.php`, `UpgradeWizardCommon.php`, `ModuleInstaller`, `DiagnosticRun.php` (dump upgrade_history)
- **Table BDD :** `upgrade_history` (sans colonne `deleted`)

---

## Notes
- L'absence de colonne `deleted` est un cas particulier pour SugarBean — la surcharge de `retrieve()` est critique (ligne 306-308).
- `UninstallAvailable()` utilise des chemins de fichiers backup (`-restore`) pour detecter les conflits — logique complexe basee sur le systeme de fichiers.
- `disable_row_level_security = true` et `tracker_visibility = false` — ce bean est invisible aux ACL.
