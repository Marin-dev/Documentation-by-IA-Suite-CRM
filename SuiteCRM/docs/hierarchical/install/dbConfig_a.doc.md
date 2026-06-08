# Fichier : dbConfig_a.php

**Chemin :** `install/dbConfig_a.php`
**Type :** installer (vue wizard — etape 5 : configuration DB)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Affiche le formulaire de configuration de la base de donnees dans le wizard d'installation. Permet a l'utilisateur de renseigner le host, le nom de la base, les credentials admin et les options de creation/suppression de la base. Inclut aussi le choix d'utiliser des donnees de demonstration.

## Role technique
Template PHP generant une page HTML complete avec formulaire `setConfig`. Les champs DB sont generes dynamiquement par `$db->installConfig()`. Inclut un mecanisme AJAX (`callDBCheck()`) pour valider la connexion DB avant de passer a l'etape suivante. Affiche la barre de progression (LBL_STEP5).

---

## Dependances cles
- **Imports principaux :**
  - `getInstallDbInstance()` — driver DB courant
  - `cache/include/javascript/sugar_grp1_yui.js` — YUI
  - `cache/include/javascript/sugar_grp1_jquery.js` — jQuery/Bootstrap
  - `install/installCommon.js`, `install/dbConfig.js` — JS formulaire
  - `themes/SuiteP/css/fontello.css`, `animation.css`
- **Variables de contexte :** `$mod_strings`, `$next_step`, `$sugar_md`, `$sugar_version`, `$js_custom_version`
- **Session :** `setup_db_host_name`, `setup_db_host_instance`, `setup_db_port_num`, `setup_db_create_database`, `setup_db_drop_tables`, `setup_db_sugarsales_*`, `dbUSRData`, `demoData`

## Exports / Symboles principaux
- Aucun export — affichage HTML uniquement

## Interactions
- **Appele par :** `install.php` (include, etape 5)
- **Appelle :**
  - `install.php` (POST AJAX `checkDBSettings=true` via `callDBCheck()`)
  - `$db->installConfig()` — genere les champs formulaire DB

---

## Notes
- Le dropdown utilisateur DB (`dbUSRData`) permet 3 modes : `provide`, `create`, `same`.
- La confirmation de suppression de tables existantes (`confirm_drop_tables()`) est geree via un panneau YUI.
- Les mots de passe sont dupliques (champ visible + champ cache) pour gerer les caracteres speciaux (ligne 148).
- Ce fichier est l'ancienne version (etape 5 separee) ; `installConfig.php` fusionne DB + site en une seule page.
