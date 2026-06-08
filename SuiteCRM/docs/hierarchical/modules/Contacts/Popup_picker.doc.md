# Popup_picker.php

**Chemin :** `modules/Contacts/Popup_picker.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Classe de sélection en popup pour le module Contacts. Fournit deux modes d'affichage : sélection d'adresse (`process_page_for_address`) et sélection pour mail merge (`process_page_for_merge`). Utilisée depuis les vues popup du module.

**Type :** helper / composant popup

---

## Dépendances clés

- `modules/Contacts/ContactFormBase.php`
- `append_where_clause()`, `generate_where_statement()` — construction des clauses WHERE
- `$_REQUEST['query']` — paramètre de recherche
- Tables `contacts`, `accounts` (via JOIN)

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `Popup_Picker` | classe | Gère les popups de sélection de contact |
| `_get_where_clause()` | méthode | Construit la clause WHERE pour recherche par prénom, nom, compte |
| `process_page_for_address()` | méthode | Affiche la popup de sélection d'adresse de contact |
| `process_page_for_merge()` | méthode | Affiche la popup de sélection pour mail merge |

---

## Interactions

**Appelée par :**
- `ContactsViewContactAddressPopup::display()` (view.contactaddresspopup.php)
- `ContactsViewMailMergePopup::display()` (view.mailmergepopup.php)

**Position dans le flux global :** Composant central des fenêtres popup de sélection de contacts.

---

## Notes

- La recherche inclut `first_name`, `last_name` et `account_name` (JOIN accounts).
- Deux méthodes distinctes pour les deux cas d'usage (adresse vs mail merge).
