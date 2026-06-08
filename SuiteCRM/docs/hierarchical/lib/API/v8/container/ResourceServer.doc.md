# Fichier : ResourceServer.php (container)

**Chemin :** `lib/API/v8/container/ResourceServer.php`
**Type :** PHP — configuration (DI factory)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Factory qui instancie le middleware de validation des tokens Bearer OAuth2 (`ResourceServer`). Ce middleware vérifie que chaque requête entrante porte un token JWT valide et l'ajoute aux attributs de la requête.

**Type :** configuration

---

## Ce que ce fichier configure

| Clé container | Classe instanciée | Description |
|---|---|---|
| `ResourceServer` | `SuiteCRM\API\OAuth2\Middleware\ResourceServer` | Middleware OAuth2 validation token |

---

## Paramètres clés

| Paramètre | Valeur | Description |
|---|---|---|
| Clé publique | `$keys->getPublicKey()` | Vérifie la signature JWT |
| `AccessTokenRepository` | `SuiteCRM\API\OAuth2\Repositories\AccessTokenRepository` | Vérification de révocation |

---

## Interactions

- **Produit :** `ResourceServer` — enregistré comme middleware Slim dans `lib/API/v8/callable/oauth2.php`
- **Consomme :**
  - `SuiteCRM\API\OAuth2\Keys`
  - `SuiteCRM\API\OAuth2\Repositories\AccessTokenRepository`
  - `League\OAuth2\Server\ResourceServer`
