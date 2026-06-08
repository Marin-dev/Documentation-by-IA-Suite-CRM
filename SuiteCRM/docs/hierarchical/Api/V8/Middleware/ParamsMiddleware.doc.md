# 📄 ParamsMiddleware.php

**Chemin :** `Api/V8/Middleware/ParamsMiddleware.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Middleware Slim de l'API V8 responsable de deux tâches critiques avant l'exécution d'un contrôleur : (1) résoudre et positionner l'utilisateur courant (`$GLOBALS['current_user']`) à partir du token OAuth2, et (2) valider et hydrater l'objet de paramètres de la requête (`BaseParam`) qui sera injecté dans l'action du contrôleur.

## ⚙️ Rôle technique
Implémente le pattern middleware PSR-15 / Slim avec `__invoke(Request, Response, callable $next)`. Récupère le token OAuth2 depuis l'attribut de requête `oauth_access_token_id`, charge l'utilisateur via `BeanManager`, valide qu'il est actif, puis configure l'objet `BaseParam` avec les paramètres fusionnés (route + query + body). En cas d'erreur, retourne une réponse 400 JSON avec log fatal. En cas de succès, ajoute l'objet `params` comme attribut de requête et appelle `$next`.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `Api\V8\JsonApi\Response\ErrorResponse` — objet de réponse d'erreur JSON:API
  - `Api\V8\Param\BaseParam` — objet de paramètres à hydrater (injecté par `ParamsMiddlewareFactory`)
  - `Api\V8\BeanDecorator\BeanManager` (`Api/V8/BeanDecorator/BeanManager.php`) — accès aux beans SuiteCRM
  - `LoggerManager` — logger SuiteCRM pour les erreurs fatales
  - `Slim\Http\Request` / `Slim\Http\Response` — objets HTTP Slim
- **Attribut de requête consommé :** `oauth_access_token_id` (positionné par le middleware OAuth2 en amont)
- **Variable globale écrite :** `$GLOBALS['current_user']`

## 📤 Sorties / Exports
- `ParamsMiddleware` — classe middleware invocable
  - `__invoke(Request, Response, callable $next): Response` — exécute le middleware, enrichit la requête avec `params`, propage vers `$next`
- **Attribut de requête produit :** `params` (objet `BaseParam` hydraté)
- **Consommateurs identifiés dans le repo :**
  - `Api/V8/Factory/ParamsMiddlewareFactory.php` (instanciateur)
  - `Api/V8/Config/routes.php` (via la factory, attaché aux routes)

## 🔗 Relations clés
- **Appelé par :** chaîne de middleware Slim, déclenché par `ParamsMiddlewareFactory::bind()` sur chaque route configurée
- **Appelle :** `BeanManager::newBeanSafe('OAuth2Tokens')`, `BeanManager::getBeanSafe('Users', ...)`, `BaseParam::configure()`, `LoggerManager::getLogger()->fatal()`
- **Position dans le flux global :** s'exécute après le middleware OAuth2 (qui positionne `oauth_access_token_id`) et avant les contrôleurs ; alimente la `SuiteInvocationStrategy` en attribut `params`

---

## 💡 Points d'attention
- Si l'utilisateur n'est pas actif (`!$currentUser->isEnabled()`), une `RuntimeException('Not found')` est levée — le message "Not found" est volontairement vague pour raisons de sécurité.
- Les paramètres sont fusionnés dans l'ordre : route args > query params > parsed body. Un paramètre de body peut écraser un paramètre de route du même nom — point d'attention pour la sécurité.
- Les valeurs de route sont décodées via `urldecode()` sauf si ce sont des booléens (ligne 100-103).
- Les erreurs sont loguées en niveau `fatal` via `LoggerManager` avec la trace complète — informations potentiellement sensibles dans les logs.
- `#[\AllowDynamicProperties]` présent pour compatibilité PHP 8.2+.
