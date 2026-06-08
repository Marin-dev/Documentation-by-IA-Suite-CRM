# 📄 MicrosoftOAuthProviderConnector.php

**Chemin :** `modules/ExternalOAuthConnection/provider/Microsoft/MicrosoftOAuthProviderConnector.php`
**Type :** PHP — connecteur OAuth
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Connecteur OAuth spécifique à Microsoft (Azure AD / Microsoft 365). Configure les paramètres par défaut pour le flux OAuth Microsoft et mappe le token retourné dans le format interne SuiteCRM.

## Rôle technique

Classe `MicrosoftOAuthProviderConnector` héritant de `ExternalOAuthProviderConnector`. Surcharge `getExtraProviderParams()` pour vider `urlResourceOwnerDetails` (non requis pour Microsoft). Le mapping de token inclut `token_type` via `values.token_type`.

---

## Notes

- `urlResourceOwnerDetails` est mis à `''` par défaut (Microsoft ne requiert pas ce endpoint dans le flux standard).
- Le mapping dynamique (`token_mapping` DB) est prioritaire sur les defaults.
- Les URLs `urlAuthorize` et `urlAccessToken` doivent être configurées dans `ExternalOAuthProvider` (ex: `https://login.microsoftonline.com/{tenant}/oauth2/v2.0/authorize`).
