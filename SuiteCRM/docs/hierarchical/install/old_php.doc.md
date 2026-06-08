# Fichier : old_php.php

**Chemin :** `install/old_php.php`
**Type :** installer (vue wizard — avertissement version PHP)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Affiche une page d'avertissement dans le wizard si la version PHP detectee est inferieure a la version recommandee mais superieure a la version minimale. Permet a l'utilisateur de reconnaitre l'avertissement et de continuer malgre tout.

## Role technique
Template PHP generant une page HTML avec un message d'avertissement (format sprintf avec versions PHP recommandee, minimale et courante), une checkbox de confirmation, et un bouton Suivant desactive jusqu'a cochage. Charge les JS YUI depuis `JSGroupings.php`.

---

## Dependances cles
- **Imports principaux :**
  - `jssource/JSGroupings.php` — groupes JS YUI (ligne 58)
  - `install/old_php.js` — JS gestion toggle checkbox
  - `themes/SuiteP/css/themes.css`, `fontello.css`, `animation.css`
- **Constantes :** `SUITECRM_PHP_REC_VERSION`, `SUITECRM_PHP_MIN_VERSION`, `PHP_VERSION`
- **Variables de contexte :** `$mod_strings`, `$supportedLanguages`, `$current_language`, `$next_step`, `$setup_sugar_version`, `$sugar_md`
- **Session :** `$_SESSION['setup_old_php']`
- **Gardes :** `sugarEntry` + `$install_script`

## Exports / Symboles principaux
- Aucun export — affichage HTML uniquement

## Interactions
- **Appele par :** `install.php` (include, si PHP entre min et recommande)
- **Appelle :** `install.php` (submit formulaire)

---

## Notes
- Le bouton "Suivant" est desactive par defaut (JavaScript `toggleNextButton()`).
- La selection de langue (dropdown `onLangSelect`) recharge la page sans perdre l'etape.
- Similaire a `welcome.php` dans sa structure mais specialise pour le cas PHP desuet.
