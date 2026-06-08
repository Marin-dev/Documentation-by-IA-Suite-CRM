# json_server.php

**Chemin :** `json_server.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-28

---

## Rôle
Point d'entrée HTTP pour le serveur JSON-RPC de SuiteCRM (API legacy). Instancie et exécute le serveur JSON-RPC qui expose des méthodes distantes aux clients compatibles.

## Responsabilités
- Vérifier le jeton `sugarEntry`
- Instancier `JsonRPCServer` depuis `service/JsonRPCServer/JsonRPCServer.php`
- Appeler `$jsonServer->run()` pour traiter la requête JSON-RPC entrante

## Dépendances internes
- `service/JsonRPCServer/JsonRPCServer.php` — implémentation du serveur JSON-RPC

## Exports / Points d'entrée
- **Point d'entrée HTTP :** `POST /json_server.php`
- Retourne une réponse JSON-RPC (format JSON)

## Notes techniques
- Ce fichier est une API legacy de SuiteCRM ; la nouvelle API REST V8 est disponible via `Api/V8/`.
- INCONNU : liste des méthodes exposées — à chercher dans `service/JsonRPCServer/`.
