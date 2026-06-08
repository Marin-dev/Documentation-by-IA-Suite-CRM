# Fichier : view.contactaddresspopup.php (Contacts)

**Chemin :** `modules/Contacts/views/view.contactaddresspopup.php`
**Type :** PHP - Vue (popup adresse)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Affiche le popup de selection d'adresse de contact. Permet de selectionner l'adresse d'un contact (principale ou secondaire) pour la remplir dans un formulaire parent.

## Role technique

Etend `SugarView`. Utilise `Popup_picker` depuis `modules/Contacts/Popup_picker.php`. Classe `ContactsViewContactAddressPopup`.

---

## Dependances cles

- `include/MVC/View/SugarView.php`
- `modules/Contacts/Popup_picker.php`

## Exports / Symboles principaux

- `ContactsViewContactAddressPopup` — classe — vue popup adresse contact

## Consommateurs identifies

- `ContactsController::action_ContactAddressPopup()`
- Formulaires necessitant la selection d'une adresse de contact (ex: publipostage)

## Relations cles

- **Ferme par :** `view.closecontactaddresspopup.php`

---

## Points d'attention

- Popup specialise pour les adresses — distinct du popup de selection de contact standard.
