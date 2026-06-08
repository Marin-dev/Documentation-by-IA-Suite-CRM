# dbConfig_a.php

**Chemin :** `install/dbConfig_a.php`
**Type :** `PHP (installeur — vue HTML étape DB)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Génère et affiche la page HTML de configuration de la base de données (étape 5 du wizard d'installation). Présente les champs de connexion DB, les options de création d'utilisateur DB, les données de démo et les boutons de navigation. Valide les paramètres via un appel AJAX asynchrone à `checkDBSettings`.

**Type :** installer (vue HTML)

---

## Dépendances clés
- `sugarEntry` + `$install_script` — protections d'accès
- `$mod_strings`, `$sugar_version`, `$js_custom_version`, `$sugar_md` — variables globales du wizard
- `getInstallDbInstance()` — instance du driver DB
- `get_language_header()` — entête HTML lang
- `$db->installConfig()` — paramètres de formulaire propres au driver
- `$db->supports("create_user")` — détermine si la création d'utilisateur DB est disponible
- `$next_step` — étape suivante dans le flux

## Exports / Symboles principaux
Aucune classe ni fonction. Affiche directement le HTML via `echo $out`.

## Interactions
- **Appelé par :** `install.php` (inclusion conditionnelle selon l'étape du wizard)
- **Appelle AJAX :** `install.php?checkDBSettings=true` (POST) → `checkDBSettings.php`
- **Position dans le flux global :** étape 5 du wizard (après le choix du type d'installation)

---

## Notes
- La validation DB est asynchrone via `YAHOO.util.Connect.asyncRequest` — la page ne se soumet que si `checkDBSettings` retourne `'dbCheckPassed'` ou confirmation de BDD existante (`'preexeest'`).
- Dropdown DB user : 3 modes — `provide` (utilisateur existant), `create` (nouvel utilisateur), `same` (admin = utilisateur applicatif).
- Les mots de passe sont gérés avec des champs `hidden` séparés pour encoder les caractères spéciaux (limitation des champs `password`).
- CSS référence `themes/SuiteP/css/fontello.css` et `animation.css`.
- **Note :** Ce fichier ancien (pattern `dbConfig_a`) coexiste avec la nouvelle vue dans `installConfig.php` (`InstallLayout`) — probablement l'ancienne version du wizard.
