# Document.php

**Chemin :** `modules/Documents/Document.php`
**Type :** model

**Dernière mise à jour doc :** 2026-06-02

---

## Rôle

Modèle principal des documents SuiteCRM. Gère les métadonnées d'un document (nom, catégorie, statut, dates d'activation/expiration) et orchestre la création automatique d'une révision (`DocumentRevision`) lors de la sauvegarde initiale. Supporte les documents externes (Google Drive, etc.) via `doc_type`.

## Type

model

---

## Dépendances clés

- `File` (`include/SugarObjects/templates/file/File.php`) — classe parente
- `BeanFactory` — instanciation DocumentRevisions, Documents
- `UploadFile` — gestion des fichiers uploadés
- `$_FILES['filename_file']` — fichier uploadé
- `$_REQUEST['duplicateSave']`, `$_REQUEST['duplicateId']` — duplication de document

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `Document` | classe | Entité document (table `documents`) |
| `save()` | méthode | Sauvegarde avec création automatique de la première révision |
| `document_revision_id` | propriété | ID de la révision courante |
| `is_template` | propriété | Indique si le document est un template de contrat |
| `doc_type` | propriété | Type de stockage : `Sugar` (local) ou externe |

## Interactions

- **Appelé par :** vues Documents, SOAP (`DocumentSoap`), `DocumentRevision`
- **Appelle :** BeanFactory (DocumentRevisions), UploadFile, `rename()` (déplacement du fichier uploadé)

## Notes

- Lors de la création, le fichier uploadé est renommé de `upload://{document_id}` vers `upload://{revision_id}`.
- En mode duplication, copie le fichier de l'ancienne révision vers la nouvelle.
- La relation `contracts` est déclarée dans `$relationship_fields`.
- Les documents de type non-Sugar (ex. Google Drive) sont gérés via `doc_id` et `doc_url`.
