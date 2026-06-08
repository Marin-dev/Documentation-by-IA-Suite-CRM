# Fichier : view.list.php

**Chemin :** `modules/Leads/views/view.list.php`
**Type :** `PHP`
**Categorie :** view (liste)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Vue liste des leads. Injecte la popup Form Letter PDF et instancie le renderer `LeadsListViewSmarty` avec ses actions enrichies.

## Role technique

Classe `LeadsViewList` heritant de `ViewList`. Surcharge `preDisplay()` : injecte la popup Form Letter et cree une instance de `LeadsListViewSmarty` comme renderer (`$this->lv`). Structure identique a `AccountsViewList`.

---

## Dependances cles

| Dependance | Role |
| --- | --- |
| `ViewList` | Classe parente (framework) |
| `LeadsListViewSmarty` | Renderer specifique avec actions enrichies |
| `formLetter::LVPopupHtml()` | Popup Form Letter |

## Exports / Symboles principaux

| Symbole | Type | Role |
| --- | --- | --- |
| `LeadsViewList` | classe | Vue liste Lead |
| `preDisplay()` | methode | Surcharge : popup PDF + renderer specifique |

## Points d'attention

- Structure identique a `AccountsViewList`. RAS.
