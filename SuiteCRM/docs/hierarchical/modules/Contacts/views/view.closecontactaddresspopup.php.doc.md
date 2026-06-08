# Fichier : view.closecontactaddresspopup.php (Contacts)

**Chemin :** `modules/Contacts/views/view.closecontactaddresspopup.php`
**Type :** PHP - Vue (fermeture popup adresse)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Gere la fermeture du popup d'adresse de contact apres selection. Renvoie les donnees de l'adresse selectionnee vers le formulaire parent via JavaScript.

## Role technique

Etend `ViewList`. Classe `ContactsViewCloseContactAddressPopup`. Le constructeur appelle `parent::__construct()` via une methode nommee differemment (pattern legacy).

---

## Dependances cles

- `ViewList` — classe parente

## Exports / Symboles principaux

- `ContactsViewCloseContactAddressPopup` — classe — vue de fermeture popup adresse

## Consommateurs identifies

- `ContactsController::action_CloseContactAddressPopup()`
- Sequence : `ContactAddressPopup` -> selection -> `CloseContactAddressPopup`

---

## Points d'attention

- Utilise un pattern de constructeur legacy (`CloseContactAddressPopup()` appelle `parent::__construct()`) — non-standard.
