# Fichier : view.retrieveemail.php (Contacts)

**Chemin :** `modules/Contacts/views/view.retrieveemail.php`
**Type :** PHP - Vue (recuperation email)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Retourne les informations d'une adresse email associee a un contact. Utilisee lors de la composition d'email pour auto-completer le destinataire avec le nom et l'adresse email du contact.

## Role technique

Surcharge `SugarView` via la classe `ContactsViewRetrieveEmailUsername`. Implemente la methode de recuperation des informations email du contact selon son identifiant.

---

## Dependances cles

- `SugarView` (heritage)

## Exports / Symboles principaux

- `ContactsViewRetrieveEmailUsername` — classe (INCONNU : methodes exactes apres l.50)

## Consommateurs identifies

- `ContactsController::action_RetrieveEmail()`
- Composant de composition email pour l'auto-completion des destinataires

## Relations cles

- **Position dans le flux :** Recuperation des infos email d'un contact pour la composition

---

## Points d'attention

- Auteur indique : Collin Lee (l.48) — classe ancienne, verifier la compatibilite.
