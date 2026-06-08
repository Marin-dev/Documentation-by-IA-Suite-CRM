# Fichier : ClientRepository.php

**Chemin :** `Api/V8/OAuth2/Repository/ClientRepository.php`
**Type :** service
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Repository OAuth2 responsable de la récupération et de la validation des clients OAuth2 enregistrés dans SuiteCRM. Implémente `ClientRepositoryInterface` de `league/oauth2-server`. Vérifie le secret client via SHA-256 et contrôle le type de grant autorisé.

---

## Type

service

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `Api\V8\BeanDecorator\BeanManager` | Accès au bean `OAuth2Clients` |
| `Api\V8\OAuth2\Entity\ClientEntity` | Entité client injectée et populée dans `getClientEntity()` |
| `League\OAuth2\Server\Repositories\ClientRepositoryInterface` | Interface du repository à implémenter |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `ClientRepository` | classe | Repository de gestion des clients OAuth2 |
| `getClientEntity(string $clientIdentifier)` | méthode publique | Récupère et retourne l'entité client depuis le bean `OAuth2Clients` |
| `validateClient(string $clientIdentifier, ?string $clientSecret, ?string $grantType)` | méthode publique | Valide l'identité du client (secret + type de grant autorisé) |

---

## Interactions

**Appelé par :**
- `Api/V8/Config/services/middlewares.php` — enregistrement DI

**Appelle :**
- `BeanManager::getBeanSafe(OAuth2Clients::class, $clientIdentifier)` — récupération du bean client (lignes 37, 50)
- `ClientEntity::setIdentifier()`, `setName()`, `setRedirectUri()`, `setIsConfidential()` — population de l'entité (lignes 39-42)
- `hash('sha256', $clientSecret)` — comparaison avec `$client->secret` pour validation (ligne 54)

---

## Notes

- La validation du secret utilise SHA-256 sans sel (`hash('sha256', $clientSecret) === $client->secret`) (ligne 54). Le stockage du secret côté `OAuth2Clients` doit également être en SHA-256 pour que la comparaison fonctionne.
- Le grant `refresh_token` est toujours autorisé quelle que soit la valeur de `allowed_grant_type` (ligne 52 : `|| $grantType === 'refresh_token'`).
- `getClientEntity()` retourne toujours la même instance de `ClientEntity` (injectée), dont les propriétés sont réécrites à chaque appel — pas de protection contre les appels concurrents.
