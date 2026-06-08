# registry.php (v2)

**Chemin :** `service/v2/registry.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Registre des fonctions et types SOAP/REST pour la version 2 de l'API SuiteCRM. Enregistre toutes les opérations disponibles (login, get_entry, set_entry, relations, etc.) et tous les types complexes WSDL (name_value, entry_list, etc.) sur le service web.

**Type :** configuration / registre

---

## Dépendances clés
Aucun `require` explicite — appelé après que la classe de service soit déjà initialisée.

---

## Exports/Symboles principaux
- `registry` — classe de registre
  - `register()` — appelle `registerFunction()` puis `registerTypes()`
  - `registerFunction()` — enregistre ~20 fonctions API : `login`, `logout`, `get_entry`, `get_entries`, `get_entry_list`, `set_relationship`, `set_relationships`, `get_relationships`, `set_entry`, `set_entries`, `get_server_info`, `get_user_id`, `get_module_fields`, `seamless_login`, `set_note_attachment`, `get_note_attachment`, `set_document_revision`, `get_document_revision`, `search_by_module`, `get_available_modules`, `get_user_team_id`, `set_campaign_merge`, `get_entries_count`
  - `registerTypes()` — enregistre ~25 types complexes WSDL : `user_auth`, `name_value`, `name_value_list`, `entry_value`, `entry_list`, `get_entry_result_version2`, `get_entry_list_result_version2`, etc.

---

## Interactions
- **Appelé par :** `service/v2/soap.php` et `service/v2/rest.php` (via `service/core/webservice.php`)
- **Appelle :** `$this->serviceClass->registerFunction()`, `$this->serviceClass->registerType()`

---

## Notes
- Ce fichier est la base de l'API v2 — toutes les versions supérieures héritent du même registre (v3, v4 héritent mais ajoutent des fonctions)
- Le même fichier `registry.php` est utilisé pour SOAP et REST v2
