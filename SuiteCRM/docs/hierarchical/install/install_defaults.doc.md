# Fichier : install_defaults.php

**Chemin :** `install/install_defaults.php`
**Type :** configuration (valeurs par defaut installation)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Definit les valeurs par defaut de tous les parametres de session utilises pendant le wizard d'installation. Ce tableau sert de reference initiale pour peupler la session lors du demarrage du wizard.

## Role technique
Expose un tableau PHP `$installer_defaults` avec toutes les cles de configuration attendues par le wizard. Couvre : parametres de langue, licence, base de donnees, site, securite, monnaie, format, et parametres utilisateur DB.

---

## Dependances cles
- **Imports principaux :** aucun
- **Variables d'environnement :** aucune

## Exports / Symboles principaux

- `$installer_defaults` — tableau — valeurs par defaut de la session wizard

**Parametres cles inclus :**

| Cle | Valeur defaut | Description |
|---|---|---|
| `language` | `'en_us'` | Langue installateure |
| `setup_db_type` | `'mysql'` | Type de base de donnees |
| `setup_db_database_name` | `'suitecrm'` | Nom de la base |
| `setup_db_create_database` | `true` | Creer la base |
| `demoData` | `'no'` | Installer les donnees de demo |
| `setup_system_name` | `'SuiteCRM'` | Nom du systeme |
| `site_default_theme` | `'SuiteP'` | Theme par defaut |
| `default_language` | `'en_us'` | Langue par defaut |
| `default_currency_name` | `'US Dollars'` | Monnaie |
| `setup_site_log_level` | `'fatal'` | Niveau de log |
| `dbUSRData` | `'same'` | Mode utilisateur DB |

## Interactions
- **Appele par :** `install.php` (include pour initialiser la session)
- **Appelle :** rien

---

## Notes
- Ce fichier ne contient pas de garde `sugarEntry` — INCONNU si c'est intentionnel ou un oubli.
- L'option `strict_id_validation` est presente (defaut `false`) mais son role exact est INCONNU sans inspecter `install.php`.
- La langue d'installation (`language`) et la langue par defaut de l'application (`default_language`) sont deux parametres distincts.
