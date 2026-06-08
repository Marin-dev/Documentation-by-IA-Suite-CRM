# Fichier : AuthorizationServer.php (container)

**Chemin :** `lib/API/v8/container/AuthorizationServer.php`
**Type :** PHP — configuration (DI factory)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Factory qui configure et instancie le serveur d'autorisation OAuth2 (League OAuth2 Server). Configure deux grants : `PasswordGrant` (username/password, token 1h, refresh 1 mois) et `ClientCredentialsGrant` (application-to-application, mêmes TTL). Charge les clés RSA depuis `SuiteCRM\API\OAuth2\Keys`.

**Type :** configuration

---

## Ce que ce fichier configure

| Clé container | Classe instanciée | Description |
|---|---|---|
| `AuthorizationServer` | `SuiteCRM\API\OAuth2\Middleware\AuthorizationServer` | Serveur OAuth2 avec 2 grants |

### Grants configurés

| Grant | TTL Token | TTL Refresh |
|---|---|---|
| `PasswordGrant` | 1 heure (`PT1H`) | 1 mois (`P1M`) |
| `ClientCredentialsGrant` | 1 heure (`PT1H`) | 1 mois (`P1M`) |

---

## Paramètres clés

| Paramètre | Valeur | Source |
|---|---|---|
| Clé privée | `$keys->getPrivateKey()` | `SuiteCRM\API\OAuth2\Keys` |
| Clé publique | `$keys->getPublicKey()` | `SuiteCRM\API\OAuth2\Keys` |
| Clé de chiffrement | `base64_encode(random_bytes(32))` | Générée aléatoirement **à chaque requête** |

---

## Interactions

- **Produit :** `AuthorizationServer` — consommé par `OAuth2Controller::authenticate()`
- **Consomme :**
  - `SuiteCRM\API\OAuth2\Repositories\ClientRepository`
  - `SuiteCRM\API\OAuth2\Repositories\AccessTokenRepository`
  - `SuiteCRM\API\OAuth2\Repositories\ScopeRepository`
  - `SuiteCRM\API\OAuth2\Repositories\UserRepository`
  - `SuiteCRM\API\OAuth2\Repositories\RefreshTokenRepository`

---

## Notes

- **Point d'attention :** `base64_encode(random_bytes(32))` génère une clé de chiffrement aléatoire à chaque instanciation (chaque requête). Cela peut provoquer des problèmes de déchiffrement des tokens entre requêtes si la clé change. Ce pattern peut indiquer que le chiffrement symétrique n'est pas utilisé en pratique dans ce contexte (JWT signé asymétriquement).
