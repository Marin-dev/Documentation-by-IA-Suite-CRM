# JsonRPCServer.php

## Rôle
Serveur JSON-RPC de SuiteCRM : reçoit les requêtes POST JSON-RPC, authentifie l'utilisateur via session PHP, route la méthode demandée vers `JsonRPCServerCalls`, encode la réponse et la renvoie au client.

## Responsabilités
- Initialiser la session PHP et vérifier la langue courante
- Rejeter les requêtes GET (API dépréciée)
- Valider la structure JSON-RPC (champs `method` et `id` obligatoires)
- Authentifier l'utilisateur via `JsonRPCServerUtils::authenticate()`
- Dispatcher l'appel de méthode sur `JsonRPCServerCalls`
- Encoder la réponse JSON et appeler `sugar_cleanup()`

## Dépendances internes
- `soap/SoapHelperFunctions.php` — fonctions helpers SOAP (ex. `insert_charset_header`)
- `include/json_config.php` — utilitaire JSON (`getJSONobj`)
- `include/utils.php` — `get_current_language`, `sugar_cleanup`
- `service/JsonRPCServer/JsonRPCServerUtils.php` — authentification et construction de WHERE
- `service/JsonRPCServer/JsonRPCServerCalls.php` — implémentation des méthodes RPC exposées

## Exports / Points d'entrée
- `JsonRPCServer` — classe — point d'entrée principal
- `JsonRPCServer::run()` — méthode publique — appelée par le script d'entrée du module JSON-RPC

## Notes techniques
- Utilise `ob_start` / `ob_end_flush` pour bufferiser la sortie avant envoi
- Les requêtes GET retournent une erreur `DEPRECATED API` (ligne 111)
- Le dispatch de méthode utilise `method_exists` + `call_user_func` de manière dynamique : toute méthode publique de `JsonRPCServerCalls` est potentiellement exposable
