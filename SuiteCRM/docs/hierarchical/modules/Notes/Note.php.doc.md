# Fichier : Note.php

**Chemin :** `modules/Notes/Note.php`
**Type :** model
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Classe metier centrale du module Notes. Represente une note textuelle pouvant porter une piece jointe (fichier). Utilisee pour l'historique des activites, les notes de reunion, les rappels, et les pieces jointes email.

## Role technique
Etend `File` (`include/SugarObjects/templates/file/File.php`), qui elle-meme etend `SugarBean`. Surcharge `mark_deleted()` pour supprimer le fichier physique si la note parent est un email et que `email_default_delete_attachments` est active. Methode `safeAttachmentName()` ajoute `.txt` aux extensions interdites (`sugar_config['upload_badext']`). Fichiers stockes dans `upload/{id}`.

---

## Dependances cles
| Import | Role |
|---|---|
| `File` (`include/SugarObjects/templates/file/File.php`) | classe parente avec gestion fichiers |
| `upload_file` (`include/upload_file.php`) | upload fichiers |
| `BeanFactory` | beans Contacts |
| `SugarEmailAddress` | recuperation email contact |

## Exports / Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `Note` | classe | bean principal module Notes |
| `safeAttachmentName()` | methode | securise les extensions de fichier |
| `deleteAttachment()` | methode | supprime le fichier physique |
| `getAttachmentContent()` | methode | lit le contenu binaire du fichier |

## Table SQL
- `notes`

---

## Relations cles
- **Appele par :** module Emails, formulaires Notes, logic hooks
- **Appelle :** `SugarEmailAddress`, `BeanFactory::newBean('Contacts')`

---

## Points d'attention
- Les fichiers sont stockes dans `upload/{note_id}` — pas dans un sous-repertoire nomme.
- `portal_flag` permet l'acces depuis le portail client — a verifier en cas de configuration portail.
- `embed_flag` indique une image inline (email) vs piece jointe separee.
