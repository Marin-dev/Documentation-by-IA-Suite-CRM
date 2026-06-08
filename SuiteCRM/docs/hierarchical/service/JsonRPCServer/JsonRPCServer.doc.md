# JsonRPCServer.php

**Chemin :** `service/JsonRPCServer/JsonRPCServer.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Serveur JSON-RPC interne de SuiteCRM. Reçoit les requêtes POST JSON-RPC, authentifie l'utilisateur via la session PHP, route vers la méthode de `JsonRPCServerCalls`, et retourne la réponse encodée en JSON. Utilisé par les interfaces JavaScript internes (ListView, etc.) et non par l'API publique.

**Type :** service / entrypoint

---

## Dépendances clés
- `soap/SoapHelperFunctions.php` — fonctions helpers SOAP
- `include/json_config.php` — configuration JSON
- `include/utils.php` — utilitaires
- `service/JsonRPCServer/JsonRPCServerUtils.php` — authentification et construction WHERE
- `service/JsonRPCServer/JsonRPCServerCalls.php` — méthodes disponibles (`retrieve`, `query`)
- `getJSONobj()` — helper global de parsing JSON

---

## Exports/Symboles principaux
- `JsonRPCServer` — classe principale
  - `run()` — point d'entrée principal : authentifie, route, encode la réponse
  - `processRequest()` — traitement privé : décode la requête, valide les champs `method` et `id`, dispatche

---

## Interactions
- **Appelé par :** `json_server.php` (racine du projet) — INCONNU : non lu mais probable
- **Appelle :** `JsonRPCServerUtils->authenticate()`, `JsonRPCServerCalls->{method}()`

---

## Notes
- Les requêtes GET sont refusées avec `'error_msg' => 'DEPRECATED API'` (ligne 111)
- L'authentification repose sur `$_SESSION['unique_key']` vs `$sugar_config['unique_key']` — clé de session interne SuiteCRM (pas de token API)
- `session_save_path` configuré si `$sugar_config['session_dir']` défini (ligne 96-98)
- Seules les méthodes existantes dans `JsonRPCServerCalls` sont routées — pas de reflection dynamique
