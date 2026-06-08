# installConfig.php

**Chemin :** `install/installConfig.php`
**Type :** `PHP (installeur — vue HTML configuration combinée)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Fichier central du wizard d'installation nouvelle génération. Regroupe en une seule page la configuration DB, la configuration du site (admin, URL, email), les options de démo, la sélection de scénarios, le branding (logo) et les paramètres régionaux. Contient les classes `InstallLayout`, `NonDBLocalization` et `DisplayErrors`.

**Type :** installer (vue HTML)

---

## Dépendances clés
- `sugarEntry` + `$install_script` — protections d'accès
- `$mod_strings`, `$sugar_version`, `$js_custom_version`, `$sugar_md`, `$next_step` — globaux wizard
- `$app_list_strings`, `$sugarConfigDefaults`, `$drivers`, `$checked`, `$supportedLanguages`, `$current_language` — data wizard
- `getInstallDbInstance()`, `DBManagerFactory::getDbDrivers()` — drivers DB
- `SugarThemeRegistry::current()->getImageURL()` — logo courant
- `TimeDate` — formats date/heure et timezone
- `install/suite_install/collations.php` — liste de collations MySQL
- `install/suite_install/scenarios.php` — scénarios d'installation
- `Localization` — classe parente de `NonDBLocalization`

## Exports / Symboles principaux
- `NonDBLocalization` — sous-classe de `Localization` : génère des options de format de nom sans accès DB
  - `getUsableLocaleNameOptions(array $options) : array`
- `InstallLayout` — classe principale de rendu
  - `show($data = null)` — méthode publique, point d'entrée unique, orchestre tout le rendu HTML
  - Méthodes privées : `getHeader()`, `getHeaderStyles()`, `getHeaderScripts()`, `getForm()`, `getFormItems()`, `getFormControlls()`, `getFormScripts()`, `getOutput()`, `getSelect()`
- `DisplayErrors` — utilitaire de debug
  - `DisplayErrors::show()` / `DisplayErrors::restore()` — active/restaure `display_errors` et `error_reporting`

## Interactions
- **Appelé par :** `install.php` (étape 2 du nouveau wizard)
- **Appelle AJAX :** `install.php?checkDBSettings=true` (POST), `install.php?storeConfig=1` (POST), `install.php?uploadLogo=1` (iframe)
- **Lit :** `install/status.json` via polling JSON pour afficher la progression
- **Position dans le flux global :** étape principale du wizard (DB + site en une seule page)

---

## Notes
- `storeConfig` : sauvegarde de la configuration en session avant soumission — permet un retour en arrière sans perte.
- `startStatusReader()` : polling toutes les 1200ms sur `install/status.json` pour mise à jour de la barre de progression.
- `onNextClick()` : validation client avant soumission (email et URL requis), puis appel `callDBCheck()` → `dbCheckPassed()` → soumission du formulaire.
- Gestion complexe du logo : upload via iframe (`upload_target`), callback JavaScript `uploadLogoCallback`.
- `DisplayErrors::show()` est commenté — ne pas décommenter en production.
- `$_SESSION = array_merge($_SESSION, $_POST)` (ligne 1677) : fusion de session pour pré-remplissage du formulaire.
