# Fichier : RefreshTokenEntity.php

**Chemin :** `Api/V8/OAuth2/Entity/RefreshTokenEntity.php`
**Type :** model
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Entité représentant un jeton de rafraîchissement OAuth2. Implémente l'interface `RefreshTokenEntityInterface` de `league/oauth2-server` via composition de traits — permet de renouveler un `access_token` expiré sans authentification complète.

---

## Type

model

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `League\OAuth2\Server\Entities\RefreshTokenEntityInterface` | Interface contractuelle du refresh token |
| `League\OAuth2\Server\Entities\Traits\RefreshTokenTrait` | Fournit `getAccessToken()` / `setAccessToken()` |
| `League\OAuth2\Server\Entities\Traits\EntityTrait` | Fournit `getIdentifier()` / `setIdentifier()` |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `RefreshTokenEntity` | classe | Entité de refresh token OAuth2 — aucune logique propre, tout via traits |

---

## Interactions

**Instancié par :**
- `Api/V8/OAuth2/Repository/RefreshTokenRepository.php` — méthode `getNewRefreshToken()` (ligne 31)

**Utilisé par :**
- `Api/V8/Config/services/middlewares.php` — enregistrement dans le conteneur DI

---

## Notes

- Classe entièrement définie par composition de traits — aucune méthode propre.
