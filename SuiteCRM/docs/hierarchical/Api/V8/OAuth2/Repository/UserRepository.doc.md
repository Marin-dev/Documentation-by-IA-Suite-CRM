# Fichier : UserRepository.php

**Chemin :** `Api/V8/OAuth2/Repository/UserRepository.php`
**Type :** service
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Repository OAuth2 responsable de l'authentification des utilisateurs dans le flux `password` grant. Vérifie les identifiants (nom d'utilisateur + mot de passe) via les beans SuiteCRM et retourne une `UserEntity` si l'authentification réussit. Implémente `UserRepositoryInterface` de `league/oauth2-server`.

---

## Type

service

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `Api\V8\BeanDecorator\BeanManager` | Accès au bean `Users` |
| `Api\V8\OAuth2\Entity\UserEntity` | Entité retournée en cas de succès |
| `League\OAuth2\Server\Entities\ClientEntityInterface` | Paramètre de l'interface — non utilisé dans l'implémentation |
| `League\OAuth2\Server\Repositories\UserRepositoryInterface` | Interface du repository à implémenter |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `UserRepository` | classe | Repository d'authentification utilisateur OAuth2 |
| `getUserEntityByUserCredentials(string $username, string $password, string $grantType, ClientEntityInterface $clientEntity)` | méthode publique | Vérifie les identifiants et retourne une `UserEntity` ou lève une exception |

---

## Interactions

**Appelé par :**
- `Api/V8/Config/services/middlewares.php` — enregistrement DI

**Appelle :**
- `BeanManager::newBeanSafe('Users')` — chargement du bean utilisateur (ligne 37)
- `\User::retrieve_by_string_fields(['user_name' => $username])` — recherche par nom (ligne 38)
- `\User::checkPassword($password, $user->user_hash)` — vérification du mot de passe (ligne 46)
- `new UserEntity($user->id)` — création de l'entité retournée (ligne 50)

---

## Notes

- Lève `\InvalidArgumentException` si l'utilisateur n'existe pas (ligne 43) ou si le mot de passe est invalide (ligne 47). Les messages d'erreur exposent le nom d'utilisateur et le mot de passe en clair — risque potentiel d'information disclosure dans les logs ou les réponses d'erreur en mode debug.
- `\User::checkPassword()` est une méthode statique SuiteCRM — elle compare le mot de passe fourni avec le hash stocké dans `user_hash`.
- Le paramètre `$grantType` et `$clientEntity` sont requis par l'interface mais non utilisés dans cette implémentation.
