# Fichier : AccessTokenEntity.php

**Chemin :** `Api/V8/OAuth2/Entity/AccessTokenEntity.php`
**Type :** model
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Entité représentant un jeton d'accès OAuth2 dans le contexte de l'API V8 de SuiteCRM. Implémente l'interface `AccessTokenEntityInterface` de la bibliothèque `league/oauth2-server` en combinant trois traits standards.

---

## Type

model

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `League\OAuth2\Server\Entities\AccessTokenEntityInterface` | Interface contractuelle du token d'accès |
| `League\OAuth2\Server\Entities\Traits\AccessTokenTrait` | Fournit la méthode `convertToJWT()` et la gestion de la clé privée |
| `League\OAuth2\Server\Entities\Traits\EntityTrait` | Fournit `getIdentifier()` / `setIdentifier()` |
| `League\OAuth2\Server\Entities\Traits\TokenEntityTrait` | Fournit la gestion des scopes, du client, de l'expiration et de l'identifiant utilisateur |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `AccessTokenEntity` | classe | Entité de token d'accès OAuth2 — aucune logique propre, tout via traits |

---

## Interactions

**Instancié par :**
- `Api/V8/OAuth2/Repository/AccessTokenRepository.php` — injecté dans le constructeur (ligne 33)

**Utilisé par :**
- `Api/V8/Config/services/middlewares.php` — enregistrement dans le conteneur DI

---

## Notes

- Classe entièrement définie par composition de traits — aucune méthode propre.
- Conforme au contrat `league/oauth2-server` version 8.x (interface `AccessTokenEntityInterface`).
