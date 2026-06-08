# view.list.php

**Chemin :** `modules/Cases/views/view.list.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Vue liste du module Cases. Surcharge `preDisplay()` pour utiliser `CasesListViewSmarty` (avec le lien cartographique jjwg_Maps).

## Type
view

## Dependances cles
- `ViewList` (heritage implicite)
- `modules/Cases/CasesListViewSmarty.php` — classe de liste specialisee

## Exports / Symboles principaux
- `class CasesViewList extends ViewList`
- Methode `preDisplay()` — instancie `CasesListViewSmarty` comme moteur de rendu liste

## Interactions
- **Appelle :** `new CasesListViewSmarty()`
- **Appele par :** framework SuiteCRM (routing action=index)

## Notes
- Necessite `CasesListViewSmarty` pour le lien map.
