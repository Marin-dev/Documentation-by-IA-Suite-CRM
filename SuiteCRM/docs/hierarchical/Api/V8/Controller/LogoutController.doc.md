# 📄 LogoutController.php

**Chemin :** `Api/V8/Controller/LogoutController.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Contrôleur de l'API V8 gérant la déconnexion d'un utilisateur. Il invalide le token d'accès OAuth2 courant et termine la session API.

## ⚙️ Rôle technique
Hérite de `BaseController`. Implémente `__invoke` (invocable directement par Slim). Extrait le `oauth_access_token_id` de la requête via le `ResourceServer` de League OAuth2, puis appelle `LogoutService::logout()` avec ce token. Retourne 200 en cas de succès ou 400 en cas d'erreur.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `Api\V8\Service\LogoutService` — service de déconnexion (révocation du token)
  - `League\OAuth2\Server\ResourceServer` — serveur de ressources OAuth2 (validation du token entrant)
  - `Slim\Http\Request` / `Slim\Http\Response` — objets HTTP Slim

## 📤 Sorties / Exports
- `LogoutController` — classe contrôleur invocable
  - `__invoke(Request, Response): Response` — traite la déconnexion et retourne une réponse JSON:API

## 🔗 Relations clés
- **Appelé par :** routeur Slim via `__invoke` (INCONNU — route exacte non visible dans ce fichier)
- **Appelle :** `ResourceServer::validateAuthenticatedRequest()`, `LogoutService::logout()`
- **Position dans le flux global :** endpoint de fin de session API ; doit être appelé après authentification OAuth2

---

## 💡 Points d'attention
- La validation du token est effectuée directement dans le contrôleur (contrairement aux autres contrôleurs qui passent par le `ParamsMiddleware`). Cela signifie que cet endpoint contourne la chaîne de middleware standard de paramètres.
- Si `validateAuthenticatedRequest` lève une exception (token invalide ou expiré), une réponse 400 est renvoyée — le code HTTP devrait idéalement être 401 pour une erreur d'authentification.
