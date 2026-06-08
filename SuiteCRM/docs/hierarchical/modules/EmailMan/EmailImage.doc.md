# EmailImage.php

**Chemin :** `modules/EmailMan/EmailImage.php`
**Type :** PHP — entry point image
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Point d'entree qui sert les images incorporees dans les emails de campagne. Verifie que la note demandee est bien associee a un email (`parent_type = "Emails"`), puis renvoie le fichier image depuis le repertoire d'upload avec le bon `Content-Type`.

**Type :** helper / entry point

---

## Dependances cles
- `Note` (`modules/Notes/Note.php`)
- `BeanFactory::newBean('Notes')`
- `$GLOBALS['sugar_config']['upload_dir']`

---

## Interactions
- **Appele par :** navigateur client via lien `<img>` dans un email de campagne (URL `index.php?entryPoint=...` ou directement)
- **Appelle :** `Note::retrieve_by_string_fields()`

---

## Notes
- Aucune authentification verifiee ici ; l'acces est controle uniquement par l'existence d'une note valide liee a un email.
- Si `getimagesize()` echoue (fichier non image), renvoie `Content-Type: image/png` par defaut.
