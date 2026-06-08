# Fichier : welcome.php

**Chemin :** `install/welcome.php`
**Type :** installer (vue wizard — etape 1)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Affiche la premiere etape du wizard d'installation de SuiteCRM : page d'accueil avec acceptation de la licence AGPL, slideshow de captures d'ecran du produit, et selection de la langue. Lance egalement une verification systeme via AJAX avant de passer a l'etape suivante.

## Role technique
Template PHP qui genere une page HTML complete. Charge les groupes JS YUI depuis `JSGroupings.php` pour le lancement du check systeme AJAX (`callSysCheck()`). Utilise `get_boolean_from_request()` pour lire l'etat de la checkbox de licence. Gère la redirection via YAHOO.util.Connect.asyncRequest vers `install.php`.

---

## Dependances cles
- **Imports principaux :**
  - `jssource/JSGroupings.php` — groupes JS YUI (ligne 70)
  - `install/install_utils.php` — `getLicenseContents()`, `get_language_header()` (ligne 64)
  - `themes/SuiteP/css/responsiveslides.css`, `themes.css`, `fontello.css`, `animation.css` — styles
  - `install/license.js` — fonctions JS d'acceptation licence
- **Variables de contexte (depuis install.php) :** `$mod_strings`, `$current_language`, `$supportedLanguages`, `$next_step`, `$setup_sugar_version`, `$sugar_md`
- **Session :** `$_SESSION['setup_license_accept']`, `$_SESSION['license_submitted']`

## Exports / Symboles principaux
- Aucun export — affichage HTML uniquement

## Interactions
- **Appele par :** `install.php` (via include avec `$install_script = true`)
- **Appelle :**
  - `install/install_utils.php::getLicenseContents()`
  - `install/install_utils.php::get_language_header()`
  - `install.php` (POST AJAX pour `checkInstallSystem=true`)

---

## Notes
- Verif. de version PHP : si `check_php_version() === -1`, la page de warning PHP est affichee a la place (ligne 334).
- La garde `$install_script` empeche l'acces direct (ligne 44).
- Le slideshow utilise responsiveSlides.js avec 4 screenshots SuiteCRM (ligne 126-129).
- La fonction `callSysCheck()` lance un check AJAX avant de passer a l'etape suivante.
