# Fichier : controller.php (Contacts)

**Chemin :** `modules/Contacts/controller.php`
**Type :** PHP - Controleur (SugarController)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Controleur principal du module Contacts. Gere les actions HTTP specifiques : popup de selection, popup de publipostage, validation de nom d'utilisateur portail, recuperation d'email, et popup d'adresse.

## Role technique

Etend `SugarController` (heritage implicite, sans `require_once` visible). Definit cinq actions supplementaires qui redirigent vers des vues specialisees.

---

## Dependances cles

- **Extends :** `SugarController` (heritage implicite)

## Exports / Symboles principaux

- `ContactsController` — classe — controleur du module Contacts
  - `action_Popup()` — vue `mailmergepopup` ou `popup` selon `$_REQUEST['html']` (l.46)
  - `action_ValidPortalUsername()` — vue `validportalusername` (l.54)
  - `action_RetrieveEmail()` — vue `retrieveemail` (l.59)
  - `action_ContactAddressPopup()` — vue `contactaddresspopup` (l.64)
  - `action_CloseContactAddressPopup()` — vue `closecontactaddresspopup` (l.69)

## Consommateurs identifies

- Framework MVC SuiteCRM (dispatch automatique)

## Relations cles

- **Vues associees :** `views/view.mailmergepopup.php`, `views/view.popup.php`, `views/view.validportalusername.php`, `views/view.retrieveemail.php`, `views/view.contactaddresspopup.php`

---

## Points d'attention

- Le popup de publipostage (mail merge) est detecte via `$_REQUEST['html'] == 'mail_merge'`.
