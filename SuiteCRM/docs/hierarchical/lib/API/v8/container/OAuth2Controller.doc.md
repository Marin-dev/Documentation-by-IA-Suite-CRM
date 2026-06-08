# Fichier : OAuth2Controller.php (container)

**Chemin :** `lib/API/v8/container/OAuth2Controller.php`
**Type :** PHP — configuration (DI factory)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Factory de conteneur Slim qui instancie `OAuth2Controller` et injecte le logger. Enregistre le service sous la clé `'OAuth2Controller'`.

**Type :** configuration

---

## Ce que ce fichier configure

| Clé container | Classe instanciée | Services injectés |
|---|---|---|
| `OAuth2Controller` | `SuiteCRM\API\v8\Controller\OAuth2Controller` | `$container`, `LoggerInterface` |

---

## Interactions

- **Produit :** `OAuth2Controller` — utilisé par la route `POST /oauth/access_token`
- **Consomme :** `Psr\Log\LoggerInterface`
