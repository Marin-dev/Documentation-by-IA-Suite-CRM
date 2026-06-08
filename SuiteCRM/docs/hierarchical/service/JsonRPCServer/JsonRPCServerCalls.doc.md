# JsonRPCServerCalls.php

**Chemin :** `service/JsonRPCServer/JsonRPCServerCalls.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Fournit les méthodes JSON-RPC disponibles pour les clients internes SuiteCRM. Expose deux opérations : récupération d'un bean individuel (`retrieve`) et requête de liste de beans avec conditions (`query`). Utilisé par les vues JavaScript pour charger des données CRM.

**Type :** service / controller

---

## Dépendances clés
- `soap/SoapHelperFunctions.php` — helpers
- `include/json_config.php` — `json_config` (sérialisation des beans)
- `include/utils.php` — utilitaires
- `service/JsonRPCServer/JsonRPCServerUtils.php` — `constructWhere()`
- `BeanFactory` — chargement des beans
- `DBManagerFactory` — accès base de données

---

## Exports/Symboles principaux
- `JsonRPCServerCalls` — classe de méthodes RPC
  - `retrieve($request_id, $params)` — charge un bean par module+id via `BeanFactory::getBean()`, retourne via `json_config->populateBean()`
  - `query($request_id, $params)` — liste des beans avec conditions, tri, limite et filtrage des champs ; supporte plusieurs modules simultanément

---

## Interactions
- **Appelé par :** `JsonRPCServer->processRequest()`
- **Appelle :** `BeanFactory::getBean()`, `json_config::populateBean()`, `json_config::listFilter()`, `JsonRPCServerUtils::constructWhere()`, `$focus->get_list()`

---

## Notes
- `$sugar_config['list_max_entries_per_page']` est forcé à 31 minimum pour les queries (ligne 100-103)
- Les champs `enum` sont traduits via `$app_list_strings` (ligne 172-186)
- Les champs `sensitive` sont filtrés (ligne 168-170)
- `query()` supporte un tableau `modules` pour des requêtes multi-module (ligne 122-153)
- La gestion de `emailAddress->handleLegacyRetrieve()` pour les emails (ligne 160-162)
