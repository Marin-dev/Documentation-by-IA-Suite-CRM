# Fichier : AdvancedOpenDiscovery.php

**Chemin :** `install/suite_install/AdvancedOpenDiscovery.php`
**Type :** installer (configuration module AOD)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Configure le module Advanced Open Discovery (AOD — moteur de recherche interne) en enregistrant le logic hook `after_restore` pour reindexer apres une restauration.

## Role technique
Expose une fonction (non nommee dans les lignes lues — probablement `install_aod()`). Enregistre un hook global (module vide) `after_restore` pour `AOD_Index/AOD_LogicHooks.php::saveModuleRestore`.

---

## Dependances cles
- **Imports principaux :** INCONNU (non visible)
- **Logic hooks :**
  - Module vide, hook `after_restore`, order 1 → `AOD_LogicHooks::saveModuleRestore`

## Exports / Symboles principaux
- Fonction d'installation AOD (nom INCONNU d'apres les lignes lues)

## Interactions
- **Appele par :** `install/suite_install/suite_install.php` (ligne 32)
- **Appelle :**
  - `check_logic_hook_file()` — enregistrement hook
  - `modules/AOD_Index/AOD_LogicHooks.php`

---

## Notes
- Le hook `after_restore` global (module='') se declenche apres toute restauration de module pour reindexer.
