# ContactsJjwg_MapsLogicHook.php

**Chemin :** `modules/Contacts/ContactsJjwg_MapsLogicHook.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Logic hook pour l'intégration cartographique jjwg_Maps. Met à jour les coordonnées géographiques d'un contact avant sauvegarde, et met à jour les réunions liées après sauvegarde.

## Type

`helper` (logic hook)

---

## Dépendances clés

| Import / Dépendance | Rôle |
|---|---|
| `get_module_info('jjwg_Maps')` | Configuration du module de cartographie |
| `$this->jjwg_Maps->updateGeocodeInfo()` | Mise à jour géocodage |
| `$this->jjwg_Maps->updateRelatedMeetingsGeocodeInfo()` | Mise à jour réunions liées |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `ContactsJjwg_MapsLogicHook` | classe | Hook cartographique pour les contacts |
| `updateGeocodeInfo()` | méthode | Hook `before_save` : géocode l'adresse du contact |
| `updateRelatedMeetingsGeocodeInfo()` | méthode | Hook `after_save` : met à jour les réunions liées |

---

## Interactions

- **Déclenché par :** Logic hooks `before_save` et `after_save` du module Contacts
- **Appelle :** Module `jjwg_Maps`

---

## Points d'attention

- N'exécute rien si `logic_hooks_enabled` est désactivé dans les settings de jjwg_Maps.
