# DocumentExternalApiDropDown.php

**Chemin :** `modules/Documents/DocumentExternalApiDropDown.php`
**Type :** helper

**Dernière mise à jour doc :** 2026-06-02

---

## Rôle

Fournit la liste déroulante des APIs externes disponibles pour le stockage de documents (Sugar local + APIs externes enregistrées : Google Drive, etc.).

## Type

helper

---

## Dépendances clés

- `ExternalAPIFactory` (`include/externalAPI/ExternalAPIFactory.php`)
- `$app_list_strings['eapm_list']` — libellés des types d'API

## Exports / Symboles principaux

- `getDocumentsExternalApiDropDown()` — fonction — retourne la liste HTML `<select>` ou tableau des APIs disponibles pour `Documents`

## Interactions

- **Appelé par :** vues EditView Documents (champ `doc_type`)
- **Appelle :** `ExternalAPIFactory::getModuleDropDown('Documents')`

## Notes

- Ajoute toujours `Sugar` (stockage local) en premier dans la liste.
