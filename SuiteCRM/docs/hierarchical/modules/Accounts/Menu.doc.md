# Fichier : Menu.php

**Chemin :** `modules/Accounts/Menu.php`
**Type :** `PHP`
**Categorie :** configuration (menu module)
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure

Definit le menu de navigation superieur du module Accounts. Enregistre trois entrees dans `$module_menu` selon les droits ACL de l'utilisateur courant.

---

## Parametres cles

| Entree menu | URL cible | Droit requis |
| --- | --- | --- |
| Nouveau compte | `index.php?module=Accounts&action=EditView` | `edit` |
| Liste des comptes | `index.php?module=Accounts&action=index` | `list` |
| Importer des comptes | `index.php?module=Import&action=Step1&import_module=Accounts` | `import` |

## Impacte par / impacte

- Charge par le framework lors du rendu de la barre de navigation du module
- Dependances : `ACLController::checkAccess()`, globals `$mod_strings`, `$app_strings`, `$sugar_config`

## Points d'attention

- Chaque entree est conditionnee par `ACLController::checkAccess()` : les entrees non autorisees sont absentes du menu.
- Script procedural pur : peuple la variable globale `$module_menu`, pas de classe.
- L'import redirige vers le module `Import` (pas Accounts directement).
