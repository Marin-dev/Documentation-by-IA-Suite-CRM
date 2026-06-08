# json_server.php

**Chemin :** `json_server.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle fonctionnel

Point d'entrée HTTP pour le serveur JSON-RPC de SuiteCRM. Expose une API JSON-RPC pour les appels inter-modules ou les intégrations légères.

**Type :** entrypoint

## Rôle technique

Charge le serveur JSON-RPC depuis `service/JsonRPCServer/JsonRPCServer.php`, instancie `JsonRPCServer` et appelle `run()`. Requiert que `sugarEntry` soit défini.

---

## Dépendances clés

- **Imports principaux :**
  - `service/JsonRPCServer/JsonRPCServer.php` — implémentation du serveur JSON-RPC
- **Sécurité :** bloque si `sugarEntry` non défini (ligne 42)

## Sorties / Comportement

- Exécute `$jsonServer->run()` qui traite la requête JSON-RPC et renvoie la réponse

## Relations clés

- **Appelé par :** composants front-end SuiteCRM ou intégrations externes via appels JSON-RPC
- **Appelle :** `JsonRPCServer::run()`

---

## Points d'attention

- Ce fichier est un simple relais — toute la logique est dans `JsonRPCServer`.
- Distinct de l'API REST V8 (`Api/`) — il s'agit d'un mécanisme JSON-RPC plus ancien.
- Contrairement à `index.php`, ne charge pas `entryPoint.php` explicitement — l'environnement doit être préchargé (INCONNU comment).
