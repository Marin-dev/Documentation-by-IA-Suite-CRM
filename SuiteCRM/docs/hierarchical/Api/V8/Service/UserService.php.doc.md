# 📄 UserService.php

**Chemin :** `Api/V8/Service/UserService.php`
**Type :** PHP (service)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Service de récupération de l'utilisateur courant authentifié. Résout l'utilisateur à partir du token OAuth2 contenu dans la requête, vérifie son statut actif et retourne ses données avec ses attributs et relations au format JSON:API.

**Type :** service

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `Api\V8\BeanDecorator\BeanManager` | Accès aux beans `OAuth2Tokens` et `Users` |
| `Api\V8\JsonApi\Helper\{Attribute,Relationship}ObjectHelper` | Construction des attributs et relations JSON:API |
| `Api\V8\JsonApi\Response\{AttributeResponse, DataResponse, DocumentResponse}` | Réponses JSON:API |
| `Slim\Http\Request` | Accès à l'attribut `oauth_access_token_id` |
| `RuntimeException` | Exception si utilisateur inactif |

---

## Exports / Symboles principaux

**Classe :** `Api\V8\Service\UserService`

| Méthode | Signature | Description |
|---|---|---|
| `__construct` | `(BeanManager, AttributeObjectHelper, RelationshipObjectHelper)` | Injection des 3 dépendances |
| `getCurrentUser` | `(Request $request): DocumentResponse` | Retourne les données de l'utilisateur courant |

---

## Flux de `getCurrentUser`

1. Crée un bean `OAuth2Tokens` vide
2. Récupère le token via `retrieve_by_string_fields(['access_token' => $request->getAttribute('oauth_access_token_id')])`
3. Récupère l'utilisateur via `BeanManager::getBeanSafe('Users', $oauth2Token->assigned_user_id)`
4. Vérifie `$currentUser->isEnabled()` → `RuntimeException('Not found')` si inactif
5. Prépare les données via `$currentUser->toArray()` et **supprime `user_hash`** (mot de passe hashé)
6. Construit `DataResponse` avec `AttributeResponse` + `RelationshipObjectHelper::getRelationships`
7. Retourne `DocumentResponse`

---

## Interactions

- **Appelé par :** `UserController` (route `GET /V8/current-user`)
- **Consommé dans DI :** `Api/V8/Config/services/services.php`
- **Appelle :** `BeanManager::newBeanSafe`, `BeanManager::getBeanSafe`, `AttributeObjectHelper`, `RelationshipObjectHelper`

---

## Notes

- `user_hash` est explicitement supprimé (ligne 113 : `unset($currentUserData['user_hash'])`) — protection de sécurité : le hash du mot de passe n'est jamais exposé via l'API.
- L'attribut `oauth_access_token_id` est injecté dans la requête Slim par le `ResourceServerMiddleware` (league/oauth2-server).
- `guard` `sugarEntry` présent (lignes 51-54).
- `RuntimeException('Not found')` pour un utilisateur désactivé — message volontairement vague pour ne pas révéler si le compte existe.
