# view.list.php

**Chemin :** `modules/Contacts/views/view.list.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Vue liste personnalisée du module Contacts. Injecte le popup de lettre PDF (formLetter) et utilise `ContactsListViewSmarty` comme moteur de liste.

## Type

`view`

---

## Dépendances clés

| Import / Héritage | Rôle |
|---|---|
| `ViewList` (extend) | Vue liste de base SuiteCRM |
| `modules/Contacts/ContactsListViewSmarty.php` | Moteur de liste custom |
| `modules/AOS_PDF_Templates/formLetter.php` | Popup lettre PDF |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `ContactsViewList` | classe | Vue liste custom Contacts |

---

## Interactions

- **Appelé par :** Framework MVC (action=index)
- **Appelle :** `ContactsListViewSmarty`

---

## Points d'attention

- RAS.
