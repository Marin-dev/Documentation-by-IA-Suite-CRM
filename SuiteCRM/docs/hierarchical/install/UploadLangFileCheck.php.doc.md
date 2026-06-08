# UploadLangFileCheck.php

**Chemin :** `install/UploadLangFileCheck.php`
**Type :** `PHP (installeur — validation upload)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Endpoint AJAX appelé lors de l'upload d'un pack de langue pendant l'installation. Vérifie que la taille du fichier à uploader ne dépasse pas les limites `upload_max_filesize` et `post_max_size` de PHP, puis retourne la taille en octets si elle est dépassée (sinon rien).

**Type :** installer

---

## Dépendances clés
- `sugarEntry` — protection d'accès direct
- `include/JSON.php` — `getJSONobj()` (importé mais non utilisé effectivement)
- `include/upload_file.php` — `return_bytes()`
- `$_REQUEST['file_name']` — chemin du fichier à vérifier

## Exports / Symboles principaux
Aucune classe ni fonction exportée. Logique procédurale directe, `echo` de la taille si dépassement.

## Interactions
- **Appelé par :** `install/download_modules.php` via AJAX (appel JavaScript `YAHOO.util.Connect.asyncRequest`)
- **Appelle :** `filesize()`, `return_bytes()`, `sugar_cleanup()`
- **Position dans le flux global :** validation côté serveur avant upload du pack de langue dans le wizard

---

## Notes
- La variable `$json` et le code JSON commenté (lignes 54-61) semblent être des vestiges non nettoyés.
- La réponse est la taille en octets du fichier si elle dépasse le maximum — le client JS utilise cette valeur pour afficher une alerte.
