# Fichier : ContactsJjwg_MapsLogicHook.php

**Chemin :** `modules/Contacts/ContactsJjwg_MapsLogicHook.php`
**Type :** PHP - Hook logique (integration cartographique)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Hook logique integrant le module de cartographie `jjwg_Maps` avec le module Contacts. Met a jour les informations de geocodage de l'adresse d'un contact lors de la sauvegarde, et met a jour les reunions georeferencees associees apres sauvegarde.

## Role technique

Classe `ContactsJjwg_MapsLogicHook`. Utilise `get_module_info('jjwg_Maps')` pour acceder aux parametres de configuration. Les methodes sont des callbacks de logic hooks SugarCRM.

---

## Dependances cles

- `get_module_info('jjwg_Maps')` — acces au module de cartes
- `jjwg_Maps->updateGeocodeInfo()` — geocodage de l'adresse
- `jjwg_Maps->updateRelatedMeetingsGeocodeInfo()` — mise a jour des reunions

## Exports / Symboles principaux

- `ContactsJjwg_MapsLogicHook` — classe
  - `updateGeocodeInfo(&$bean, $event, $arguments)` — hook `before_save` (l.21)
  - `updateRelatedMeetingsGeocodeInfo(&$bean, $event, $arguments)` — hook `after_save` (l.29)

## Consommateurs identifies

- Fichier de logic hooks Contacts (INCONNU : `custom/Extension/modules/Contacts/Ext/LogicHooks/`)

## Relations cles

- **Appelle :** module `jjwg_Maps`
- **Position dans le flux :** before_save / after_save du bean Contact

---

## Points d'attention

- Conditionnel : les hooks ne s'executent que si `jjwg_Maps->settings['logic_hooks_enabled']` est `true`.
- Dependance forte sur le module `jjwg_Maps` — si absent ou desactive, le geocodage est silencieusement ignore.
