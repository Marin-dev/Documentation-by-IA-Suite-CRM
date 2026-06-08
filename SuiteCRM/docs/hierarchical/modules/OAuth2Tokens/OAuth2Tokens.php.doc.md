# 📄 OAuth2Tokens.php

**Chemin :** `modules/OAuth2Tokens/OAuth2Tokens.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Modèle persistant les tokens OAuth2 (access tokens et refresh tokens) de l'API V8 SuiteCRM. Chaque token représente une session d'accès accordée à un client OAuth2 pour un utilisateur donné.

## Rôle technique

Classe `OAuth2Tokens` héritant de `SugarBean` (table `oauth2tokens`). Filtre la liste en vue pour les non-admins (accès limité aux propres tokens). Fournit une méthode utilitaire `getNowDateString()` pour les opérations DB de comparaison de dates.

---

## Dépendances clés

- `SugarBean` — classe parente ORM
- `DBManager` — conversion de date dans `getNowDateString()`
- `$current_user` — filtrage dans `create_new_list_query()`

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `OAuth2Tokens` | classe | Modèle des tokens OAuth2 V8 |
| `getNowDateString()` | méthode statique | Retourne la représentation DB de la date/heure courante |
| `create_new_list_query()` | méthode | Filtre : admin voit tout, utilisateur voit ses tokens uniquement |

## Champs principaux

| Champ | Rôle |
|---|---|
| `token_type` | Type de token (Bearer…) |
| `token_is_revoked` | Flag de révocation |
| `access_token` | Valeur du token d'accès |
| `access_token_expires` | Date d'expiration de l'access token |
| `refresh_token` | Valeur du refresh token |
| `refresh_token_expires` | Date d'expiration du refresh token |
| `scopes` | Scopes accordés |
| `client` | ID du client OAuth2 associé |

---

## Relations clés

- **Appelé par :** serveur OAuth2 API V8 (`Api/V8/OAuth2/`)
- **Appelle :** `SugarBean`, `DBManager`
- **Position dans le flux global :** persistance des tokens après échange du code d'autorisation ou des credentials client

---

## Notes

- `disable_row_level_security = true`.
- Le filtre liste par utilisateur est identique à celui d'`OAuth2AuthCodes` — pattern cohérent.
- Aucune logique de révocation dans ce fichier : elle est gérée par les repositories League OAuth2 (INCONNU — non lu).
