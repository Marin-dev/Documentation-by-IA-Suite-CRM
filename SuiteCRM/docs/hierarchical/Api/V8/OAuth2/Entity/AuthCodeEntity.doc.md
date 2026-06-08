# Fichier : AuthCodeEntity.php

**Chemin :** `Api/V8/OAuth2/Entity/AuthCodeEntity.php`
**Type :** model
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Entité représentant un code d'autorisation OAuth2 (flux `authorization_code`). Implémente l'interface `AuthCodeEntityInterface` de `league/oauth2-server` via composition de traits.

---

## Type

model

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `League\OAuth2\Server\Entities\AuthCodeEntityInterface` | Interface contractuelle du code d'autorisation |
| `League\OAuth2\Server\Entities\Traits\AuthCodeTrait` | Fournit `getRedirectUri()` / `setRedirectUri()` |
| `League\OAuth2\Server\Entities\Traits\EntityTrait` | Fournit `getIdentifier()` / `setIdentifier()` |
| `League\OAuth2\Server\Entities\Traits\TokenEntityTrait` | Fournit la gestion des scopes, du client, de l'expiration et de l'identifiant utilisateur |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `AuthCodeEntity` | classe | Entité de code d'autorisation OAuth2 — aucune logique propre, tout via traits |

---

## Interactions

**Instancié par :**
- `Api/V8/OAuth2/Repository/AuthCodeRepository.php` — méthode `getNewAuthCode()` (ligne 92)

**Utilisé par :**
- `Api/V8/Config/services/middlewares.php` — enregistrement dans le conteneur DI

---

## Notes

- Classe entièrement définie par composition de traits — aucune méthode propre.
- Utilisée uniquement dans le flux `authorization_code` OAuth2.
