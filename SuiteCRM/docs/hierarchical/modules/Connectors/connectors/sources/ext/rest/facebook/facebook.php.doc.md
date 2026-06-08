# facebook.php

**Chemin :** `modules/Connectors/connectors/sources/ext/rest/facebook/facebook.php`
**Type :** helper (connecteur externe)

**Dernière mise à jour doc :** 2026-06-02

---

## Rôle

Connecteur REST Facebook. Implémente la récupération de données de profils Facebook pour les enrichir dans les beans CRM (Contacts, Leads). Désactivé par défaut dans l'admin mapping (`_enable_in_admin_mapping = false`).

## Type

helper (connecteur externe)

---

## Dépendances clés

- `ext_rest` (`include/connectors/sources/ext/rest/rest.php`) — classe parente
- `$app_list_strings`

## Exports / Symboles principaux

- `ext_rest_facebook` — classe — connecteur Facebook via API REST

## Interactions

- **Appelé par :** framework Connectors SugarCRM (ExternalAPIFactory)
- **Appelle :** `ext_rest` (héritage)

## Notes

- `_enable_in_admin_mapping = false` : la configuration du mapping est désactivée dans l'admin.
- L'API Facebook Graph a considérablement évolué depuis la création de ce connecteur — à vérifier pour la compatibilité.
