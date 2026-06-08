# Fichier : license.php

**Chemin :** `install/license.php`
**Type :** installer (vue wizard — etape 2 alternative)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Affiche la page d'acceptation de la licence AGPL dans le wizard d'installation (variante utilisee apres rechargement avec SuiteCRM deja installe ou en mode mise a jour). Similaire a `welcome.php` mais avec une mise en page differente et une progression en etapes visuelles.

## Role technique
Template PHP generant une page HTML complete avec textarea de licence, checkbox d'acceptation, et verification AJAX via YAHOO.util.Connect. Utilise les variables de session pour persister l'etat d'acceptation. Charge le JS YUI depuis le cache (sugar_grp1_yui.js).

---

## Dependances cles
- **Imports principaux :**
  - `install/install_utils.php` — `getLicenseContents()`, `get_language_header()` (ligne 56)
  - `cache/include/javascript/sugar_grp1_yui.js` — YUI (depuis cache)
  - `install/license.js` — JS d'activation bouton Next
  - `themes/SuiteP/css/fontello.css`, `animation.css` — icones et animations
- **Variables de contexte :** `$mod_strings`, `$current_language`, `$next_step`, `$sugar_md`, `$sugar_version`, `$js_custom_version`
- **Session :** `$_SESSION['setup_license_accept']`, `$_SESSION['license_submitted']`

## Exports / Symboles principaux
- Aucun export — affichage HTML uniquement

## Interactions
- **Appele par :** `install.php` (include)
- **Appelle :**
  - `install/install_utils.php::getLicenseContents()`
  - `install.php` (POST AJAX `checkInstallSystem=true`)
  - `install.php?page=licensePrint` (ouverture fenetre impression)

---

## Notes
- Difference avec `welcome.php` : pas de slideshow, barre de progression en etapes (LBL_STEP2), chargement JS depuis cache.
- Commentaire ligne 1 : garde `sugarEntry` deliberement commentee.
- La garde `$install_script` est presente (ligne 45).
