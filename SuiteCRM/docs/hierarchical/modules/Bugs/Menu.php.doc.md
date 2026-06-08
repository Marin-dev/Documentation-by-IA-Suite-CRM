# 📄 Menu.php

**Chemin :** `modules/Bugs/Menu.php`
**Type :** PHP — configuration de menu
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Définit les entrées du menu de navigation du module Bugs (barre du haut). Conditionne chaque entrée à une vérification ACL.

## Rôle technique

Fichier de configuration procédural. Peuple le tableau global `$module_menu` avec 3 entrées conditionnelles : Créer un bug, Lister les bugs, Importer des bugs. Chaque entrée est soumise à `ACLController::checkAccess()`.

---

## Dépendances clés

- `ACLController::checkAccess()` — contrôle d'accès par action (`edit`, `list`, `import`)
- `$mod_strings` — libellés traduits du module

## Exports / Symboles principaux

- `$module_menu` (tableau global) — entrées de menu du module Bugs

---

## Notes

- Entrées : `EditView` (create), `index` (list), `Import/Step1` (import).
- Fichier chargé automatiquement par le framework SugarCRM lors de l'affichage du menu du module.
