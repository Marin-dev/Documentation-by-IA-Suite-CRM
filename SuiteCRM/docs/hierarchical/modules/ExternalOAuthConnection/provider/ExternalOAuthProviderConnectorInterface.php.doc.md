# 📄 ExternalOAuthProviderConnectorInterface.php

**Chemin :** `modules/ExternalOAuthConnection/provider/ExternalOAuthProviderConnectorInterface.php`
**Type :** PHP — interface
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Interface définissant le contrat que tout connecteur OAuth externe doit respecter. Garantit l'interopérabilité entre les connecteurs Google, Microsoft, Generic et tout connecteur custom.

## Rôle technique

Interface PHP `ExternalOAuthProviderConnectorInterface`. Définit les méthodes pour obtenir l'URL d'autorisation, échanger un code contre un token, rafraîchir un token et mapper le token dans le format interne SuiteCRM.

---

## Exports / Symboles principaux

| Méthode | Rôle |
|---|---|
| `getProviderID()` | Retourne l'ID du fournisseur |
| `getProviderType()` | Retourne le type du connecteur |
| `getAuthorizeURL($clientId, $clientSecret)` | URL d'autorisation |
| `getAccessToken($code)` | Échange code → token |
| `refreshAccessToken($refreshToken)` | Rafraîchit le token |
| `mapAccessToken($token)` | Mappe le token au format interne |
| `getProviderConfig()` | Configuration du fournisseur |

---

## Relations clés

- **Implémentée par :** `ExternalOAuthProviderConnector` (abstraite), `GenericOAuthProviderConnector`, `MicrosoftOAuthProviderConnector`, `GoogleOAuthProviderConnector`
- **Consommée par :** `OAuthAuthorizationService`
