# studio.php

**Chemin :** `modules/Campaigns/metadata/studio.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Déclare les définitions de vues éditables via l'outil Studio de SuiteCRM pour le module Campaigns. Référence les fichiers de templates (HTML) et PHP pour chaque type de vue (détail, édition, liste, formulaire de recherche).

**Type :** configuration / metadata Studio

---

## Configure

Outil Studio de SuiteCRM (`$GLOBALS['studioDefs']['Campaigns']`)

## Paramètres clés

| Vue | Template | Fichiers référencés |
|---|---|---|
| `LBL_DETAILVIEW` | xtpl | `DetailView.html`, `DetailView.php` |
| `LBL_EDITVIEW` | xtpl | `EditView.html`, `EditView.php` |
| `LBL_LISTVIEW` | listview | `listviewdefs.php` |
| `LBL_SEARCHFORM` | xtpl | `SearchForm.html`, `ListView.php` |

---

## Impacté par / impacte

- Outil Studio (admin) — lit ce fichier pour proposer les vues personnalisables
- Fichiers HTML/PHP référencés — doivent exister pour que Studio fonctionne

---

## Notes

- Les fichiers `DetailView.html`, `EditView.html` etc. référencés sont des templates classiques (non MVC) — le module Campaigns utilise partiellement l'architecture "classic" de SugarCRM.
