# Fichier : view.list.php

**Chemin :** `modules/Accounts/views/view.list.php`
**Type :** `PHP`
**Categorie :** view (liste)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Vue liste des comptes. Injecte la popup Form Letter PDF et instancie le renderer de liste specifique Accounts avec les actions supplementaires (target list, cartographie).

## Role technique

Classe `AccountsViewList` heritant de `ViewList`. Surcharge `preDisplay()` pour injecter la popup Form Letter et creer une instance de `AccountsListViewSmarty` comme renderer de liste (`$this->lv`).

---

## Dependances cles

| Dependance | Chemin | Role |
| --- | --- | --- |
| `ViewList` | framework | Classe parente |
| `AccountsListViewSmarty` | `modules/Accounts/AccountsListViewSmarty.php` | Renderer specifique avec actions enrichies |
| `formLetter` | `modules/AOS_PDF_Templates/formLetter.php` | Popup Form Letter |

## Exports / Symboles principaux

| Symbole | Type | Role |
| --- | --- | --- |
| `AccountsViewList` | classe | Vue liste Account |
| `preDisplay()` | methode | Surcharge : popup PDF + instanciation du renderer specifique |

## Relations cles

- **Appele par :** Framework SuiteCRM (routing action=index/ListView, module=Accounts)
- **Appelle :** `AccountsListViewSmarty` (via `$this->lv`)

---

## Points d'attention

- Classe tres courte : toute la logique de rendu est deleguee a `AccountsListViewSmarty`.
- La popup Form Letter est injectee via `formLetter::LVPopupHtml('Accounts')` dans `preDisplay()`.
