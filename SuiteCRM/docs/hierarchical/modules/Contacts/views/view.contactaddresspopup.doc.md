# view.contactaddresspopup.php

**Chemin :** `modules/Contacts/views/view.contactaddresspopup.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Vue popup de sélection d'adresse de contact. Affiche une liste de contacts avec leurs adresses pour permettre la sélection et le remplissage d'un formulaire dans la fenêtre parente.

**Type :** view / popup

---

## Dépendances clés

- `include/MVC/View/SugarView.php` (classe parente)
- `modules/Contacts/Popup_picker.php` — classe `Popup_Picker`

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `ContactsViewContactAddressPopup` | classe | Vue popup de sélection d'adresse |
| `display()` | méthode | Lance `Popup_Picker::process_page_for_address()` |

---

## Interactions

**Appelle :**
- `$popup->process_page_for_address()` — génère le HTML de la popup

**Appelée par :** `ContactsController::action_ContactAddressPopup()` (controller.php ligne 65).

**Position dans le flux global :** Sélection d'adresse de contact depuis un formulaire externe (ex: formulaire de création de tâche/email).

---

## Notes

- Appelle `$this->renderJavascript()` avant l'affichage pour injecter les scripts nécessaires à la communication popup/parent.
