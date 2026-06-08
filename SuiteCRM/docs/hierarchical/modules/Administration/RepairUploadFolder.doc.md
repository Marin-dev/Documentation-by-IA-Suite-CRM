# RepairUploadFolder.php

**Chemin :** `modules/Administration/RepairUploadFolder.php`
**Type :** PHP (action / maintenance)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Nettoie le dossier `upload/` en supprimant les fichiers orphelins (GUIDs qui ne correspondent a aucun enregistrement BDD actif) et les fichiers lies a des enregistrements supprimes logiquement.

## Role technique
Construit la liste des beans qui ont des champs fichier (`haveFiles()`). Itere sur `upload://` via `DirectoryIterator`, filtre les GUIDs, cherche chaque fichier dans les tables BDD correspondantes (actif et deleted=1). Supprime le fichier si non trouve ou si `deleted=1`. Affiche une barre de progression `....` par tranches de 100.

---

## Dependances cles
| Element | Role |
|---|---|
| `BeanFactory::getBean()` | Instanciation des beans |
| `SugarBean::haveFiles()` | Verifie si le bean a des champs fichier |
| `SugarBean::getFilesFields()` | Liste des champs de type fichier |
| `SugarBean::deleteFiles()` | Suppression des fichiers du bean |
| `DirectoryIterator('upload://')` | Iteration sur le dossier upload |

## Interactions
- **Appele par :** `index.php?module=Administration&action=RepairUploadFolder`
- **Modifie :** Systeme de fichiers (`upload/`)

---

## Notes
- `set_time_limit(3600)` — peut etre tres long sur de grosses instances avec beaucoup de fichiers.
- `is_guid()` filtre uniquement les fichiers au format GUID — les autres fichiers sont ignores.
- `ob_flush()` + `flush()` tous les 100 fichiers pour eviter les timeouts HTTP.
