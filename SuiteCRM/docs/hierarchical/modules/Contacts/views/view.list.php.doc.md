# Fichier : view.list.php (Contacts)

**Chemin :** `modules/Contacts/views/view.list.php`
**Type :** PHP - Vue (liste)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Surcharge la vue liste standard pour le module Contacts. Integre le popup de publipostage PDF et utilise `ContactsListViewSmarty` pour le rendu enrichi (cartographie, Confirm Opt-In).

## Role technique

Etend `ViewList`. Override `preDisplay()` pour initialiser `formLetter::LVPopupHtml()` et instancier `ContactsListViewSmarty` comme renderer de liste.

---

## Dependances cles

- `modules/Contacts/ContactsListViewSmarty.php`
- `modules/AOS_PDF_Templates/formLetter.php`
- `ViewList` — classe parente

## Exports / Symboles principaux

- `ContactsViewList` — classe
  - `preDisplay()` — initialise le popup PDF et le renderer (l.11)

## Consommateurs identifies

- Framework MVC SuiteCRM (charge pour `action=index` du module Contacts)

## Relations cles

- **Utilise :** `ContactsListViewSmarty` (avec liens carte et publipostage)
- **Position dans le flux :** Vue liste principale des contacts

---

## Points d'attention

- `formLetter::LVPopupHtml('Contacts')` ajoute le bouton de publipostage PDF dans la barre d'actions de la liste.
