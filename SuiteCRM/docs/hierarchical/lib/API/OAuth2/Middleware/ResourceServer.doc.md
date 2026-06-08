# 📄 ResourceServer.php (Middleware)

**Chemin :** `lib/API/OAuth2/Middleware/ResourceServer.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Middleware Slim 3 de validation des tokens OAuth2 sur chaque requête API entrante. Vérifie le Bearer token, identifie et charge l'utilisateur SuiteCRM associé dans `$GLOBALS['current_user']`.

## ⚙️ Rôle technique
Callable PSR-7 (`__invoke(Request, Response, callable $next)`). Pour chaque requête (sauf les routes exemptées : `oauth/access_token` et `v8/swagger.json`), valide le token via `OAuthResourceServer::validateAuthenticatedRequest()`. Charge ensuite l'utilisateur depuis `oauth_user_id` ou `oauth_client_id` (pour les grants sans utilisateur). Vérifie que l'utilisateur est actif (`status !== 'Inactive'`).

---

## 📥 Entrées / Dépendances
- `League\OAuth2\Server\ResourceServer as OAuthResourceServer`
- `League\OAuth2\Server\Exception\OAuthServerException`
- `SuiteCRM\API\v8\Exception\NotAllowedException`
- `SuiteCRM\Enumerator\ExceptionCode`
- `SuiteCRM\Utility\SuiteLogger`
- `\User`, `\OAuth2Clients` (classes SugarCRM natives)
- `$GLOBALS['current_user']` — variable globale SuiteCRM

## 📤 Sorties / Exports
- `ResourceServer` — classe (middleware)
  - `__invoke(Request, Response, callable $next): Response`
- **Consommateurs identifiés :** enregistré dans le pipeline Slim middleware (INCONNU — containers v8)

## 🔗 Relations clés
- **Appelé par :** pipeline Slim pour chaque requête
- **Position dans le flux global :** garde d'authentification avant les contrôleurs de l'API

---

## 💡 Points d'attention
- Les routes `oauth/access_token` et `v8/swagger.json` sont exemptées d'authentification (liste codée en dur `$ROUTES_EXEMPT_FROM_AUTH`).
- Toute exception OAuth2 est loggée et transformée en réponse HTTP appropriée — les erreurs PHP inattendues deviennent des 500 avec message `unknown_error`.
- Le fallback sur `OAuth2Clients.assigned_user_id` permet les grants de type `client_credentials` sans utilisateur spécifique — l'utilisateur doit être actif dans SuiteCRM.
