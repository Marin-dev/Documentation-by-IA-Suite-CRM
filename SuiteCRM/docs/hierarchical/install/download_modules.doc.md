# Fichier : download_modules.php

**Chemin :** `install/download_modules.php`
**Type :** installer (telechargement modules)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Gere le telechargement et l'installation de modules additionnels pendant le wizard d'installation. Utilise le gestionnaire de paquets pour permettre l'ajout de modules depuis le depot SuiteCRM.

## Role technique
Inclut `ModuleInstall/PackageManager/PackageManagerDisplay.php` pour l'interface de gestion de paquets. Prefixe les variables de configuration `$sugar_config` pour les uploads (upload_dir, upload_maxsize, upload_badext). Requiert une session DB valide (`setup_db_admin_user_name`) pour fonctionner.

---

## Dependances cles
- **Imports principaux :**
  - `ModuleInstall/PackageManager/PackageManagerDisplay.php` — affichage gestionnaire paquets
  - `$sugar_version`, `$js_custom_version` (globaux)
- **Variables de contexte :** `$mod_strings`, `$install_script`, `$sugar_config`, `$_SESSION['language']`
- **Condition d'acces :** `$_SESSION['setup_db_admin_user_name']` doit etre present
- **Garde :** `sugarEntry` requise

## Exports / Symboles principaux
- Aucun export — affichage HTML/telechargement

## Interactions
- **Appele par :** `install.php` (include, etape optionnelle download modules)
- **Appelle :**
  - `PackageManagerDisplay` — interface de gestion des paquets

---

## Notes
- Securite : si `setup_db_admin_user_name` est vide en session, le script meurt (ligne 48-50).
- L'upload maxsize est prefixe a 8192000 octets (8 MB) si non defini (ligne 56).
- La liste des extensions interdites (`upload_badext`) est initialisee si absente (suite du fichier non lue).
- Cette etape est probablement optionnelle dans le flux du wizard.
