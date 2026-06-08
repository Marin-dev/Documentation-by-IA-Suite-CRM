# 📄 OAuthAuthorizationService.php

**Chemin :** `modules/ExternalOAuthConnection/services/OAuthAuthorizationService.php`
**Type :** PHP — service
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Service principal du système OAuth externe. Orchestre le flux complet d'autorisation OAuth vers des fournisseurs tiers (Google, Microsoft, Generic) : redirection vers le fournisseur, récupération du token après consentement, rafraîchissement du token expiré, et gestion des erreurs associées.

## Rôle technique

Classe `OAuthAuthorizationService` (non héritante). Instancie dynamiquement le connecteur approprié selon le `type` du fournisseur (`Microsoft`, `Google`, `Generic`). Supporte l'extension via un fichier custom `externaloauthproviders.ext.php`. Toutes les opérations DB passent par `ExternalOAuthConnection`.

---

## Dépendances clés

- `League\OAuth2\Client\Provider\Exception\IdentityProviderException` — gestion des erreurs
- `League\OAuth2\Client\Token\AccessTokenInterface` — interface du token
- `provider/ExternalOAuthProviderConnectorInterface.php` — interface connecteur
- `provider/Generic/GenericOAuthProviderConnector.php` — connecteur générique
- `provider/Microsoft/MicrosoftOAuthProviderConnector.php` — connecteur Microsoft
- `provider/Google/GoogleOAuthProviderConnector.php` — connecteur Google
- `BeanFactory::getBean('ExternalOAuthProvider', ...)` — chargement de la config fournisseur
- `BeanFactory::getBean('ExternalOAuthConnection', ...)` — chargement de la connexion
- `$log` — journalisation

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `OAuthAuthorizationService` | classe | Service OAuth externe |
| `hasProvider($providerId)` | méthode | Vérifie si un fournisseur est configuré et opérationnel |
| `getProvider($providerId)` | méthode | Instancie le connecteur approprié |
| `authorizationRedirect($providerId, $clientId, $clientSecret)` | méthode | Redirige vers l'URL d'autorisation du fournisseur |
| `getAccessToken($providerId, $code)` | méthode | Échange un code d'autorisation contre un token |
| `refreshConnectionToken(ExternalOAuthConnection)` | méthode | Rafraîchit le token d'une connexion existante |
| `hasConnectionTokenExpired(ExternalOAuthConnection)` | méthode | Vérifie si le token a expiré |
| `refreshExpiredOAuthToken($oAuthConnectionId)` | méthode | Vérifie et rafraîchit automatiquement si expiré |
| `mapToken($providerId, $token)` | méthode | Mappe les champs du token selon la config fournisseur |
| `getExternalOauthProvidersConnectors()` | méthode | Retourne la liste des connecteurs (extensible via custom) |

---

## Relations clés

- **Appelé par :** `entrypoint/redirectToExternalOAuth.php`, `entrypoint/setExternalOAuthToken.php`, modules de messagerie (INCONNU)
- **Appelle :** `ExternalOAuthProvider::getConfigArray()`, connecteurs OAuth, `ExternalOAuthConnection::save()`
- **Position dans le flux global :** orchestrateur central du OAuth externe, appelé lors de la connexion à Gmail/Outlook pour l'envoi d'e-mails

---

## Notes

- L'extension des connecteurs se fait via `custom/application/Ext/ExternalOAuthProviders/externaloauthproviders.ext.php` (ligne 429).
- `refreshConnectionToken()` remet à jour les tokens dans `ExternalOAuthConnection` ET restaure les valeurs décryptées après sauvegarde (car la sauvegarde chiffre les tokens).
- `hasConnectionTokenExpired()` compare `expires_in` (timestamp Unix) avec `time()`.
- Les erreurs `IdentityProviderException` sont loguées avec le corps de la réponse HTTP (ligne 388-396).
