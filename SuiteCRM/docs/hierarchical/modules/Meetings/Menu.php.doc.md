# Fichier : Menu.php

**Chemin :** `modules/Meetings/Menu.php`
**Type :** config / vue (menu navigation)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Definit les entrees du menu de navigation du module Meetings : planifier une nouvelle reunion, lister les reunions, importer des reunions. Chaque entree est conditionnee par une verification ACL.

## Role technique
Populez le tableau global `$module_menu` avec des tableaux `[url, label, icon, module]`. Verifie les permissions via `ACLController::checkAccess()` pour les actions `edit`, `list`, `import`.

---

## Dependances cles
- `ACLController` (global)
- `$mod_strings`, `$app_strings` (globaux)

## Exports / Symboles principaux
- `$module_menu` — tableau global alimente

---

## Relations cles
- **Appele par :** le framework SuiteCRM lors du rendu de la navigation
- **Appelle :** `ACLController::checkAccess()`

---

## Points d'attention
RAS.
