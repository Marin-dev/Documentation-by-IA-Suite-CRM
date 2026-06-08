# welcome.php

**Chemin :** `install/welcome.php`
**Type :** `PHP (installeur — vue HTML page d'accueil)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Affiche la première page du wizard d'installation (étape d'accueil / acceptation de licence). Présente le sélecteur de langue, le texte de licence, et la case d'acceptation requise pour passer à l'étape suivante. Gère l'état de la session de licence.

**Type :** installer (vue HTML)

---

## Dépendances clés
- `sugarEntry` + `$install_script` — protections
- `$mod_strings`, `$sugar_md`, `$next_step`, `$setup_sugar_version` — globaux wizard
- `$supportedLanguages`, `$current_language` — sélection de langue
- `get_language_header()`, `get_select_options_with_id()`
- `$_SESSION['setup_license_accept']`, `$_SESSION['license_submitted']`

## Exports / Symboles principaux
Aucun. Vue HTML procédurale.

## Interactions
- **Appelé par :** `install.php` (étape d'accueil / licence initiale)
- **Position dans le flux global :** étape 1 du wizard (première page affichée)

---

## Notes
- `$_SESSION['setup_license_accept']` est mis à `true`/`false` selon la case cochée.
- Le changement de langue recharge la page sans progresser dans le wizard (comportement identique à `old_php.php`).
- `$_SESSION['license_submitted'] = true` : une fois soumis, l'état est mémorisé pour pré-cocher la case si l'utilisateur revient.
- Différent de `license.php` qui affiche la page de licence intermédiaire — `welcome.php` est la toute première page.
