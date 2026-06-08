# Fichier : ScopeRepository.php

**Chemin :** `Api/V8/OAuth2/Repository/ScopeRepository.php`
**Type :** service
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Repository OAuth2 gérant les scopes d'autorisation. Implémente `ScopeRepositoryInterface` de `league/oauth2-server`. Dans l'état actuel, les scopes ne sont pas gérés fonctionnellement : `getScopeEntityByIdentifier()` ne retourne rien et `finalizeScopes()` retourne les scopes en l'état sans filtrage.

---

## Type

service

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `League\OAuth2\Server\Entities\ClientEntityInterface` | Paramètre de `finalizeScopes()` — non utilisé |
| `League\OAuth2\Server\Repositories\ScopeRepositoryInterface` | Interface du repository à implémenter |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `ScopeRepository` | classe | Repository de scopes OAuth2 — implémentation minimale |
| `getScopeEntityByIdentifier(string $identifier)` | méthode publique | Retourne `null` (non implémenté) |
| `finalizeScopes(array $scopes, string $grantType, ClientEntityInterface, ?string $userIdentifier)` | méthode publique | Retourne les scopes sans modification |

---

## Interactions

**Appelé par :**
- `Api/V8/Config/services/middlewares.php` — enregistrement DI

---

## Notes

- Implementation stub : les scopes ne sont pas validés ni filtrés (commentaire ligne 22 : "we just return scopes for now").
- `getScopeEntityByIdentifier()` n'a pas de corps de retour — retourne implicitement `null`. Cela signifie que toute logique de validation de scope côté `league/oauth2-server` sera inopérante.
- Point d'attention : si les scopes OAuth2 doivent être restreints à l'avenir, c'est cette classe qui doit être complétée en priorité.
