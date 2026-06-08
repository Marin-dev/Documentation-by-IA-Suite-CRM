# Fichier : ClientEntity.php

**Chemin :** `Api/V8/OAuth2/Entity/ClientEntity.php`
**Type :** model
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Entité représentant un client OAuth2 enregistré dans SuiteCRM. Implémente l'interface `ClientEntityInterface` de `league/oauth2-server` et ajoute des setters pour permettre l'injection des données du client récupérées depuis la base de données.

---

## Type

model

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `League\OAuth2\Server\Entities\ClientEntityInterface` | Interface contractuelle du client OAuth2 |
| `League\OAuth2\Server\Entities\Traits\ClientTrait` | Fournit les propriétés `$name`, `$redirectUri`, `$isConfidential` |
| `League\OAuth2\Server\Entities\Traits\EntityTrait` | Fournit `getIdentifier()` / `setIdentifier()` |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `ClientEntity` | classe | Entité client OAuth2 avec setters personnalisés |
| `setName(string $name)` | méthode publique | Définit le nom du client |
| `getName()` | méthode publique | Retourne le nom du client |
| `setRedirectUri(string $uri)` | méthode publique | Définit l'URI de redirection |
| `getRedirectUri()` | méthode publique | Retourne l'URI de redirection |
| `setIsConfidential(bool $confidential)` | méthode publique | Définit si le client est confidentiel |

---

## Interactions

**Instancié par :**
- `Api/V8/OAuth2/Repository/ClientRepository.php` — injecté dans le constructeur (ligne 26) et populé dans `getClientEntity()` (lignes 39-42)

**Utilisé par :**
- `Api/V8/Config/services/middlewares.php` — enregistrement dans le conteneur DI

---

## Notes

- Les propriétés `$name`, `$redirectUri`, `$isConfidential` sont issues du trait `ClientTrait` de `league/oauth2-server` — les setters les surchargent via `#[\AllowDynamicProperties]`.
- Le secret du client n'est pas stocké dans cette entité — il est validé directement dans `ClientRepository::validateClient()` via un hash SHA-256.
