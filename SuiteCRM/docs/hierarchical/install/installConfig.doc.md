# Fichier : installConfig.php

**Chemin :** `install/installConfig.php`
**Type :** installer (vue wizard unifiee — configuration DB + site)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Page de configuration unifiee du wizard d'installation qui regroupe en une seule etape : le choix du driver DB, la configuration DB, les identifiants admin, les parametres de localisation (date, heure, fuseau, monnaie), les scenarios d'installation, le branding (logo), et les options avancees. C'est la version modernisee remplacant les etapes 5+6a+6b separees.

## Role technique
Expose trois classes :
- `NonDBLocalization` : extension de `Localization` pour formatter les options de nom sans acces DB.
- `InstallLayout` : classe de generation HTML modulaire avec methodes privees (`getHeader`, `getForm`, `getFormItems`, `getFormControlls`, `getFormScripts`, `getOutput`). La methode `show()` orchestre l'assemblage complet.
- `DisplayErrors` : utilitaire pour activer/desactiver le rapport d'erreurs PHP (usage debug uniquement).

Le formulaire inclut des sections accordeon pliables pour les options avancees (scenarios, branding, locale, securite, collation DB).

---

## Dependances cles
- **Imports principaux :**
  - `install/suite_install/scenarios.php` — scenarios d'installation (ligne 1643)
  - `install/suite_install/collations.php` — liste collations MySQL (ligne 864)
  - `SugarThemeRegistry::current()->getImageURL()` — logo courant
  - `DBManagerFactory::getDbDrivers()` — liste drivers DB disponibles
  - `TimeDate::getTimezoneList()`, `TimeDate::guessTimezone()` — fuseaux horaires
  - `get_sugar_config_defaults()` — valeurs par defaut de config
  - `getInstallDbInstance()` — instance DB courante
- **Classes exportees :** `NonDBLocalization`, `InstallLayout`, `DisplayErrors`
- **Session :** setup_db_*, setup_site_*, install_type, demoData, custom_session/log/guid options

## Exports / Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `NonDBLocalization` | classe | Localization sans DB pour les formats de noms |
| `InstallLayout` | classe | Generation complete de la page de configuration |
| `InstallLayout::show($data)` | methode | Affiche la page unifiee |
| `DisplayErrors::show()` | methode statique | Active E_ALL pour debug |
| `DisplayErrors::restore()` | methode statique | Restaure les parametres d'erreur |

## Interactions
- **Appele par :** `install.php` (include, etape unique de configuration)
- **Appelle :**
  - `install.php` (POST AJAX DB check, upload logo, storeConfig)
  - `install/suite_install/scenarios.php` — liste scenarios
  - `install/suite_install/collations.php` — collations

---

## Notes
- Fichier tres long (1692 lignes) : vue la plus complexe du wizard.
- La validation cote client (`getFormErrors()`) verifie email admin et URL du site (lignes 1155-1171).
- Le mecanisme `storeConfig` (ligne 1035) sauvegarde la config en session via AJAX avant la redirection.
- `startStatusReader()` interroge periodiquement `install/status.json` pour afficher la progression (ligne 1082).
- Le logo peut etre televerse via une iframe cachee (upload asynchrone, lignes 1018-1025).
- TODO identifies dans le code : Name Format, SMTP settings (commente).
