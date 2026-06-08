# license.php

**Chemin :** `install/license.php`
**Type :** `PHP (installeur — vue HTML licence)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Affiche la page de licence AGPL du wizard d'installation. L'utilisateur doit cocher la case d'acceptation pour pouvoir passer à l'étape suivante. Lit le contenu de `LICENSE.txt` et le présente dans la page.

**Type :** installer (vue HTML)

---

## Dépendances clés
- `$install_script` — protection d'accès (pas de guard `sugarEntry` commenté ligne 2)
- `$mod_strings`, `$sugar_version`, `$js_custom_version`, `$sugar_md`, `$next_step` — globaux wizard
- `install/install_utils.php` — `getLicenseContents()`
- `get_language_header()` — entête HTML lang
- `$_SESSION['setup_license_accept']` — état de l'acceptation de licence

## Exports / Symboles principaux
Aucun. Vue HTML pure.

## Interactions
- **Appelé par :** `install.php` (étape de présentation de la licence)
- **Position dans le flux global :** étape 2 du wizard (après la vérification système)

---

## Notes
- La protection `sugarEntry` est commentée (ligne 2) — accès possible directement si `$install_script` n'est pas défini.
- `$checked` : pré-coche la case si l'utilisateur est déjà revenu sur cette étape avec acceptation en session.
- `LICENSE.txt` contient la licence AGPL v3 de SuiteCRM.
