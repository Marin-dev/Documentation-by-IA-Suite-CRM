# 📄 ExternalOAuthProviderConnector.php

**Chemin :** `modules/ExternalOAuthConnection/provider/ExternalOAuthProviderConnector.php`
**Type :** PHP — classe abstraite
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Classe de base abstraite pour tous les connecteurs OAuth externes. Implémente la logique commune : construction du provider League OAuth2, obtention/rafraîchissement de tokens, résolution des credentials depuis la session ou la config DB, et mapping dynamique des champs de token.

## Rôle technique

Classe abstraite `ExternalOAuthProviderConnector` implémentant `ExternalOAuthProviderConnectorInterface`. Utilise `League\OAuth2\Client\Provider\GenericProvider` pour toutes les opérations OAuth. Les sous-classes n'ont à implémenter que `mapAccessToken()` et `getProviderType()`.

---

## Dépendances clés

- `League\OAuth2\Client\Provider\GenericProvider` — provider OAuth2 générique
- `League\OAuth2\Client\Provider\AbstractProvider` — type parent
- `BeanFactory::getBean('ExternalOAuthProvider', ...)` — chargement config DB
- `$_SESSION['external_oauth_client_id/secret']` — credentials temporaires
- `$_SESSION['oauth2state']` — anti-CSRF state

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `ExternalOAuthProviderConnector` | classe abstraite | Base des connecteurs OAuth externes |
| `getProvider($clientId, $clientSecret)` | méthode | Construit le GenericProvider League |
| `getAuthorizeURL($clientId, $clientSecret)` | méthode | Génère l'URL d'autorisation + state session |
| `getAccessToken($code)` | méthode | Échange le code contre un token |
| `refreshAccessToken($refreshToken)` | méthode | Rafraîchit un token |
| `mapTokenDynamically($token, $tokenMapping)` | méthode protégée | Mappe le token selon config |
| `getArrayValue($data, $path)` | méthode | Accès à un chemin en notation pointée dans un tableau |

---

## Relations clés

- **Étendue par :** `GenericOAuthProviderConnector`, `MicrosoftOAuthProviderConnector`, `GoogleOAuthProviderConnector`
- **Consommée par :** `OAuthAuthorizationService`
- **Appelle :** `BeanFactory::getBean('ExternalOAuthProvider')`, `League\OAuth2\Client`

---

## Notes

- Les credentials sont résolus dans l'ordre : session > paramètre > config DB (lignes 213-219).
- `refreshAccessToken()` avale les `IdentityProviderException` (retourne `null`) — les erreurs doivent être gérées par l'appelant.
