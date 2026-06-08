# Fichier : SecurityGroups.php

**Chemin :** `install/suite_install/SecurityGroups.php`
**Type :** installer (configuration module SecurityGroups)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Configure les groupes de securite (SecurityGroups) de SuiteCRM lors de l'installation initiale, en initialisant les parametres par defaut du systeme de controle d'acces base sur les groupes.

## Role technique
Fonction `install_ss()` qui verifie si les parametres SecurityGroups existent deja dans `$sugar_config` avant de les initialiser (protection contre la double installation).

---

## Dependances cles
- **Imports principaux :**
  - `sugar_version.php`
  - `modules/Administration/Administration.php`
  - `$sugar_config` (global)

## Exports / Symboles principaux
| Symbole | Role |
|---|---|
| `install_ss()` | Configure les parametres par defaut de SecurityGroups |

**Parametres initialises :**
- `securitysuite_additive = true`
- `securitysuite_user_role_precedence = true`
- `securitysuite_user_popup = true`
- `securitysuite_popup_select = false`
- `securitysuite_inherit_creator = true`
- `securitysuite_inherit_parent = true`
- `securitysuite_inherit_assigned = true`
- `securitysuite_strict_rights = false`

## Interactions
- **Appele par :** `install/suite_install/suite_install.php` (ligne 48)
- **Appelle :** `write_array_to_file()` (INCONNU : verifier si appele ici)

---

## Notes
- La garde `if (!array_key_exists('securitysuite_additive', $sugar_config))` (ligne 12) empeche l'ecrasement lors d'un upgrade.
- `securitysuite_additive = true` signifie que les droits sont additifs (union des droits de tous les groupes).
