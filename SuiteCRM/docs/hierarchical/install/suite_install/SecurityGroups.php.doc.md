# SecurityGroups.php

**Chemin :** `install/suite_install/SecurityGroups.php`
**Type :** `PHP (installeur — initialisation groupes de sécurité)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Initialise le module SecuritySuite (groupes de sécurité) lors de l'installation. Configure les paramètres par défaut de contrôle d'accès par groupe si ce n'est pas déjà fait.

**Type :** installer

---

## Dépendances clés
- `sugar_version.php`, `modules/Administration/Administration.php`
- `$sugar_config` — tableau de configuration global

## Exports / Symboles principaux
- `install_ss()` — initialise les clés de config `securitysuite_*` si absentes :

| Paramètre | Valeur par défaut |
|---|---|
| `securitysuite_additive` | `true` |
| `securitysuite_user_role_precedence` | `true` |
| `securitysuite_user_popup` | `true` |
| `securitysuite_popup_select` | `false` |
| `securitysuite_inherit_creator` | `true` |
| `securitysuite_inherit_parent` | `true` |
| `securitysuite_inherit_assigned` | `true` |
| `securitysuite_strict_rights` | `false` (puis `true` si absent) |
| `securitysuite_filter_user_list` | `false` |

## Interactions
- **Appelé par :** `install/suite_install/suite_install.php` (ligne 47-48)
- **Appelle :** (probablement `write_array_to_file()` — commenté dans le code)
- **Position dans le flux global :** configuration des droits d'accès par groupe de sécurité

---

## Notes
- Les appels `write_array_to_file()` sont commentés — la configuration n'est pas immédiatement écrite dans `config.php` depuis ce fichier (probablement écrite en batch à la fin de `suite_install.php`).
- `securitysuite_strict_rights` : incohérence — première initialisation à `false`, deuxième (si absent) à `true` (lignes 28 et 37).
- `$GLOBALS['sugar_config']['addAjaxBannedModules']` — suite du fichier tronquée, logique partielle.
