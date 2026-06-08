# download_modules.php

**Chemin :** `install/download_modules.php`
**Type :** `PHP (installeur — vue HTML upload pack langue)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Affiche l'interface d'upload et de gestion des packs de langue pendant l'installation. Permet d'uploader un fichier ZIP de pack de langue, de le valider, de l'installer (`commit`), de le désinstaller ou de le supprimer. Gère également l'affichage des packs disponibles et installés.

**Type :** installer (vue HTML)

---

## Dépendances clés
- `sugarEntry` + `$install_script` + `$_SESSION['setup_db_admin_user_name']` — protections d'accès
- `ModuleInstall/PackageManager/PackageManager.php` — téléchargement depuis SugarCRM portal
- `ModuleInstall/PackageManager/PackageManagerDisplay.php` — `buildPatchDisplay()`
- `include/utils/php_zip_utils.php`, `include/upload_file.php` — upload et ZIP
- `$mod_strings`, `$sugar_version`, `$js_custom_version` — globaux wizard
- Fonctions : `langPackUnpack()`, `commitModules()`, `uninstallLanguagePack()`, `removeLanguagePack()`, `getLangPacks()`, `getInstalledLangPacks()`

## Exports / Symboles principaux
Aucune classe ni fonction exportée. Vue procédurale.

## Interactions
- **Appelé par :** `install.php` (inclusion selon l'étape)
- **Appelle AJAX :** `index.php?module=install&action=UploadLangFileCheck` pour valider la taille du fichier avant upload
- **Position dans le flux global :** étape optionnelle du wizard avant la configuration DB (installation de packs de langue supplémentaires)

---

## Notes
- La validation AJAX de la taille du fichier se fait avant l'activation du bouton "Upload" (JS `uploadCheck()`).
- L'upload n'accepte que les fichiers `.zip` — vérification côté client et côté serveur.
- Constante `SUGARCRM_MIN_UPLOAD_MAX_FILESIZE_BYTES` = 6 Mo minimum pour l'upload (ligne 165).
- `$sugar_config['upload_badext']` définit les extensions de fichiers interdites dans les uploads (lignes 60-76).
