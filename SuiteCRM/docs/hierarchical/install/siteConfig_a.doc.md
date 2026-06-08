# Fichier : siteConfig_a.php

**Chemin :** `install/siteConfig_a.php`
**Type :** installer (vue wizard — etape 6a : configuration site)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Affiche le formulaire de configuration du site SuiteCRM : URL du site, nom du systeme, identifiants administrateur, et collation DB (en mode custom). C'est l'etape de configuration principale avant l'installation effective.

## Role technique
Template PHP generant une page HTML. Charge les valeurs depuis `config.php` (si existant) dans la session (theme, langue, charset, monnaie, etc.). En mode `custom` uniquement, affiche les champs URL et collation DB. Affiche toujours les champs admin username/password.

---

## Dependances cles
- **Imports principaux :**
  - `config.php` (racine) — parametres existants (ligne 51)
  - `install/installCommon.js`, `install/siteConfig.js` — JS formulaire
  - `themes/SuiteP/css/fontello.css`, `animation.css`
  - `getDbConnection()` — pour les options de collation (mode custom)
- **Variables de contexte :** `$mod_strings`, `$next_step`, `$sugar_md`, `$validation_errors`
- **Session :** `setup_site_url`, `setup_system_name`, `setup_site_admin_user_name`, `setup_site_admin_password`, `install_type`, `site_default_theme`, `default_language`, `default_currency_*`

## Exports / Symboles principaux
- Aucun export — affichage HTML uniquement

## Interactions
- **Appele par :** `install.php` (include, etape 6a)
- **Appelle :**
  - `getDbConnection()` — connexion DB pour collations
  - `get_select_options_with_id()` — generation dropdown collation
  - `install.php` (submit formulaire)

---

## Notes
- La garde `$install_script` est presente (ligne 47).
- En mode `typical`, l'URL et le nom systeme ne sont pas affichables (masques).
- Les erreurs de validation sont affichees en haut du formulaire (variable `$validation_errors`).
- Ce fichier est l'etape 6 sur 8 dans le wizard (LBL_STEP6, ligne 145).
