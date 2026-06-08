# 📄 GoogleOAuthProviderConnector.php

**Chemin :** `modules/ExternalOAuthConnection/provider/Google/GoogleOAuthProviderConnector.php`
**Type :** PHP — connecteur OAuth
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Connecteur OAuth spécifique à Google. Configure les URLs Google OAuth2 par défaut et force les paramètres requis pour obtenir un refresh_token (`access_type=offline`, `prompt=consent`).

## Rôle technique

Classe `GoogleOAuthProviderConnector` héritant de `ExternalOAuthProviderConnector`. Surcharge les URLs par défaut (Google OAuth2 endpoints), les options d'autorisation, et nettoie le paramètre déprécié `approval_prompt` de l'URL finale.

---

## URLs par défaut injectées

| Paramètre | Valeur |
|---|---|
| `urlAuthorize` | `https://accounts.google.com/o/oauth2/auth` |
| `urlAccessToken` | `https://oauth2.googleapis.com/token` |
| `urlResourceOwnerDetails` | `https://www.googleapis.com/oauth2/v2/userinfo` |

## Notes

- `access_type=offline` et `prompt=consent` sont forcés pour garantir l'obtention du refresh_token Google.
- `approval_prompt` est explicitement supprimé pour éviter les conflits avec `prompt`.
- Le mapping par défaut inclut `token_type` via chemin `values.token_type`.
