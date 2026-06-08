# Fichier : view.validportalusername.php (Contacts)

**Chemin :** `modules/Contacts/views/view.validportalusername.php`
**Type :** PHP - Vue (validation username portail)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Verifie via AJAX si un nom d'utilisateur portail est deja utilise. Retourne une reponse indiquant la disponibilite du nom d'utilisateur propose lors de la creation/modification d'un utilisateur portail.

## Role technique

Etend `SugarView` via `ContactsViewValidPortalUsername`. Appelee par une requete AJAX JavaScript lors de la saisie du nom d'utilisateur portail dans le formulaire de contact. Requiert `include/MVC/View/SugarView.php`.

---

## Dependances cles

- `include/MVC/View/SugarView.php`

## Exports / Symboles principaux

- `ContactsViewValidPortalUsername` — classe — validateur AJAX de nom d'utilisateur portail

## Consommateurs identifies

- `ContactsController::action_ValidPortalUsername()`
- Requete AJAX JavaScript depuis le formulaire d'edition du contact (champ `portal_name`)

## Relations cles

- **Appelle :** requete SQL sur `users` (INCONNU : details exacts)
- **Position dans le flux :** Validation temps-reel lors de la saisie du nom portail

---

## Points d'attention

- Auteur : Collin Lee (l.53) — utilise le framework MVC pour une action AJAX, pattern documentee dans le commentaire.
- Retourne probablement une reponse JSON ou HTML simple pour JavaScript.
