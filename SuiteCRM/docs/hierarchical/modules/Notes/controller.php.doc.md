# Fichier : controller.php

**Chemin :** `modules/Notes/controller.php`
**Type :** PHP - Controleur MVC
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Controleur MVC du module Notes. Gere la sauvegarde des notes avec upload de piece jointe, et la suppression de piece jointe depuis la vue edition.

## Role technique

Classe `NotesController` heritant de `SugarController`. L'action `action_save()` gere l'upload via `UploadFile`, deplace le fichier avec `final_move()` ou le duplique si `old_id` est present. L'action `action_editview()` intercepte la suppression de piece jointe (`deleteAttachment`) avant l'affichage du formulaire.

---

## Dependances principales

| Import / Classe | Role |
|---|---|
| `SugarController` (`include/MVC/Controller/SugarController.php`) | Classe de base MVC |
| `UploadFile` (`include/upload_file.php`) | Gestion de l'upload et du stockage fichier |
| `SuiteValidator` (`SuiteCRM\Utility\SuiteValidator`) | Validation d'IDs (securite) |
| `Note` (via `$this->bean`) | Bean Notes hydrate par le framework |

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `NotesController` | Classe | Controleur module Notes |
| `action_save()` | Methode | Sauvegarde note + upload fichier |
| `action_editview()` | Methode | Affichage formulaire + suppression piece jointe |

---

## Relations cles

- **Appele par :** Routeur SuiteCRM (`index.php?module=Notes&action=Save` ou `action=EditView`)
- **Appelle :** `UploadFile::confirm_upload()`, `UploadFile::final_move()`, `UploadFile::duplicate_file()`, `Note::save()`, `Note::deleteAttachment()`
- **Position dans le flux :** Entre la soumission HTTP et la persistance du bean Note

---

## Points d'attention

- Si `relate_id` et `parent_id` sont tous deux presents et differents, `relate_id` est efface (ligne 60-62) — evite une double relation.
- Si `parent_type == 'Contacts'`, le contact est automatiquement rempli dans `contact_id` / `contact_name` (lignes 64-70).
- La suppression de piece jointe en EditView est traitee par `echo` + `sugar_cleanup(true)` — reponse AJAX JSON-like (true/false).
