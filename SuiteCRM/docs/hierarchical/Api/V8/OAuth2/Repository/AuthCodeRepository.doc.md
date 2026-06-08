# Fichier : AuthCodeRepository.php

**Chemin :** `Api/V8/OAuth2/Repository/AuthCodeRepository.php`
**Type :** service
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Repository OAuth2 gérant le cycle de vie des codes d'autorisation (`authorization_code` grant). Persiste les codes en base, les révoque et vérifie leur validité. Implémente `AuthCodeRepositoryInterface` de `league/oauth2-server`.

---

## Type

service

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `Api\V8\BeanDecorator\BeanManager` | Accès au bean `OAuth2AuthCodes` |
| `Api\V8\OAuth2\Entity\AuthCodeEntity` | Entité retournée par `getNewAuthCode()` |
| `League\OAuth2\Server\Entities\AuthCodeEntityInterface` | Interface de l'entité code d'autorisation |
| `League\OAuth2\Server\Repositories\AuthCodeRepositoryInterface` | Interface du repository à implémenter |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `AuthCodeRepository` | classe | Repository de gestion des codes d'autorisation OAuth2 |
| `persistNewAuthCode(AuthCodeEntityInterface)` | méthode publique | Persiste le code d'autorisation en base |
| `revokeAuthCode(string $codeId)` | méthode publique | Révoque le code (suppression ou marquage selon `auto_authorize`) |
| `isAuthCodeRevoked(string $codeId)` | méthode publique | Vérifie si le code est révoqué via `OAuth2AuthCodes::is_revoked()` |
| `getNewAuthCode()` | méthode publique | Instancie et retourne une nouvelle `AuthCodeEntity` |

---

## Interactions

**Appelé par :**
- `Api/V8/Config/services/middlewares.php` — enregistrement DI

**Appelle :**
- `BeanManager::newBeanSafe(OAuth2AuthCodes::class)` — création/lecture du bean (lignes 38, 55, 79)
- `OAuth2AuthCodes::retrieve_by_string_fields()` — recherche par code
- `OAuth2AuthCodes::mark_deleted()` — révocation par suppression (ligne 70)
- `OAuth2AuthCodes::is_revoked()` — vérification de révocation (ligne 84)

---

## Notes

- `persistNewAuthCode()` lit la variable `$_POST['confirmed']` pour déterminer si la demande est "toujours autorisée" (`auto_authorize`) (ligne 44). Ce couplage direct avec `$_POST` est un point d'attention (testabilité réduite).
- `revokeAuthCode()` a deux comportements distincts selon `auto_authorize` : si `'1'`, le code est marqué révoqué mais conservé en base (`auth_code_is_revoked = '1'`) ; sinon, il est supprimé via `mark_deleted` (lignes 64-70).
- Lève `\InvalidArgumentException` si le code à révoquer n'existe pas (ligne 58-61).
