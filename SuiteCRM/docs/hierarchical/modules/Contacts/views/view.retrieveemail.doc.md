# view.retrieveemail.php

**Chemin :** `modules/Contacts/views/view.retrieveemail.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Vue AJAX de récupération d'informations sur une adresse email. Retourne en JSON les données de la table `email_addresses` pour une adresse donnée. Utilisée pour la validation/auto-complétion d'adresses email dans les formulaires de contact.

**Type :** view / AJAX endpoint

---

## Dépendances clés

- `include/MVC/View/SugarView.php` (classe parente)
- `include/JSON.php` — encodage JSON
- `DBManagerFactory::getInstance()` — requête sur `email_addresses`
- `$_REQUEST['email']` — adresse à rechercher (comparaison insensible à la casse via `email_address_caps`)
- `$_REQUEST['target']` — cible retournée dans la réponse

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `ContactsViewRetrieveEmail` | classe | Vue AJAX retournant les infos d'une adresse email |
| `display()` | méthode | Requête `email_addresses` et retourne JSON `{target, email}` |

---

## Interactions

**Appelle :**
- Requête SQL sur `email_addresses` WHERE `email_address_caps = '$email'`
- `$json->encode($data)` — sérialisation

**Appelée par :** `ContactsController::action_RetrieveEmail()` (controller.php ligne 59). Appelée via AJAX depuis les formulaires de contact.

**Position dans le flux global :** Service de lookup d'adresse email pour la validation inline dans les formulaires.

---

## Notes

- Retourne un tableau vide `email = ''` si l'adresse n'est pas trouvée.
- Utilise `strtoupper()` + `trim()` pour la comparaison case-insensitive (ligne 73).
