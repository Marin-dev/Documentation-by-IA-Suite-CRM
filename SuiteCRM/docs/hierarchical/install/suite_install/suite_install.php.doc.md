# suite_install.php

**Chemin :** `install/suite_install/suite_install.php`
**Type :** `PHP (installeur — orchestrateur des modules SuiteCRM)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Orchestrateur central de l'initialisation de tous les modules spécifiques à SuiteCRM lors de l'installation. Configure les paramètres globaux (version, tabs, search engine, IMAP), puis appelle successivement les fonctions d'installation de chaque module SuiteCRM, et termine par un Repair & Clear All.

**Type :** installer

---

## Dépendances clés
- `sugar_version.php`, `suitecrm_version.php`
- `$sugar_config` — tableau de configuration global
- `write_array_to_file()` — écriture `config.php`
- `modules/Administration/updater_utils.php` — `set_CheckUpdates_config_setting()`
- `modules/Administration/QuickRepairAndRebuild.php` — `RepairAndClear`
- Tous les fichiers du dossier `install/suite_install/` (voir liste ci-dessous)

## Exports / Symboles principaux
Aucune fonction ni classe exportée. Logique procédurale séquentielle.

## Séquence d'exécution
1. Configuration globale : version, tabs max (10), sugarbeet (false), action menu, search engine, IMAP test
2. `install_aos()` — AOS (ventes)
3. `install_aop()` — AOP (portail)
4. `install_aod()` — AOD (recherche interne)
5. `install_aoe()` — AOE (événements)
6. `install_search()` + `install_es()` — moteur de recherche
7. `install_projects()` — Projets
8. `install_reschedule()` — Reschedule
9. `install_ss()` — SecurityGroups
10. `install_gmaps()` — Google Maps
11. `install_calendar_sync_hooks()` — synchronisation calendrier
12. `install_social()` — Social
13. `installSystemEmailTemplates()` + `setSystemEmailTemplatesDefaultConfig()` — templates email
14. `RepairAndClear::repairAndClearAll(['clearAll'])` — nettoyage des caches

## Interactions
- **Appelé par :** `install/performSetup.php` (INCONNU : inclusion directe)
- **Position dans le flux global :** exécution finale après la création de la BDD et des tables — configure l'application SuiteCRM

---

## Notes
- `set_CheckUpdates_config_setting('manual')` : vérification des mises à jour en mode manuel par défaut.
- `$sugar_config['imap_test'] = false` : désactive le test IMAP automatique.
- `$sugar_config['default_max_tabs'] = 10` : nombre maximum d'onglets dans la barre de navigation.
- Le `repairAndClearAll(['clearAll'])` final est crucial pour que tous les caches soient cohérents après l'installation.
