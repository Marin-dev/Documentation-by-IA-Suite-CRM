# 📄 OAuth2AuthCodes.php

**Chemin :** `modules/OAuth2AuthCodes/OAuth2AuthCodes.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Modèle persistant les codes d'autorisation OAuth2 (Authorization Code Flow). Un code d'autorisation est un jeton temporaire échangeable contre un access token. Ce bean gère leur création, validation et révocation.

## Rôle technique

Classe `OAuth2AuthCodes` héritant de `SugarBean` (table `oauth2authcodes`). Implémente la vérification d'expiration et de révocation, la vérification de portée pré-autorisée (`auto_authorize`), et filtre la liste pour les utilisateurs non-admin (uniquement leurs propres codes).

---

## Dépendances clés

- `SugarBean` — classe parente ORM
- `League\OAuth2\Server\RequestTypes\AuthorizationRequest` — type de la requête d'autorisation
- `DBManager` — filtrage dans `create_new_list_query()`
- `$current_user` — filtrage par utilisateur

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `OAuth2AuthCodes` | classe | Modèle des codes d'autorisation OAuth2 |
| `is_revoked()` | méthode | Vérifie si le code est révoqué ou expiré |
| `is_scope_authorized(AuthorizationRequest)` | méthode | Vérifie si les scopes sont pré-autorisés (auto-authorize) |
| `create_new_list_query()` | méthode | Filtre la liste : admin voit tout, utilisateur voit les siens |

## Consommateurs identifiés

- `modules/OAuth2AuthCodes/services/OAuthCodeGrantManager.php` — gestion du flux d'autorisation
- `Api/V8/OAuth2/` — serveur d'autorisation League OAuth2

---

## Relations clés

- **Appelé par :** `OAuthCodeGrantManager`, serveur OAuth2 API V8
- **Appelle :** `SugarBean`, `DBManager`
- **Position dans le flux global :** étape intermédiaire du flux Authorization Code : code créé lors du consentement, consommé lors de l'échange contre un token

---

## Notes

- `disable_row_level_security = true` — pas de filtrage SecurityGroups.
- `is_revoked()` vérifie à la fois le flag `auth_code_is_revoked` ET l'expiration via `\DateTime` (ligne 103).
- `is_scope_authorized()` recherche une entrée existante avec `auto_authorize='1'` pour éviter de redemander le consentement à chaque connexion.
