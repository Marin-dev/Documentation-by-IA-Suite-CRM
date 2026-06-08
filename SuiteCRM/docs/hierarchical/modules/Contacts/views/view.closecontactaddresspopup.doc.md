# view.closecontactaddresspopup.php

**Chemin :** `modules/Contacts/views/view.closecontactaddresspopup.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Vue de fermeture de la popup d'adresse de contact. Ferme la fenêtre popup via JavaScript (`window.close()`) si le paramètre `close_window` est présent dans la requête, puis délègue à la vue liste parente.

**Type :** view / popup

---

## Dépendances clés

- `ViewList` (classe parente)
- `$_REQUEST['close_window']` — déclencheur de fermeture

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `ContactsViewCloseContactAddressPopup` | classe | Vue de fermeture popup |
| `display()` | méthode | Émet `window.close()` si `close_window` défini, puis appelle `parent::display()` |

---

## Interactions

**Appelée par :** `ContactsController::action_CloseContactAddressPopup()` (controller.php ligne 70).

**Position dans le flux global :** Étape finale après sélection d'une adresse dans la popup ; ferme la fenêtre et renvoie le résultat à la fenêtre parente.

---

## Notes

- La fermeture via `window.close()` nécessite que la popup ait été ouverte par JavaScript depuis la même origine.
