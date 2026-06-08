# Fichier : Menu.php

**Chemin :** `modules/Leads/Menu.php`
**Type :** `PHP`
**Categorie :** configuration (menu module)
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure

Definit le menu de navigation superieur du module Leads. Enregistre quatre entrees dans `$module_menu` selon les droits ACL.

---

## Parametres cles

| Entree menu | URL cible | Droit requis |
| --- | --- | --- |
| Nouveau lead | `index.php?module=Leads&action=EditView` | `edit` |
| Importer vCard | `index.php?module=Leads&action=ImportVCard` | `edit` |
| Liste des leads | `index.php?module=Leads&action=index` | `list` |
| Importer des leads | `index.php?module=Import&action=Step1&import_module=Leads` | `import` |

## Points d'attention

- Script procedural pur. L'import vCard est une entree specifique aux Leads (non presente dans les autres modules).
