# 📄 GenericOAuthProviderConnector.php

**Chemin :** `modules/ExternalOAuthConnection/provider/Generic/GenericOAuthProviderConnector.php`
**Type :** PHP — connecteur OAuth
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Connecteur OAuth générique utilisable avec n'importe quel fournisseur OAuth2 standard. Utilise la configuration personnalisée définie dans `ExternalOAuthProvider` (URLs, scopes, mappings).

## Rôle technique

Classe `GenericOAuthProviderConnector` héritant de `ExternalOAuthProviderConnector`. Implémente `mapAccessToken()` en utilisant le mapping dynamique si défini, sinon retourne les 3 champs standard. Note : `getProviderType()` retourne incorrectement `'Microsoft'` (bug probable — devrait retourner `'Generic'`).

---

## Notes

- `getProviderType()` retourne `'Microsoft'` — incohérence probable avec l'inscription dans `OAuthAuthorizationService` comme type `'Generic'`.
- Si aucun `tokenMapping` n'est défini dans la config DB, retourne : `access_token`, `expires_in`, `refresh_token`.
