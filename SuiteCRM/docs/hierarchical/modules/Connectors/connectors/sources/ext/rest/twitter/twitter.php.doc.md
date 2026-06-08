# twitter.php

**Chemin :** `modules/Connectors/connectors/sources/ext/rest/twitter/twitter.php`
**Type :** helper (connecteur externe)

**Dernière mise à jour doc :** 2026-06-02

---

## Rôle

Connecteur REST Twitter/X. Permet la récupération de données de profils Twitter pour les enrichir dans les beans CRM (Accounts, Contacts, Leads). Hover, test et mapping admin désactivés.

## Type

helper (connecteur externe)

---

## Dépendances clés

- `ext_rest` (`include/connectors/sources/ext/rest/rest.php`) — classe parente
- `$app_list_strings`

## Exports / Symboles principaux

- `ext_rest_twitter` — classe — connecteur Twitter via API REST
- `$allowedModuleList` — propriété — modules compatibles (Accounts, ...)

## Interactions

- **Appelé par :** framework Connectors SugarCRM
- **Appelle :** `ext_rest` (héritage)

## Notes

- `_has_testing_enabled = false`, `_enable_in_admin_search = false`, `_enable_in_admin_mapping = false`, `_enable_in_hover = false`.
- L'API Twitter/X a changé depuis la création de ce connecteur (v2, restrictions) — compatibilité à vérifier.
