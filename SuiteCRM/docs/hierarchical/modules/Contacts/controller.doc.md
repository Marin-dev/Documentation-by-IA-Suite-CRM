# controller.php

**Chemin :** `modules/Contacts/controller.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Contrôleur MVC du module Contacts. Déclare les actions spécifiques au module : popup (standard ou mail merge), validation nom d'utilisateur portal, récupération email, popup adresse, fermeture popup adresse.

## Type

`controller`

---

## Dépendances clés

| Import / Héritage | Rôle |
|---|---|
| `SugarController` (extend) | Contrôleur de base SuiteCRM |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `ContactsController` | classe | Contrôleur du module Contacts |
| `action_Popup()` | méthode | Route vers `mailmergepopup` ou `popup` selon paramètre |
| `action_ValidPortalUsername()` | méthode | Route vers vue `validportalusername` |
| `action_RetrieveEmail()` | méthode | Route vers vue `retrieveemail` |
| `action_ContactAddressPopup()` | méthode | Route vers vue `contactaddresspopup` |
| `action_CloseContactAddressPopup()` | méthode | Route vers vue `closecontactaddresspopup` |

---

## Interactions

- **Appelé par :** Framework MVC SuiteCRM (dispatch)
- **Appelle :** Vues correspondantes dans `modules/Contacts/views/`

---

## Points d'attention

- `action_Popup()` vérifie le paramètre `$_REQUEST['html'] == 'mail_merge'` pour distinguer les deux types de popup.
