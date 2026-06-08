# Menu.php

**Chemin :** `modules/Bugs/Menu.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Definit les entrees du menu de navigation superieur du module Bugs. Chaque entree est conditionnee par les droits ACL de l'utilisateur courant.

## Type
config / helper navigation

## Dependances cles
- `ACLController::checkAccess()` — verification des droits (edit, list, import)
- `$mod_strings` — labels localises
- `$module_menu` — tableau global du menu SuiteCRM

## Exports / Symboles principaux
- `$module_menu` (tableau global) — entrees : Creer un bug, Lister les bugs, Importer

## Interactions
- **Appelle :** `ACLController::checkAccess('Bugs', 'edit'|'list'|'import', true)`
- **Appele par :** framework SuiteCRM lors de l'affichage de la barre de navigation du module

## Notes
- Actions disponibles : `EditView` (creer), `index` (liste), `Import > Step1` (import).
- Aucune logique metier, fichier purement declaratif.
