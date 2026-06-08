# Fichier : UserEntity.php

**Chemin :** `Api/V8/OAuth2/Entity/UserEntity.php`
**Type :** model
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Entité représentant un utilisateur authentifié dans le contexte OAuth2. Implémente `UserEntityInterface` de `league/oauth2-server`. Stocke uniquement l'identifiant de l'utilisateur SuiteCRM et l'expose via `getIdentifier()`.

---

## Type

model

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `League\OAuth2\Server\Entities\UserEntityInterface` | Interface contractuelle de l'entité utilisateur OAuth2 |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `UserEntity` | classe | Entité utilisateur OAuth2 portant uniquement l'identifiant SuiteCRM |
| `__construct(string $userId)` | méthode publique | Initialise l'entité avec l'ID utilisateur SuiteCRM |
| `getIdentifier()` | méthode publique | Retourne l'ID utilisateur (implémentation de `UserEntityInterface`) |

---

## Interactions

**Instancié par :**
- `Api/V8/OAuth2/Repository/UserRepository.php` — méthode `getUserEntityByUserCredentials()` (ligne 50)

**Utilisé par :**
- `Api/V8/Config/services/middlewares.php` — enregistrement dans le conteneur DI

---

## Notes

- Classe minimaliste : stocke uniquement l'UUID de l'utilisateur SuiteCRM.
- Ne stocke ni nom, ni email, ni rôles — seul l'identifiant est transmis au serveur d'autorisation OAuth2.
