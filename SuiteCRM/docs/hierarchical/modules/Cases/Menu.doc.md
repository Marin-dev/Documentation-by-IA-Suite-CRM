# Menu.php

**Chemin :** `modules/Cases/Menu.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Definit les entrees du menu de navigation superieur du module Cases, conditionnees par les droits ACL.

## Type
config / helper navigation

## Dependances cles
- `ACLController::checkAccess()` — verification droits (edit, list, import)
- `$mod_strings`, `$module_menu`

## Exports / Symboles principaux
- `$module_menu` — entrees : Creer un case, Lister les cases, Importer

## Interactions
- **Appele par :** framework SuiteCRM (barre de navigation du module)

## Notes
- Fichier purement declaratif.
