# AttachFiles.php

**Chemin :** `modules/EmailTemplates/AttachFiles.php`
**Type :** PHP — endpoint upload
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Gere l'upload de fichiers images/pieces jointes pour les templates email. Valide le type MIME, stocke le fichier dans le cache, retourne un tableau JSON avec le resultat.

**Type :** helper / endpoint upload

---

## Dependances cles
- `include/JSON.php`
- `include/upload_file.php`
- Types MIME acceptes : `image/gif`, `image/png`, `image/x-png`, `image/bmp`, `image/jpeg`, `image/jpg`, `image/pjpeg`

---

## Notes
- Cree le repertoire `sugar_cached('images/')` si absent.
