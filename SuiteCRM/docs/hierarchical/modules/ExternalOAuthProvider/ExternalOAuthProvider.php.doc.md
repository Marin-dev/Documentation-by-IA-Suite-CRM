# 📄 ExternalOAuthProvider.php

**Chemin :** `modules/ExternalOAuthProvider/ExternalOAuthProvider.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Modèle représentant la configuration d'un fournisseur OAuth externe (Google, Microsoft, ou générique). Stocke les paramètres nécessaires pour initier et compléter un flux OAuth : URLs, credentials, scopes, mappings de champs de token. Permet à SuiteCRM d'envoyer des e-mails via Gmail/Outlook en utilisant OAuth.

## Rôle technique

Classe `ExternalOAuthProvider` héritant de `Basic` (table `external_oauth_providers`). Logique ACL identique à `ExternalOAuthConnection`. Expose `getConfigArray()` qui construit la configuration complète pour les connecteurs. Désérialise les champs JSON (scopes, options, mappings).

---

## Dépendances clés

- `Basic` (framework SuiteCRM) — classe parente ORM
- `$sugar_config['site_url']` — construction de l'URI de redirection
- `json_decode()` / `html_entity_decode()` — désérialisation des champs complexes

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `ExternalOAuthProvider` | classe | Configuration d'un fournisseur OAuth externe |
| `getConfigArray()` | méthode | Retourne le tableau de config complet pour les connecteurs |
| `getRedirectURI()` | méthode | Construit l'URI de redirection (pretty_url ou standard) |
| `getScope()` | méthode | Retourne les scopes séparés par espaces |
| `getConfigArray()` renvoie | — | `type`, `client_id/secret`, `redirect_uri`, `authorize_url_options`, `extra_provider_params`, `token_mapping`… |

## Champs principaux

| Champ | Rôle |
|---|---|
| `connector` | Type de connecteur (`Microsoft`, `Google`, `Generic`) |
| `url_authorize` | URL d'autorisation du fournisseur |
| `url_access_token` | URL d'échange de token |
| `scope` | JSON array des scopes demandés |
| `access_token_mapping` | Nom du champ access_token dans la réponse |
| `refresh_token_mapping` | Nom du champ refresh_token dans la réponse |
| `redirect_uri_type` | `pretty_url` ou standard |

---

## Relations clés

- **Appelé par :** `OAuthAuthorizationService::getProviderConfig()`, entrypoints OAuth
- **Appelle :** `Basic`, `json_decode()`, `$sugar_config`
- **Position dans le flux global :** référentiel de configuration des fournisseurs OAuth, consommé par `OAuthAuthorizationService` pour construire les connecteurs

---

## Notes

- `getRedirectURI()` supporte les "pretty URLs" (`/ep/setExternalOAuthToken`) en plus du format standard.
- Les champs `scope`, `authorize_url_options`, `extra_provider_params`, etc. sont stockés en JSON dans la DB et désérialisés via `deserializeMapField()`.
- La logique ACL (admin-only, personal, etc.) est identique à `ExternalOAuthConnection`.
