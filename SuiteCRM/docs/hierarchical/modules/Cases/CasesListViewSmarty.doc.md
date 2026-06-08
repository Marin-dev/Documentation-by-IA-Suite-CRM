# CasesListViewSmarty.php

**Chemin :** `modules/Cases/CasesListViewSmarty.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Surcharge de la vue liste generique pour le module Cases. Ajoute un lien d'export vers les cartes geographiques (jjwg_Maps) en plus du lien d'export standard.

## Type
view / helper

## Dependances cles
- `include/ListView/ListViewSmarty.php` — classe parente `ListViewSmarty`
- Module `jjwg_Maps` — integration cartographique

## Exports / Symboles principaux
- `class CasesListViewSmarty extends ListViewSmarty`
- Methode `buildExportLink()` — retourne le HTML avec deux liens : export standard + lien carte jjwg_Maps

## Interactions
- **Appele par :** `CasesViewList` (views/view.list.php) qui instancie `CasesListViewSmarty` dans `preDisplay()`

## Notes
- Le lien map utilise le module `jjwg_Maps` avec `display_module=Cases`.
- Injection directe de `$_REQUEST['module']` dans les URLs — attention XSS potentiel si non echappe en aval.
