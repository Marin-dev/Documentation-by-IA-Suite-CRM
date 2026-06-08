# insideview.php

**Chemin :** `modules/Connectors/connectors/sources/ext/rest/insideview/insideview.php`
**Type :** helper (connecteur externe)

**Dernière mise à jour doc :** 2026-06-02

---

## Rôle

Connecteur REST InsideView. Permet l'enrichissement des données CRM avec des informations d'entreprises/contacts depuis InsideView. Toutes les fonctionnalités admin sont désactivées par défaut.

## Type

helper (connecteur externe)

---

## Dépendances clés

- `ext_rest` (`include/connectors/sources/ext/rest/rest.php`) — classe parente

## Exports / Symboles principaux

- `ext_rest_insideview` — classe — connecteur InsideView via API REST
- `$allowedModuleList` — propriété — liste des modules compatibles

## Interactions

- **Appelé par :** framework Connectors SugarCRM
- **Appelle :** `ext_rest` (héritage)

## Notes

- Toutes les options admin sont désactivées (`_enable_in_wizard`, `_enable_in_hover`, `_enable_in_admin_properties`, `_enable_in_admin_mapping`, `_enable_in_admin_search`, `_has_testing_enabled` = false).
- InsideView est un service tiers d'enrichissement de données B2B — vérifier la disponibilité du service.
