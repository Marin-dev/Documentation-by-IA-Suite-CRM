# old_php.php

**Chemin :** `install/old_php.php`
**Type :** `PHP (installeur — vue HTML avertissement PHP obsolète)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Affiche une page d'avertissement lorsque la version PHP détectée est inférieure à la version minimale recommandée pour SuiteCRM. L'utilisateur peut tout de même continuer en cochant une case de confirmation.

**Type :** installer (vue HTML)

---

## Dépendances clés
- `$install_script`, `$mod_strings`, `$sugar_md`, `$next_step` — globaux wizard
- `$supportedLanguages`, `$current_language` — sélection de langue
- `jssource/JSGroupings.php` — pour charger les scripts YUI dynamiquement (ligne 58)
- Constantes : `SUITECRM_PHP_REC_VERSION`, `SUITECRM_PHP_MIN_VERSION`, `PHP_VERSION`
- `get_language_header()`, `get_select_options_with_id()`
- CSS : `themes/SuiteP/css/themes.css`, `fontello.css`, `animation.css`
- `install/old_php.js` — logique JS `toggleNextButton()`, `toggleOldPHP()`

## Exports / Symboles principaux
Aucun. Vue HTML procédurale.

## Interactions
- **Appelé par :** `install.php` quand `check_php_version()` retourne une version non recommandée
- **Position dans le flux global :** étape intermédiaire avant la licence, si PHP < version recommandée

---

## Notes
- `$_SESSION['setup_old_php']` stocke le choix de l'utilisateur.
- La case cochée active le bouton "Suivant" (`toggleNextButton()` en JS).
- Le changement de langue remet à zéro la navigation (`$("input[name=current_step]").attr('name', '_current_step')`) pour forcer un rechargement sans avancer.
