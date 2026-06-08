# 📄 UserPreferencesService.php

**Chemin :** `Api/V8/Service/UserPreferencesService.php`
**Type :** PHP (service)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Service de récupération des préférences utilisateur SuiteCRM. Retourne l'ensemble des catégories de préférences d'un utilisateur donné, désérialisées depuis la table `user_preferences`. Vérifie que l'utilisateur courant a le droit d'accéder aux préférences demandées (soi-même ou admin).

**Type :** service

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `Api\V8\BeanDecorator\BeanManager` | Récupération du bean utilisateur |
| `Api\V8\JsonApi\Response\{AttributeResponse, DataResponse, DocumentResponse}` | Construction de la réponse JSON:API |
| `Api\V8\Param\GetUserPreferencesParams` | Paramètres validés |
| `DBManagerFactory` | Accès direct à la base de données |
| `SuiteCRM\Exception\AccessDeniedException` | Exception d'accès refusé |

---

## Exports / Symboles principaux

**Classe :** `Api\V8\Service\UserPreferencesService`

| Méthode | Signature | Description |
|---|---|---|
| `__construct` | `(BeanManager $beanManager)` | Injection du BeanManager |
| `getUserPreferences` | `(GetUserPreferencesParams $params): DocumentResponse` | Retourne les préférences de l'utilisateur |

---

## Flux de `getUserPreferences`

1. Vérifie que `$params->getUserId() === $GLOBALS['current_user']->id` OU que l'utilisateur courant est admin → sinon `AccessDeniedException`
2. Récupère le bean utilisateur via `BeanManager::getBeanSafe('Users', userId)`
3. Requête SQL directe sur `user_preferences` : `WHERE assigned_user_id = ? AND deleted = 0`
4. Désérialise chaque ligne : `unserialize(base64_decode($row['contents']), ['allowed_classes' => false])`
5. Retourne `DocumentResponse` avec `DataResponse(type: 'UserPreference', id: userId)` + `AttributeResponse($preferences)`

---

## Interactions

- **Appelé par :** `UserPreferencesController` (route `GET /V8/user-preferences/{id}`)
- **Consommé dans DI :** `Api/V8/Config/services/services.php`
- **Appelle :** `DBManagerFactory::getInstance()`, `$db->query`, `$db->fetchByAssoc`

---

## Notes

- Utilise `DBManagerFactory::getInstance()` directement (contournement du `BeanManager`) pour une requête SQL brute — incohérence d'accès aux données.
- La requête SQL contient `$user->id` directement interpolé (ligne 94) — risque d'injection SQL si `$user->id` n'est pas sanitisé. Cependant `getBeanSafe` valide que l'utilisateur existe, ce qui réduit le risque.
- `unserialize` avec `['allowed_classes' => false]` est la protection PHP contre la désérialisation d'objets (PHP 7+).
- `guard` `sugarEntry` présent (lignes 51-53).
- Variables globales utilisées : `$GLOBALS['current_user']` pour la vérification d'identité et admin.
