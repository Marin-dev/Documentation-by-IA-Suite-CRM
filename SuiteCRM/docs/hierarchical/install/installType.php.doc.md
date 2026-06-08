# installType.php

**Chemin :** `install/installType.php`
**Type :** `PHP (installeur — vue HTML choix type installation)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Affiche la page de sélection du type d'installation (Typical vs Custom) dans le wizard SuiteCRM. Affiche également un avertissement si la version PHP est en dessous de la version recommandée.

**Type :** installer (vue HTML)

---

## Dépendances clés
- `sugarEntry` + `$install_script` — protections
- `$mod_strings`, `$sugar_md`, `$next_step` — globaux wizard
- `$supportedLanguages`, `$current_language` — sélection de langue
- `get_language_header()`, `get_select_options_with_id()`, `check_php_version()` — fonctions utilitaires
- Constantes : `SUITECRM_PHP_REC_VERSION`, `SUITECRM_PHP_MIN_VERSION`, `PHP_VERSION`

## Exports / Symboles principaux
Aucun. Vue HTML pure.

## Interactions
- **Appelé par :** `install.php` (étape 3 du wizard)
- **Position dans le flux global :** après la vérification des prérequis et la licence, avant la configuration DB

---

## Notes
- `$_SESSION['install_type']` : `'Typical'` (défaut) ou `'custom'` — conditionne l'affichage de champs avancés dans les étapes suivantes.
- `check_php_version() === -1` : affiche un message d'avertissement PHP (non bloquant) si la version est en dessous de la recommandée.
- CSS : `themes/SuiteP/css/responsiveslides.css`, `themes.css`, `fontello.css`, `animation.css`.
- Indicateur de progression visuel : icônes `icon-progress-0` à `icon-progress-7` (étape 3 active).
