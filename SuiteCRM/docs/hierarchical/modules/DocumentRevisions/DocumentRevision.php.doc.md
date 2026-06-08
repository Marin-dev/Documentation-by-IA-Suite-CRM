# DocumentRevision.php

**Chemin :** `modules/DocumentRevisions/DocumentRevision.php`
**Type :** model

**Dernière mise à jour doc :** 2026-06-02

---

## Rôle

Modèle d'une révision de document. Chaque révision stocke un fichier physique avec son numéro de version, son type MIME, son changelog et son lien vers le document parent. La table `document_revisions` historise toutes les versions d'un document.

## Type

model

---

## Dépendances clés

- `SugarBean` (classe parente)
- `include/upload_file.php` — gestion des fichiers uploadés

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `DocumentRevision` | classe | Entité révision de document (table `document_revisions`) |
| `document_id` | propriété | ID du document parent |
| `revision` | propriété | Numéro/libellé de la révision |
| `change_log` | propriété | Description des changements |
| `file_mime_type` | propriété | Type MIME du fichier |
| `latest_revision_id` | propriété | ID de la dernière révision du document |

## Interactions

- **Appelé par :** `Document::save()` (création automatique d'une révision), vues DocumentRevisions
- **Appelle :** UploadFile

## Notes

- Le fichier physique est stocké dans `upload://{revision_id}`.
- `Document` crée automatiquement une `DocumentRevision` lors de la première sauvegarde (ligne 134 de Document.php).
