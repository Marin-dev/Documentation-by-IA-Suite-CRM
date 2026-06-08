# AdvancedOpenDiscovery.php

**Chemin :** `install/suite_install/AdvancedOpenDiscovery.php`
**Type :** `PHP (installeur — initialisation module AOD)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Initialise le module Advanced Open Discovery (AOD — moteur de recherche interne SuiteCRM) lors de l'installation. Désactive AOD par défaut dans la configuration et enregistre les logic hooks nécessaires au suivi des modifications.

**Type :** installer

---

## Dépendances clés
- `modules/Administration/Administration.php`
- `ModuleInstall/ModuleInstaller.php` — `check_logic_hook_file()`
- `$sugar_config` — tableau de configuration global

## Exports / Symboles principaux
- `install_aod()` — désactive AOD (`$sugar_config['aod']['enable_aod'] = false`), écrit `config.php`, appelle `installAODHooks()`
- `installAODHooks()` — enregistre 3 logic hooks globaux sur `after_save`, `after_delete`, `after_restore` pointant vers `AOD_LogicHooks`

## Interactions
- **Appelé par :** `install/suite_install/suite_install.php` (ligne 32)
- **Appelle :** `write_array_to_file()`, `check_logic_hook_file()`
- **Position dans le flux global :** étape d'initialisation des modules SuiteCRM après installation DB

---

## Notes
- AOD est désactivé par défaut à l'installation — l'admin doit l'activer manuellement dans la configuration.
- Les hooks sont globaux (module vide `''`) : s'appliquent à tous les modules.
