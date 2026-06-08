# Menu.php

**Chemin :** `modules/Prospects/Menu.php`
**Type :** PHP - Configuration (menu)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Définit le menu du module Prospects avec vérifications ACL pour chaque entrée : Créer, Liste, Import.

## Type
config

## Dépendances clés
- `ACLController::checkAccess()` — vérification des droits
- `$mod_strings` — LNK_NEW_PROSPECT, LNK_PROSPECT_LIST, LNK_IMPORT_PROSPECTS

## Exports / Symboles principaux
- `$module_menu` (tableau) — 3 entrées conditionnelles selon les droits ACL

## Interactions
- **Appelé par :** framework SugarCRM (chargement du menu du module)
- **Appelle :** `ACLController::checkAccess()`

## Notes
- Import redirige vers `Import/Step1?import_module=Prospects`.
