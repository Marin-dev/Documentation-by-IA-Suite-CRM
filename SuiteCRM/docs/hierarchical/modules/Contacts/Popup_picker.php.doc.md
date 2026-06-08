# Fichier : Popup_picker.php (Contacts)

**Chemin :** `modules/Contacts/Popup_picker.php`
**Type :** PHP - Composant UI (selecteur popup)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Fournit la classe `Popup_Picker` pour le selecteur popup de contacts. Permet de rechercher et selectionner un contact depuis une fenetre modale dans d'autres modules (ex: associer un contact a une opportunite).

## Role technique

Classe `Popup_Picker`. La methode `_get_where_clause()` construit la clause WHERE pour la recherche par prenom, nom et nom de compte. Requiert `modules/Contacts/ContactFormBase.php`.

---

## Dependances cles

- `modules/Contacts/ContactFormBase.php`
- `append_where_clause()` — construction de la clause WHERE

## Exports / Symboles principaux

- `Popup_Picker` — classe — selecteur popup de contacts
  - `_get_where_clause()` — construit le filtre de recherche (l.53)

## Consommateurs identifies

- Framework SuiteCRM (popup de selection de contact)

## Relations cles

- **Recherche sur :** `contacts.first_name`, `contacts.last_name`, `accounts.name`

---

## Points d'attention

- La recherche inclut le nom du compte (`accounts.name`) — necessite une jointure avec `accounts_contacts`.
