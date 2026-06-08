# view.validportalusername.php

**Chemin :** `modules/Contacts/views/view.validportalusername.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Vue AJAX de validation de l'unicité d'un nom d'utilisateur portail. Retourne le nombre de contacts existants avec ce `portal_name`, permettant au front-end de détecter les doublons lors de la saisie du nom d'utilisateur portail.

**Type :** view / AJAX endpoint

---

## Dépendances clés

- `include/MVC/View/SugarView.php` (classe parente)
- `$this->bean->db` — accès à la base de données
- `$_REQUEST['portal_name']` — nom d'utilisateur à vérifier
- Table `contacts` — requête COUNT

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `ContactsViewValidPortalUsername` | classe | Vue AJAX de validation d'unicité du nom portail |
| `display()` | méthode | Retourne le count (int) de contacts avec ce `portal_name` |

---

## Interactions

**Appelée par :** `ContactsController::action_ValidPortalUsername()` (controller.php ligne 54). Appelée via AJAX depuis le formulaire d'édition de contact lors de la saisie du nom portail.

**Position dans le flux global :** Validation en temps réel de l'unicité du `portal_name` pour le portail AOP.

---

## Notes

- Retourne `0` si `$_REQUEST['portal_name']` est vide (ligne 86).
- La valeur retournée est le COUNT brut (integer) — le front-end interprète > 0 comme un doublon.
- Requête : `SELECT count(id) AS total FROM contacts WHERE portal_name = '...' AND deleted='0'`.
