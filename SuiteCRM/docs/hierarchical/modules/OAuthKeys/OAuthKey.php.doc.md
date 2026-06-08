# 📄 OAuthKey.php

**Chemin :** `modules/OAuthKeys/OAuthKey.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Modèle représentant une clé consommateur OAuth 1.0 (consumer key/secret). Utilisé pour authentifier les applications tierces via OAuth 1.0 (SOAP/REST legacy de SugarCRM CE). Distinct du système OAuth2 V8.

## Rôle technique

Classe `OAuthKey` héritant de `Basic` (table `oauth_consumer`). Fournit une méthode de recherche par `c_key` avec cache statique, et surcharge `mark_deleted()` pour supprimer physiquement la clé et tous ses tokens associés.

---

## Dépendances clés

- `Basic` (framework SuiteCRM) — classe parente ORM
- `DBManager` (`$this->db`) — requêtes DELETE directes
- `BeanFactory::registerBean()` — enregistrement en cache BeanFactory

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `OAuthKey` | classe | Modèle clé consommateur OAuth 1.0 |
| `getByKey($key)` | méthode | Récupère une clé par sa valeur `c_key` |
| `fetchKey($key)` | méthode statique | Récupère une clé avec cache statique |
| `mark_deleted($id)` | méthode | Suppression physique de la clé ET de tous ses tokens |
| `$keys_cache` | tableau statique | Cache des clés par valeur `c_key` |

## Champs principaux

| Champ | Rôle |
|---|---|
| `c_key` | Clé consommateur publique |
| `c_secret` | Secret consommateur (chiffré) |
| `name` | Nom descriptif |

---

## Relations clés

- **Appelé par :** `modules/OAuthTokens/OAuthToken.php` — `BeanFactory::getBean('OAuthKeys', ...)`
- **Appelle :** `DBManager` (DELETE direct sur `oauth_consumer` et `oauth_tokens`)
- **Position dans le flux global :** authentification OAuth 1.0 legacy (SOAP/REST CE)

---

## Notes

- La suppression est physique (DELETE, pas soft delete) — ligne 103-104.
- Le cache statique `$keys_cache` persiste pendant toute la durée de la requête PHP.
- `disable_row_level_security = true`.
