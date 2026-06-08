# Menu.php

**Chemin :** `modules/Contacts/Menu.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Définit les entrées du menu de navigation du module Contacts. Génère la liste `$module_menu` avec les liens de création, import vCard, liste et import CSV, en respectant les contrôles ACL.

**Type :** configuration / menu

---

## Dépendances clés

- `ACLController::checkAccess()` — vérification des droits par action
- `$mod_strings` — libellés localisés
- `$app_strings`, `$sugar_config`

---

## Exports / Symboles principaux

| Variable | Contenu |
|---|---|
| `$module_menu` | Tableau des entrées de menu (url, libellé, icône, module) |

**Entrées définies :**

| Action | Droits requis | Destination |
|---|---|---|
| Nouveau Contact | `edit` | `action=EditView` |
| Importer vCard | `import` | `action=ImportVCard` |
| Liste des Contacts | `list` | `action=index` |
| Importer des Contacts | `import` | `module=Import&action=Step1` |

---

## Interactions

**Appelée par :** Framework SuiteCRM lors du rendu de la barre de navigation du module Contacts.

**Position dans le flux global :** Menu de navigation module — chargé à chaque affichage de page du module.

---

## Notes

- Toutes les entrées sont conditionnées par `ACLController::checkAccess()` — rien n'est affiché si l'utilisateur n'a pas les droits.
