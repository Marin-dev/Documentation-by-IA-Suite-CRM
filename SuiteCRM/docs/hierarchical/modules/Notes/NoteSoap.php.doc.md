# Fichier : NoteSoap.php

**Chemin :** `modules/Notes/NoteSoap.php`
**Type :** PHP - Helper API SOAP/Web Services
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Fournit les operations de gestion de pieces jointes sur les Notes via l'API SOAP/Web Services de SuiteCRM. Permet de sauvegarder un fichier encode en base64 sur une note existante, et de recuperer le contenu d'une piece jointe en base64.

## Role technique

Classe `NoteSoap` avec trois methodes. `saveFile()` et `newSaveFile()` decodent un fichier base64 depuis le payload SOAP, appliquent la securite des extensions (`upload_badext`), sauvegardent la note et deplacent le fichier. `retrieveFile()` retourne le contenu en base64. Utilise `UploadFile::set_for_soap()` pour l'upload hors contexte HTTP.

---

## Dependances principales

| Import / Classe | Role |
| --- | --- |
| `UploadFile` (`include/upload_file.php`) | Gestion upload/download fichiers |
| `BeanFactory` | Instanciation du bean `Notes` |
| `SuiteValidator` | Validation de l'ID (securite) |
| `$sugar_config['upload_badext']` | Liste des extensions interdites |

---

## Exports / Symboles principaux

| Symbole | Type | Role |
| --- | --- | --- |
| `NoteSoap` | Classe | Helper SOAP pour les pieces jointes Notes |
| `NoteSoap::saveFile()` | Methode | Sauvegarde fichier base64 sur note existante (legacy) |
| `NoteSoap::newSaveFile()` | Methode | Sauvegarde fichier + gestion module lie (nouvelle version) |
| `NoteSoap::retrieveFile()` | Methode | Recupere contenu fichier encode base64 |

---

## Relations cles

- **Appele par :** API SOAP SuiteCRM (INCONNU — module web services v8 ou legacy)
- **Appelle :** `Note::save()`, `UploadFile::set_for_soap()`, `UploadFile::final_move()`

---

## Points d'attention

- Double `require_once('include/upload_file.php')` (lignes 47 et 49) — anomalie bénigne (idempotent).
- `saveFile()` retourne `-1` si l'ID est absent ou invalide — pas d'exception levee.
- `newSaveFile()` ne valide pas l'ID avec `SuiteValidator` contrairement a `saveFile()` — asymetrie de securite.
- Si `related_module_name == 'Contacts'`, utilise `contact_id` au lieu de `parent_id` (ligne 157-163).
