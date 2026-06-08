# 📄 OAuthCodeGrantManager.php

**Chemin :** `modules/OAuth2AuthCodes/services/OAuthCodeGrantManager.php`
**Type :** PHP — service
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Service orchestrant le flux Authorization Code OAuth2. Gère la persistance temporaire en session des paramètres de la requête d'autorisation (entre la redirection vers la page de login et le retour de consentement), la reconstruction de la requête depuis la session, et la validation du consentement utilisateur.

## Rôle technique

Classe `OAuthCodeGrantManager` (non héritante). Sérialise/désérialise les paramètres OAuth2 dans `$_SESSION`. Intègre un mécanisme anti-CSRF via `oauth2_authcode_hash` et `oauth2_authcode_process_id`. Compatible avec PKCE (code_challenge).

---

## Dépendances clés

- `Api\V8\OAuth2\Entity\UserEntity` — entité utilisateur OAuth2
- `League\OAuth2\Server\AuthorizationServer` — serveur d'autorisation
- `League\OAuth2\Server\RequestTypes\AuthorizationRequest` — type de requête
- `Psr\Http\Message\ServerRequestInterface` — interface PSR-7
- `$_SESSION` — stockage des paramètres de la requête
- `$current_user` — utilisateur courant pour `loadAuthorizationRequest()`

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `OAuthCodeGrantManager` | classe | Service de gestion du flux Authorization Code |
| `saveRequestToSession()` | méthode | Persiste les paramètres OAuth2 + hash anti-CSRF en session |
| `loadAuthorizationRequest()` | méthode | Reconstruit la `AuthorizationRequest` depuis la session |
| `cleanupSession()` | méthode | Nettoie toutes les variables de session OAuth2 |
| `validateConfirmationRequest()` | méthode | Valide le hash et le process_id anti-CSRF |

## Consommateurs identifiés

- `modules/OAuth2AuthCodes/views/view.authorize.php` — INCONNU (non lu)
- `Api/V8/OAuth2/` — INCONNU (non lu)

---

## Relations clés

- **Appelé par :** vue d'autorisation OAuth2, serveur API V8
- **Appelle :** `League\OAuth2\Server\AuthorizationServer`, `UserEntity`
- **Position dans le flux global :** pont entre la page de login SuiteCRM et le serveur OAuth2, maintient l'état de la requête pendant l'authentification

---

## Notes

- Variables de session utilisées : `oauth2_authcode_response_type`, `client_id`, `redirect_uri`, `state`, `scope`, `code_challenge`, `code_challenge_method`, `logout`, `hash`, `process_id`.
- `validateConfirmationRequest()` vérifie que `confirmed` vaut `'once'`, `'always'` ou `'abort'` (ligne 177) — toute autre valeur lève une `InvalidArgumentException`.
- Le flag `oauth2_authcode_logout` détecte si l'utilisateur vient de la page Login (via `HTTP_REFERER`).
