# Fichier : view.edit.php

**Chemin :** `modules/Meetings/views/view.edit.php`
**Type :** vue (edit view)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Vue d'edition d'une reunion. Charge les donnees de rappels pour le formulaire et injecte la configuration JSON pour les invites (json_config). Gere le cas "duplication" en reinitialisant le statut par defaut.

## Role technique
Etend `ViewEdit`. Surcharge `preDisplay()` pour forcer le statut `Held` si present dans la requete. Surcharge `display()` pour injecter `JSON_CONFIG_JAVASCRIPT`, les donnees de rappels (`Reminder::loadRemindersData`, `loadRemindersDataJson`, `loadRemindersDefaultValuesDataJson`) dans les variables Smarty.

---

## Dependances cles
- `ViewEdit` — classe parente
- `json_config` (`include/json_config.php`) — configuration JSON invites
- `Reminder` — chargement donnees rappels

## Exports / Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `MeetingsViewEdit` | classe | vue edition reunion |

---

## Relations cles
- **Appele par :** routeur SuiteCRM (`action=EditView`)
- **Appelle :** `Reminder::loadRemindersData()`, `json_config::get_static_json_server()`

---

## Points d'attention
- Si duplication (`isDuplicate`), le statut est reinitialise via `getDefaultStatus()` pour ne pas copier le statut `Held`.
