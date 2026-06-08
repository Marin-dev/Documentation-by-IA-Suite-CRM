# Fichier : suite_install.php

**Chemin :** `install/suite_install/suite_install.php`
**Type :** installer (orchestrateur modules SuiteCRM)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Orchestre l'installation de tous les modules specifiques a SuiteCRM (au-dela du core SugarCRM). Appelle chaque module d'installation pour configurer les fonctionnalites avancees de SuiteCRM et lance le Repair and Clear final.

## Role technique
Script d'orchestration sans classe propre. Charge la configuration version, ecrit dans `config.php`, puis inclut et appelle sequentiellement les fonctions d'installation de chaque module SuiteCRM. Se termine par un `RepairAndClear` complet.

---

## Dependances cles
- **Imports principaux :**
  - `sugar_version.php`, `suitecrm_version.php` — versions
  - `modules/Administration/updater_utils.php` — `set_CheckUpdates_config_setting()`
  - `modules/Administration/QuickRepairAndRebuild.php` — `RepairAndClear`
  - `install/suite_install/AdvancedOpenSales.php` — `install_aos()`
  - `install/suite_install/AdvancedOpenPortal.php` — `install_aop()`
  - `install/suite_install/AdvancedOpenDiscovery.php` — `install_aod()`
  - `install/suite_install/AdvancedOpenEvents.php` — `install_aoe()`
  - `install/suite_install/Search.php` — `install_search()`, `install_es()`
  - `install/suite_install/Projects.php` — `install_projects()`
  - `install/suite_install/Reschedule.php` — `install_reschedule()`
  - `install/suite_install/SecurityGroups.php` — `install_ss()`
  - `install/suite_install/GoogleMaps.php` — `install_gmaps()`
  - `install/suite_install/CalendarSync.php` — `install_calendar_sync_hooks()`
  - `install/suite_install/Social.php` — `install_social()`
  - `install/suite_install/SystemEmailTemplates.php` — `installSystemEmailTemplates()`, `setSystemEmailTemplatesDefaultConfig()`

## Exports / Symboles principaux
- Aucun export — execution directe

## Interactions
- **Appele par :** `install/performSetup.php` (INCONNU : verifier l'appel exact)
- **Appelle :** toutes les fonctions `install_*` listees ci-dessus + `RepairAndClear`

---

## Notes
- Configuration globale appliquee : `default_max_tabs=10`, `sugarbeet=false`, `enable_action_menu=true`, `search.controller='UnifiedSearch'`, `imap_test=false`.
- Le `RepairAndClear` final avec `clearAll` garantit que les caches et extensions sont rebuildes apres l'installation.
- `write_array_to_file()` ecrit la `$sugar_config` dans `config.php` (ligne 19).
