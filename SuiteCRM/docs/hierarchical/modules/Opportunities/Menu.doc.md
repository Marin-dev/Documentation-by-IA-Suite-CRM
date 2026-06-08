# Fichier : Menu.php

**Chemin :** `modules/Opportunities/Menu.php`
**Type :** `PHP`
**Categorie :** configuration (menu module)
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure

Definit le menu de navigation superieur du module Opportunities avec trois entrees.

---

## Parametres cles

| Entree menu | URL cible | Droit requis |
| --- | --- | --- |
| Nouvelle opportunite | `index.php?module=Opportunities&action=EditView` | `edit` |
| Liste des opportunites | `index.php?module=Opportunities&action=index` | `list` |
| Importer | `index.php?module=Import&action=Step1&import_module=Opportunities` | `import` |

## Points d'attention

- Script procedural pur. RAS.
